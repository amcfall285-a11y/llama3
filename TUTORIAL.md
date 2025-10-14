# Building an App with Llama 3: Step-by-Step Tutorial

This tutorial will guide you through building a simple application using Llama 3. We'll start from scratch and build up to a functional chatbot application.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Step 1: Environment Setup](#step-1-environment-setup)
3. [Step 2: Install Dependencies](#step-2-install-dependencies)
4. [Step 3: Download the Model](#step-3-download-the-model)
5. [Step 4: Understanding the Basics](#step-4-understanding-the-basics)
6. [Step 5: Build Your First App](#step-5-build-your-first-app)
7. [Step 6: Build an Interactive Chatbot](#step-6-build-an-interactive-chatbot)
8. [Step 7: Customize Your App](#step-7-customize-your-app)
9. [Next Steps](#next-steps)

## Prerequisites

Before starting, make sure you have:
- Python 3.8 or higher installed
- CUDA-capable GPU (recommended) or CPU
- At least 16GB of RAM (for 8B model)
- Basic knowledge of Python
- Command line/terminal familiarity

## Step 1: Environment Setup

First, let's set up a proper Python environment:

```bash
# Create a new conda environment (recommended)
conda create -n llama3-app python=3.10
conda activate llama3-app

# Or use venv if you prefer
python -m venv llama3-env
source llama3-env/bin/activate  # On Windows: llama3-env\Scripts\activate
```

## Step 2: Install Dependencies

Clone the repository and install required packages:

```bash
# Clone the repository
git clone https://github.com/meta-llama/llama3.git
cd llama3

# Install the package and dependencies
pip install -e .

# Verify installation
python -c "import llama; print('Llama 3 installed successfully!')"
```

The key dependencies are:
- `torch` - PyTorch for deep learning
- `fairscale` - For model parallelism
- `fire` - For CLI argument parsing
- `tiktoken` - For tokenization

## Step 3: Download the Model

You need to download the Llama 3 model weights:

1. Visit [Meta Llama website](https://llama.meta.com/llama-downloads/) and register
2. Accept the license agreement
3. You'll receive an email with a download URL
4. Run the download script:

```bash
# Make the script executable
chmod +x download.sh

# Run the download script
./download.sh
```

When prompted:
- Enter the URL from your email
- Select the model size (8B recommended for getting started)
- Wait for the download to complete

The model will be downloaded to a directory like `Meta-Llama-3-8B-Instruct/`

## Step 4: Understanding the Basics

### Key Concepts

**Tokenizer**: Converts text to tokens (numbers) that the model understands
```python
from llama import Llama

# The tokenizer breaks text into pieces
# Example: "Hello world" -> [15339, 1917]
```

**Model Parameters**:
- `max_seq_len`: Maximum sequence length (up to 8192 for Llama 3)
- `max_batch_size`: How many prompts to process at once
- `temperature`: Controls randomness (0.0 = deterministic, 1.0 = creative)
- `top_p`: Controls diversity of responses

### Try the Examples

Run the provided examples to see Llama 3 in action:

```bash
# For chat completion (instruction-tuned models)
torchrun --nproc_per_node 1 example_chat_completion.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --max_seq_len 512 --max_batch_size 4

# For text completion (pretrained models)
torchrun --nproc_per_node 1 example_text_completion.py \
    --ckpt_dir Meta-Llama-3-8B/ \
    --tokenizer_path Meta-Llama-3-8B/tokenizer.model \
    --max_seq_len 128 --max_batch_size 4
```

## Step 5: Build Your First App

Let's create a simple app that generates a story:

Create a file named `my_first_app.py`:

```python
#!/usr/bin/env python3
"""
My First Llama 3 App - Story Generator
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
```

Run your app:

```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "a space explorer discovering a new planet"
```

## Step 6: Build an Interactive Chatbot

Now let's create a more interactive application - a chatbot!

Create a file named `interactive_chatbot.py`:

```python
#!/usr/bin/env python3
"""
Interactive Chatbot using Llama 3
"""
from typing import List
import fire
from llama import Dialog, Llama

def chat(
    ckpt_dir: str,
    tokenizer_path: str,
    max_seq_len: int = 2048,
    max_batch_size: int = 1,
):
    """
    Run an interactive chatbot session.
    
    Args:
        ckpt_dir: Path to the model checkpoint directory
        tokenizer_path: Path to the tokenizer model
        max_seq_len: Maximum sequence length
        max_batch_size: Maximum batch size
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
    
    # Optional: Set a system prompt to define chatbot personality
    system_prompt = {
        "role": "system",
        "content": "You are a helpful, friendly AI assistant. Be concise and engaging."
    }
    conversation.append(system_prompt)
    
    print("👋 Hello! I'm your Llama 3 assistant. How can I help you today?\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
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
```

Run your chatbot:

```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

## Step 7: Customize Your App

### Add Different Personalities

You can customize the chatbot's personality by changing the system prompt:

```python
# Professional assistant
system_prompt = {
    "role": "system",
    "content": "You are a professional business consultant. Provide expert advice."
}

# Creative writer
system_prompt = {
    "role": "system",
    "content": "You are a creative writer. Respond with vivid imagery and poetic language."
}

# Code helper
system_prompt = {
    "role": "system",
    "content": "You are a programming expert. Help with coding questions and provide clear examples."
}
```

### Adjust Generation Parameters

Control the output style with these parameters:

```python
results = generator.chat_completion(
    dialogs,
    max_gen_len=256,        # Shorter responses
    temperature=0.3,        # More focused and deterministic
    top_p=0.9,              # Consider top 90% probable tokens
)

# For creative writing
results = generator.chat_completion(
    dialogs,
    max_gen_len=1024,       # Longer responses
    temperature=0.9,        # More creative and random
    top_p=0.95,             # More diversity
)
```

### Add Features

Here are ideas to extend your app:

1. **Save Conversation History**
```python
import json

# Save conversation
with open('conversation.json', 'w') as f:
    json.dump(conversation, f, indent=2)

# Load conversation
with open('conversation.json', 'r') as f:
    conversation = json.load(f)
```

2. **Add Logging**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"User: {user_input}")
logger.info(f"Assistant: {assistant_message}")
```

3. **Create a Web Interface**
```python
# Use Flask or FastAPI to create a web UI
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_message = request.json['message']
    # Process with Llama 3
    return jsonify({'response': assistant_message})
```

## Next Steps

Now that you've built your first Llama 3 apps, here are some ideas to explore:

1. **Build Specific Applications**:
   - Q&A system for your documents
   - Code review assistant
   - Creative writing tool
   - Language tutor
   - Summarization tool

2. **Optimize Performance**:
   - Use quantization for faster inference
   - Implement caching for repeated queries
   - Batch multiple requests together

3. **Add Safety Features**:
   - Input validation and filtering
   - Output moderation
   - Rate limiting
   - User authentication

4. **Deploy Your App**:
   - Create a REST API with FastAPI
   - Build a web interface with Streamlit
   - Deploy to cloud (AWS, GCP, Azure)
   - Containerize with Docker

5. **Learn More**:
   - Check out the [Llama Cookbook](https://github.com/meta-llama/llama-recipes)
   - Read the [Model Card](MODEL_CARD.md)
   - Review the [Responsible Use Guide](https://ai.meta.com/static-resource/responsible-use-guide/)

## Troubleshooting

### Common Issues

**Out of Memory Error**:
- Reduce `max_seq_len` or `max_batch_size`
- Use a smaller model (8B instead of 70B)
- Close other GPU-intensive applications

**CUDA Not Available**:
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
```

**Model Loading Fails**:
- Verify the checkpoint directory path
- Ensure all model files are downloaded
- Check file permissions

**Slow Generation**:
- Use GPU instead of CPU
- Reduce `max_gen_len`
- Use smaller model for development

## Resources

- [Official Llama 3 Repository](https://github.com/meta-llama/llama3)
- [Llama Cookbook](https://github.com/meta-llama/llama-recipes)
- [Model Card](MODEL_CARD.md)
- [Hugging Face Models](https://huggingface.co/meta-llama)

## Support

If you encounter issues:
1. Check the [FAQ](https://llama.meta.com/faq)
2. Search [GitHub Issues](https://github.com/meta-llama/llama3/issues)
3. Review the [Contributing Guide](CONTRIBUTING.md)

Happy building! 🚀
