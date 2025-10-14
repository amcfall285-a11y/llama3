# Quick Start Guide: Build Your First Llama 3 App in 5 Minutes

This is a condensed guide to get you up and running with Llama 3 as quickly as possible.

## Prerequisites

- Python 3.8+
- CUDA-capable GPU (recommended)
- 16GB+ RAM

## Installation (2 minutes)

```bash
# 1. Clone and install
git clone https://github.com/meta-llama/llama3.git
cd llama3
pip install -e .

# 2. Download model (requires registration at https://llama.meta.com/llama-downloads/)
chmod +x download.sh
./download.sh
# Follow prompts to download Meta-Llama-3-8B-Instruct
```

## Your First App (3 minutes)

### Option 1: Run the Story Generator

```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "a robot learning to paint"
```

### Option 2: Run the Interactive Chatbot

```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

## Basic Code Template

```python
from llama import Llama

# Load model
generator = Llama.build(
    ckpt_dir="Meta-Llama-3-8B-Instruct/",
    tokenizer_path="Meta-Llama-3-8B-Instruct/tokenizer.model",
    max_seq_len=512,
    max_batch_size=1,
)

# Create a conversation
dialogs = [[{"role": "user", "content": "Tell me a joke"}]]

# Generate response
results = generator.chat_completion(
    dialogs,
    max_gen_len=256,
    temperature=0.7,
)

print(results[0]['generation']['content'])
```

## Next Steps

1. Read the full [TUTORIAL.md](TUTORIAL.md) for detailed explanations
2. Try the provided examples: `example_chat_completion.py` and `example_text_completion.py`
3. Customize the example apps to suit your needs
4. Build your own application!

## Common Issues

**Out of Memory?** Reduce `max_seq_len` to 128 or use CPU (slower)

**No GPU?** PyTorch will automatically use CPU, but it's slower

**Model not found?** Check the paths match your downloaded model directory

## Resources

- Full Tutorial: [TUTORIAL.md](TUTORIAL.md)
- Examples: `example_chat_completion.py`, `my_first_app.py`, `interactive_chatbot.py`
- Documentation: [README.md](README.md)

Happy coding! 🚀
