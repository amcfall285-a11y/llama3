# Llama 3 Code Cheatsheet

Quick reference for common Llama 3 patterns and code snippets.

## Basic Setup

```python
from llama import Llama

# Initialize model
generator = Llama.build(
    ckpt_dir="Meta-Llama-3-8B-Instruct/",
    tokenizer_path="Meta-Llama-3-8B-Instruct/tokenizer.model",
    max_seq_len=512,
    max_batch_size=1,
)
```

## Simple Generation

```python
# Single question
dialogs = [[{"role": "user", "content": "What is Python?"}]]

results = generator.chat_completion(
    dialogs,
    max_gen_len=256,
    temperature=0.7,
    top_p=0.9,
)

print(results[0]['generation']['content'])
```

## Conversation with History

```python
# Multi-turn conversation
conversation = [
    {"role": "user", "content": "Tell me about Paris"},
    {"role": "assistant", "content": "Paris is the capital of France..."},
    {"role": "user", "content": "What's the best time to visit?"},
]

results = generator.chat_completion([conversation])
print(results[0]['generation']['content'])
```

## System Prompts

```python
# Helpful assistant
conversation = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "How do I learn Python?"}
]

# Code expert
conversation = [
    {"role": "system", "content": "You are an expert programmer. Provide code examples."},
    {"role": "user", "content": "Show me a bubble sort in Python"}
]

# Creative writer
conversation = [
    {"role": "system", "content": "You are a creative writer. Use vivid imagery."},
    {"role": "user", "content": "Describe a sunset"}
]
```

## Temperature Settings

```python
# Deterministic (factual, consistent)
results = generator.chat_completion(dialogs, temperature=0.1)

# Balanced (default)
results = generator.chat_completion(dialogs, temperature=0.6)

# Creative (varied, imaginative)
results = generator.chat_completion(dialogs, temperature=0.9)
```

## Batch Processing

```python
# Process multiple prompts at once
dialogs = [
    [{"role": "user", "content": "What is AI?"}],
    [{"role": "user", "content": "What is ML?"}],
    [{"role": "user", "content": "What is DL?"}],
]

results = generator.chat_completion(dialogs, max_batch_size=3)

for i, result in enumerate(results):
    print(f"Answer {i+1}: {result['generation']['content']}\n")
```

## Text Completion (Pre-trained models)

```python
prompts = [
    "The meaning of life is",
    "In a galaxy far, far away",
]

results = generator.text_completion(
    prompts,
    max_gen_len=64,
    temperature=0.6,
)

for prompt, result in zip(prompts, results):
    print(f"{prompt} {result['generation']}")
```

## Interactive CLI Pattern

```python
conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ['quit', 'exit']:
        break
    
    conversation.append({"role": "user", "content": user_input})
    
    results = generator.chat_completion([conversation], max_gen_len=512)
    response = results[0]['generation']['content']
    
    conversation.append({"role": "assistant", "content": response})
    print(f"Bot: {response}\n")
```

## Error Handling

```python
try:
    results = generator.chat_completion(dialogs)
    response = results[0]['generation']['content']
except Exception as e:
    print(f"Error: {e}")
    response = "Sorry, I encountered an error."
```

## File I/O

```python
import json

# Save conversation
with open('conversation.json', 'w') as f:
    json.dump(conversation, f, indent=2)

# Load conversation
with open('conversation.json', 'r') as f:
    conversation = json.load(f)
```

## Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"User: {user_input}")
logger.info(f"Assistant: {response}")
```

## Common Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ckpt_dir` | str | Required | Path to model checkpoint |
| `tokenizer_path` | str | Required | Path to tokenizer |
| `max_seq_len` | int | 512 | Max sequence length (≤8192) |
| `max_batch_size` | int | 4 | Max batch size |
| `max_gen_len` | int | None | Max generation length |
| `temperature` | float | 0.6 | Sampling temperature (0.0-1.0) |
| `top_p` | float | 0.9 | Top-p sampling (0.0-1.0) |

## Model Files Required

```
Meta-Llama-3-8B-Instruct/
├── consolidated.00.pth    # Model weights
├── params.json            # Model config
└── tokenizer.model        # Tokenizer
```

## Command Line Usage

```bash
# Basic
torchrun --nproc_per_node 1 script.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model

# With custom parameters
torchrun --nproc_per_node 1 script.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --max_seq_len 1024 \
    --max_batch_size 2 \
    --temperature 0.8
```

## Performance Tips

```python
# For faster inference
max_seq_len = 512          # Lower = faster
max_batch_size = 1         # Process one at a time
max_gen_len = 256          # Limit response length

# For better quality
max_seq_len = 2048         # More context
temperature = 0.3          # More focused
top_p = 0.9                # Standard diversity

# For creativity
temperature = 0.9          # More random
top_p = 0.95               # More diverse
```

## Quick Debugging

```python
import torch

# Check GPU
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Device count: {torch.cuda.device_count()}")

# Check model loading
print(f"Model loaded: {generator.model is not None}")
print(f"Tokenizer vocab size: {generator.tokenizer.n_words}")
```

## Resources

- Full tutorial: [TUTORIAL.md](TUTORIAL.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- Quick start: [QUICKSTART.md](QUICKSTART.md)
