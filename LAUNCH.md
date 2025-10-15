# How to Launch Your Llama 3 App

This guide will help you launch your Llama 3 application quickly and easily.

## Quick Launch (Recommended)

### Option A: Using the Launcher Script

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

### Option B: Using VS Code (Easiest for Development)

If you're using Visual Studio Code, we've included pre-configured launch configurations:

1. Open the project in VS Code
2. Press `F5` or go to **Run > Start Debugging**
3. Select from the dropdown:
   - **Story Generator** - Generate creative stories
   - **Interactive Chatbot** - Chat with the AI
   - **Chat Completion Example** - Run predefined examples
   - **Text Completion Example** - Complete text prompts
   - **Hemp Seed Web App** - Launch the web application

The configurations are in `.vscode/launch.json` and can be customized to match your model paths.

**Note:** Make sure you have the Python extension installed in VS Code for debugging support.

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
- If using VS Code, update the paths in `.vscode/launch.json` to match your setup

### "Module 'llama' not found"
- Run `pip install -e .` to install dependencies

### "Out of memory"
- Reduce `max_seq_len` to 128
- Reduce `max_batch_size` to 1
- Close other applications

### "No GPU detected"
- The app will use CPU automatically (slower)
- For better performance, use a CUDA-capable GPU

### VS Code debugging not working
- Ensure the Python extension is installed in VS Code
- Install `debugpy`: `pip install debugpy`
- Check that model paths in `.vscode/launch.json` match your setup
- For the Hemp Seed app, no `torchrun` is needed (runs directly with Python)

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
