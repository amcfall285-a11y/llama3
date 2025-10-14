# How to Launch Your Llama 3 App

This guide will help you launch your Llama 3 application quickly and easily.

> **💡 Quick Answer:** The easiest way to launch an app is: `./launch_app.sh`
> 
> See our [FAQ](FAQ.md) for more common questions!

## Quick Launch (Recommended)

We've created a simple launcher script that handles everything for you:

```bash
./launch_app.sh
```

The launcher will:
- ✅ Check your Python installation
- ✅ Install dependencies if needed
- ✅ Guide you through choosing an app
- ✅ Help configure model paths
- ✅ Launch the app with proper settings

## Manual Launch Methods

### Option 1: Story Generator

Generate creative stories on any topic:

```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "a robot learning to paint"
```

### Option 2: Interactive Chatbot

Chat with the AI interactively:

```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### Option 3: Chat Completion Examples

Run predefined conversation examples:

```bash
torchrun --nproc_per_node 1 example_chat_completion.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --max_seq_len 512 \
    --max_batch_size 6
```

### Option 4: Text Completion Examples

Complete text prompts:

```bash
torchrun --nproc_per_node 1 example_text_completion.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --max_seq_len 128 \
    --max_batch_size 4
```

## Prerequisites

Before launching, ensure you have:

1. **Python 3.8+** installed
2. **Dependencies installed**: Run `pip install -e .`
3. **Model downloaded**: 
   - Visit https://llama.meta.com/llama-downloads/
   - Register and get download URL
   - Run `./download.sh` and follow prompts

## Troubleshooting

### "Model directory not found"
- Make sure you've downloaded the model using `./download.sh`
- Check that the model path matches your downloaded model directory

### "Module 'llama' not found"
- Run `pip install -e .` to install dependencies

### "Out of memory"
- Reduce `max_seq_len` to 128
- Reduce `max_batch_size` to 1
- Close other applications

### "No GPU detected"
- The app will use CPU automatically (slower)
- For better performance, use a CUDA-capable GPU

## Command Line Arguments

All apps support these common arguments:

- `--ckpt_dir`: Path to model checkpoint directory
- `--tokenizer_path`: Path to tokenizer model file
- `--max_seq_len`: Maximum sequence length (default: varies by app)
- `--max_batch_size`: Maximum batch size (default: varies by app)

Story Generator specific:
- `--topic`: The topic for the story (default: "a brave knight")

Interactive Chatbot specific:
- `--system_prompt`: System prompt to define chatbot personality

## Need More Help?

- 📖 Full Tutorial: [TUTORIAL.md](TUTORIAL.md)
- 🚀 Quick Start: [QUICKSTART.md](QUICKSTART.md)
- 📚 Main Documentation: [README.md](README.md)
- 💡 Examples: [EXAMPLES.md](EXAMPLES.md)

Happy coding! 🎉
