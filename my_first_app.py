#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

"""
My First Llama 3 App - Story Generator

This is a simple example application that generates creative stories using Llama 3.
It demonstrates basic usage of the Llama 3 API for text generation.
"""
from typing import Optional
import fire
from llama import Llama


def generate_story(
    ckpt_dir: str,
    tokenizer_path: str,
    topic: str = "a brave knight",
    max_seq_len: int = 512,
    max_batch_size: int = 1,
):
    """
    Generate a short story based on a topic.
    
    Args:
        ckpt_dir: Path to the model checkpoint directory
        tokenizer_path: Path to the tokenizer model
        topic: The topic for the story
        max_seq_len: Maximum sequence length
        max_batch_size: Maximum batch size
    
    Example:
        torchrun --nproc_per_node 1 my_first_app.py \
            --ckpt_dir Meta-Llama-3-8B-Instruct/ \
            --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
            --topic "a space explorer discovering a new planet"
    """
    print("🚀 Loading Llama 3 model...")
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    print("✅ Model loaded!\n")

    # Create a story prompt
    prompt = f"Write a short, creative story about {topic}. Make it engaging and fun!"
    
    print(f"📝 Topic: {topic}\n")
    print("Generating story...\n")
    
    # Generate the story
    dialogs = [[{"role": "user", "content": prompt}]]
    
    results = generator.chat_completion(
        dialogs,
        max_gen_len=512,
        temperature=0.8,  # More creative
        top_p=0.9,
    )
    
    story = results[0]['generation']['content']
    print("📖 Generated Story:")
    print("=" * 60)
    print(story)
    print("=" * 60)


if __name__ == "__main__":
    fire.Fire(generate_story)
