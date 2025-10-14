#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

"""
Interactive Chatbot using Llama 3

This application creates an interactive chatbot that maintains conversation history
and can respond to multiple turns of dialogue.
"""
from typing import List
import fire
from llama import Dialog, Llama


def chat(
    ckpt_dir: str,
    tokenizer_path: str,
    max_seq_len: int = 2048,
    max_batch_size: int = 1,
    system_prompt: str = "You are a helpful, friendly AI assistant. Be concise and engaging.",
):
    """
    Run an interactive chatbot session.
    
    Args:
        ckpt_dir: Path to the model checkpoint directory
        tokenizer_path: Path to the tokenizer model
        max_seq_len: Maximum sequence length
        max_batch_size: Maximum batch size
        system_prompt: System prompt to define chatbot personality
    
    Example:
        torchrun --nproc_per_node 1 interactive_chatbot.py \
            --ckpt_dir Meta-Llama-3-8B-Instruct/ \
            --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
    """
    print("🤖 Loading Llama 3 Chatbot...")
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    print("✅ Chatbot ready! Type 'quit' to exit.\n")
    
    # Store conversation history
    conversation: Dialog = []
    
    # Set system prompt to define chatbot personality
    conversation.append({
        "role": "system",
        "content": system_prompt
    })
    
    print("👋 Hello! I'm your Llama 3 assistant. How can I help you today?\n")
    
    while True:
        # Get user input
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye! Have a great day!")
            break
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye! Have a great day!")
            break
        
        if not user_input:
            continue
        
        # Add user message to conversation
        conversation.append({"role": "user", "content": user_input})
        
        # Generate response
        try:
            results = generator.chat_completion(
                [conversation],
                max_gen_len=512,
                temperature=0.7,
                top_p=0.9,
            )
            
            assistant_message = results[0]['generation']['content']
            
            # Add assistant response to conversation
            conversation.append({"role": "assistant", "content": assistant_message})
            
            print(f"\nAssistant: {assistant_message}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            # Remove the last user message if generation failed
            conversation.pop()


if __name__ == "__main__":
    fire.Fire(chat)
