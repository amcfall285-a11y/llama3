#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

"""
The Hemp Seed - AI-Powered Business Web Application

This is a Flask-based web application for The Hemp Seed business that uses
Llama 3 to provide an intelligent customer service assistant. The assistant
can answer questions about hemp seeds, their benefits, products, and recipes.
"""

from flask import Flask, render_template, request, jsonify, session
from typing import List, Dict
import fire
from llama import Llama
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Global variable to hold the Llama generator
generator = None

# Hemp Seed business knowledge base
HEMP_SEED_INFO = """
The Hemp Seed - Your Premium Hemp Products Store

Products:
- Organic Hemp Seeds (Raw, Hulled, Roasted)
- Hemp Seed Oil (Cold-pressed, Extra Virgin)
- Hemp Protein Powder
- Hemp Seed Butter
- Hemp Seed Flour
- Hemp Seed Snacks

Benefits of Hemp Seeds:
- Rich in Omega-3 and Omega-6 fatty acids
- Complete protein source with all 9 essential amino acids
- High in fiber, vitamins, and minerals
- Supports heart health and brain function
- May reduce inflammation
- Promotes healthy skin and hair
- Aids in digestion

Popular Uses:
- Smoothies and protein shakes
- Salad toppings
- Baking (bread, muffins, cookies)
- Yogurt and oatmeal topping
- Energy bars and snacks
- Pesto and sauces
- Hemp milk (dairy alternative)

Recipes:
1. Hemp Seed Smoothie: Blend 2 tbsp hemp seeds, banana, berries, almond milk
2. Hemp Energy Balls: Mix hemp seeds, dates, cocoa, roll into balls
3. Hemp Pesto: Blend hemp seeds, basil, garlic, olive oil, parmesan
4. Hemp Granola: Mix oats, hemp seeds, honey, nuts, bake until golden

Store Information:
- Location: Organic Market District
- Hours: Mon-Sat 9am-7pm, Sun 10am-5pm
- Shipping: Free shipping on orders over $50
- Contact: info@thehemp seed.com
"""


def initialize_llama(ckpt_dir: str, tokenizer_path: str, max_seq_len: int = 2048):
    """Initialize the Llama model for the web application."""
    global generator
    print("🚀 Loading Llama 3 model for The Hemp Seed app...")
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=1,
    )
    print("✅ Model loaded successfully!\n")


@app.route('/')
def index():
    """Render the main page."""
    # Initialize conversation history if not exists
    if 'conversation' not in session:
        session['conversation'] = []
    return render_template('hemp_seed.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages from the user."""
    if generator is None:
        return jsonify({
            'error': 'Llama model not initialized. Please start the server with model parameters.'
        }), 500
    
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400
    
    # Get or initialize conversation history
    if 'conversation' not in session:
        session['conversation'] = []
    
    conversation = session['conversation']
    
    # Create system prompt with hemp seed knowledge
    system_prompt = {
        "role": "system",
        "content": f"""You are a helpful and friendly customer service assistant for The Hemp Seed, 
a business specializing in premium hemp seed products. Use the following information to answer 
customer questions accurately and enthusiastically:

{HEMP_SEED_INFO}

Be conversational, informative, and always promote the health benefits and versatility of hemp seeds.
If asked about something outside of hemp seeds or The Hemp Seed business, politely redirect the 
conversation back to hemp products."""
    }
    
    # Build dialog with system prompt, conversation history, and new message
    dialog = [system_prompt] + conversation + [{"role": "user", "content": user_message}]
    
    try:
        # Generate response
        results = generator.chat_completion(
            [dialog],
            max_gen_len=512,
            temperature=0.7,
            top_p=0.9,
        )
        
        assistant_message = results[0]['generation']['content']
        
        # Update conversation history
        conversation.append({"role": "user", "content": user_message})
        conversation.append({"role": "assistant", "content": assistant_message})
        
        # Keep only last 10 exchanges to manage context length
        if len(conversation) > 20:
            conversation = conversation[-20:]
        
        session['conversation'] = conversation
        
        return jsonify({
            'response': assistant_message,
            'conversation_length': len(conversation) // 2
        })
    
    except Exception as e:
        return jsonify({'error': f'Error generating response: {str(e)}'}), 500


@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset the conversation history."""
    session['conversation'] = []
    return jsonify({'status': 'Conversation reset successfully'})


@app.route('/api/products', methods=['GET'])
def products():
    """Return product information."""
    products_list = [
        {
            "name": "Organic Raw Hemp Seeds",
            "description": "Premium quality, unprocessed hemp seeds",
            "price": "$12.99",
            "size": "16 oz"
        },
        {
            "name": "Cold-Pressed Hemp Seed Oil",
            "description": "Extra virgin, nutrient-rich oil",
            "price": "$18.99",
            "size": "8 fl oz"
        },
        {
            "name": "Hemp Protein Powder",
            "description": "50% protein content, perfect for smoothies",
            "price": "$24.99",
            "size": "1 lb"
        },
        {
            "name": "Hemp Seed Butter",
            "description": "Creamy, nutrient-dense spread",
            "price": "$15.99",
            "size": "12 oz"
        },
        {
            "name": "Roasted Hemp Seeds",
            "description": "Lightly salted, ready to eat snack",
            "price": "$9.99",
            "size": "8 oz"
        },
        {
            "name": "Hemp Seed Flour",
            "description": "Gluten-free baking flour",
            "price": "$13.99",
            "size": "16 oz"
        }
    ]
    return jsonify(products_list)


def run_server(
    ckpt_dir: str,
    tokenizer_path: str,
    max_seq_len: int = 2048,
    host: str = "127.0.0.1",
    port: int = 5000,
    debug: bool = False
):
    """
    Start The Hemp Seed web application server.
    
    Args:
        ckpt_dir: Path to the model checkpoint directory
        tokenizer_path: Path to the tokenizer model
        max_seq_len: Maximum sequence length for the model
        host: Host address to bind the server (default: 127.0.0.1)
        port: Port number to run the server (default: 5000)
        debug: Enable Flask debug mode (default: False)
    
    Example:
        python hemp_seed_app.py \
            --ckpt_dir Meta-Llama-3-8B-Instruct/ \
            --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
            --port 5000
    """
    # Initialize the Llama model
    initialize_llama(ckpt_dir, tokenizer_path, max_seq_len)
    
    # Start Flask server
    print(f"🌿 Starting The Hemp Seed web application...")
    print(f"🌐 Open your browser and navigate to: http://{host}:{port}")
    print(f"💬 Chat with our AI assistant about hemp seeds and products!")
    print(f"\nPress Ctrl+C to stop the server.\n")
    
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    fire.Fire(run_server)
