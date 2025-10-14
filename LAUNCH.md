# How to Launch Your Llama 3 App

This guide will help you launch your Llama 3 application quickly and easily.

## Quick Launch (Recommended)

We've created a simple launcher script that handles everything for you:

```bash
./launch_app.sh
```

The launcher will:
- ✅ Check your Python installation
- ✅ Install dependencies if needed
- ✅ Verify torch and torchrun are available
- ✅ Guide you through choosing an app
- ✅ Help configure model paths
- ✅ Launch the app with proper settings
- ✅ Provide helpful error messages if something goes wrong

**First time setup:**
```bash
# Make the script executable
chmod +x launch_app.sh

# Run the launcher
./launch_app.sh
```

The launcher will automatically install dependencies on first run. Just follow the prompts!

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

**Quick Setup Check:**

Before trying to launch, verify your setup is correct:

```bash
python3 verify_setup.py
```

This will check all dependencies and model files, and tell you exactly what needs to be fixed.

## Troubleshooting

### "bash: ./launch_app.sh: Permission denied"
Make the script executable first:
```bash
chmod +x launch_app.sh
./launch_app.sh
```

### "Module 'llama' not found"
The launcher should install this automatically, but if it fails:
```bash
pip install -e .
# Or with user flag if permission denied:
pip install -e . --user
```

### "No module named 'torch'" or "torchrun: command not found"
Install PyTorch:
```bash
pip install torch
# Verify installation:
python3 -c "import torch; print(torch.__version__)"
```

### "Model directory not found"
You need to download the Llama 3 model:
1. Visit https://llama.meta.com/llama-downloads/
2. Register and get download URL
3. Run `./download.sh` and follow prompts
4. Choose "8B-instruct" when prompted

### "Out of memory"
- Reduce `max_seq_len` to 128
- Reduce `max_batch_size` to 1
- Close other applications
- Consider using a smaller model

### "No GPU detected"
- The app will use CPU automatically (slower)
- For better performance, use a CUDA-capable GPU
- Ensure CUDA drivers are installed for GPU usage

### "CUDA error" or GPU issues
If you have a GPU but it's not working:
```bash
# Check if CUDA is available
python3 -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```
If CUDA is not available, PyTorch will fall back to CPU.

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
