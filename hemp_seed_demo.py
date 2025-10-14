#!/usr/bin/env python3
"""
Hemp Seed App - Demo Mode
This is a standalone version that works without the Llama model for testing the UI.
"""

from flask import Flask, render_template, request, jsonify, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Mock responses for demo
DEMO_RESPONSES = {
    "default": "Thank you for your interest in The Hemp Seed! Our hemp seeds are packed with nutrition. They're a complete protein source with all 9 essential amino acids, rich in Omega-3 and Omega-6 fatty acids, and loaded with vitamins and minerals. Would you like to know more about our products, recipes, or health benefits?",
    "products": "We have 6 amazing products:\n\n1. Organic Raw Hemp Seeds - $12.99 (16 oz)\n2. Cold-Pressed Hemp Seed Oil - $18.99 (8 fl oz)\n3. Hemp Protein Powder - $24.99 (1 lb)\n4. Hemp Seed Butter - $15.99 (12 oz)\n5. Roasted Hemp Seeds - $9.99 (8 oz)\n6. Hemp Seed Flour - $13.99 (16 oz)\n\nWhich one interests you most?",
    "recipe": "Here's a delicious Hemp Seed Smoothie recipe:\n\n🥤 Ingredients:\n- 2 tablespoons hemp seeds\n- 1 banana\n- 1 cup mixed berries\n- 1 cup almond milk\n- 1 tablespoon honey (optional)\n- Ice cubes\n\nBlend everything until smooth and enjoy! This smoothie provides complete protein, healthy fats, and tons of antioxidants. Perfect for breakfast or post-workout!",
    "benefits": "Hemp seeds offer incredible health benefits:\n\n💚 Complete protein with all 9 essential amino acids\n🧠 Rich in Omega-3 and Omega-6 (perfect 3:1 ratio)\n❤️ Supports heart health\n🦴 High in minerals (magnesium, zinc, iron)\n🌟 Anti-inflammatory properties\n💪 Aids muscle recovery\n✨ Improves skin health\n\nThey're a true superfood!"
}

@app.route('/')
def index():
    if 'conversation' not in session:
        session['conversation'] = []
    return render_template('hemp_seed.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').strip().lower()
    
    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400
    
    # Simple keyword matching for demo
    if any(word in user_message for word in ['product', 'sell', 'buy', 'price', 'cost']):
        response = DEMO_RESPONSES['products']
    elif any(word in user_message for word in ['recipe', 'cook', 'make', 'prepare', 'eat']):
        response = DEMO_RESPONSES['recipe']
    elif any(word in user_message for word in ['benefit', 'health', 'nutrition', 'good', 'why']):
        response = DEMO_RESPONSES['benefits']
    else:
        response = DEMO_RESPONSES['default']
    
    # Get or initialize conversation history
    if 'conversation' not in session:
        session['conversation'] = []
    
    conversation = session['conversation']
    conversation.append({"role": "user", "content": user_message})
    conversation.append({"role": "assistant", "content": response})
    
    session['conversation'] = conversation
    
    return jsonify({
        'response': response,
        'conversation_length': len(conversation) // 2
    })

@app.route('/api/reset', methods=['POST'])
def reset():
    session['conversation'] = []
    return jsonify({'status': 'Conversation reset successfully'})

@app.route('/api/products', methods=['GET'])
def products():
    products_list = [
        {
            "name": "Organic Raw Hemp Seeds",
            "description": "Premium quality, unprocessed hemp seeds",
            "price": "$12.99",
            "size": "16 oz"
        },
        {
            "name": "Cold-Pressed Hemp Seed Oil",
            "description": "Extra virgin, unrefined hemp oil",
            "price": "$18.99",
            "size": "8 fl oz"
        },
        {
            "name": "Hemp Protein Powder",
            "description": "50% protein content, easy to digest",
            "price": "$24.99",
            "size": "1 lb"
        },
        {
            "name": "Hemp Seed Butter",
            "description": "Creamy, spreadable, great alternative",
            "price": "$15.99",
            "size": "12 oz"
        },
        {
            "name": "Roasted Hemp Seeds",
            "description": "Lightly salted, crunchy snack",
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

if __name__ == '__main__':
    print("🌿 Starting The Hemp Seed web application (DEMO MODE)...")
    print("🌐 Open your browser and navigate to: http://127.0.0.1:5000")
    print("💬 This is a demo version with pre-programmed responses.")
    print("\nPress Ctrl+C to stop the server.\n")
    app.run(host='127.0.0.1', port=5000, debug=False)
