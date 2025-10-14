# 🚀 Quick Launch Help - Get Started in 3 Steps!

Welcome! This guide will help you launch your Llama 3 app quickly and easily.

## The Easiest Way to Launch 🎯

**Just run this command:**

```bash
./launch_app.sh
```

That's it! The script will:
- ✅ Check your Python installation
- ✅ Install dependencies automatically if needed
- ✅ Show you a menu of apps to choose from
- ✅ Help you configure model paths
- ✅ Launch your chosen app

## Step-by-Step First Time Setup

### Step 1: Install Dependencies (One-time setup)

```bash
pip install -e .
```

This installs all the required packages including PyTorch, fairscale, and Flask.

### Step 2: Download the Model (One-time setup)

You need to download the Llama 3 model:

1. Visit [https://llama.meta.com/llama-downloads/](https://llama.meta.com/llama-downloads/)
2. Register and accept the license
3. You'll receive an email with a download URL
4. Run the download script:

```bash
./download.sh
```

5. Enter the URL from your email when prompted
6. Choose to download **Meta-Llama-3-8B-Instruct** (recommended for getting started)

### Step 3: Launch an App

Once setup is complete, choose one of these methods:

#### Option A: Use the Launcher (Easiest!)

```bash
./launch_app.sh
```

Then follow the interactive prompts to:
1. Choose which app to run (Story Generator, Chatbot, etc.)
2. Confirm or customize model paths
3. Let the script launch the app for you!

#### Option B: Launch Directly

**Story Generator:**
```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "your topic here"
```

**Interactive Chatbot:**
```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

**Hemp Seed Web App:**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --port 5000
```

Then open your browser to: http://127.0.0.1:5000

## Available Apps

1. **Story Generator** (`my_first_app.py`) - Generate creative stories on any topic
2. **Interactive Chatbot** (`interactive_chatbot.py`) - Chat with AI in real-time
3. **Chat Completion Example** (`example_chat_completion.py`) - See predefined conversations
4. **Text Completion Example** (`example_text_completion.py`) - Complete text prompts
5. **Hemp Seed Web App** (`hemp_seed_app.py`) - Full web application with AI assistant

## Common Issues & Solutions 🔧

### "Command not found: ./launch_app.sh"

Make sure the script is executable:
```bash
chmod +x launch_app.sh
./launch_app.sh
```

### "Module 'llama' not found"

Install dependencies:
```bash
pip install -e .
```

### "Model directory not found"

You need to download the model first:
```bash
./download.sh
```

Follow the instructions in Step 2 above.

### "Out of memory"

Your system doesn't have enough RAM/VRAM. Try:
- Close other applications
- Use smaller sequence length: `--max_seq_len 128`
- Use smaller batch size: `--max_batch_size 1`

### "No GPU detected"

This is OK! The app will run on CPU (it will be slower). For better performance:
- Use a system with a CUDA-capable GPU
- Make sure PyTorch with CUDA support is installed

### "Port already in use" (for web apps)

Choose a different port:
```bash
python hemp_seed_app.py ... --port 5001
```

### "torchrun: command not found"

Install PyTorch:
```bash
pip install torch
```

## Need More Help? 📚

- **Full Tutorial**: [TUTORIAL.md](TUTORIAL.md) - Comprehensive step-by-step guide
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md) - Get running in 5 minutes
- **Launch Guide**: [LAUNCH.md](LAUNCH.md) - Detailed launcher documentation
- **Main README**: [README.md](README.md) - Complete project documentation
- **Examples**: [EXAMPLES.md](EXAMPLES.md) - All example applications
- **Hemp Seed App**: [HEMP_SEED_QUICKSTART.md](HEMP_SEED_QUICKSTART.md) - Web app guide

## Quick Reference Commands

```bash
# Check Python version
python3 --version

# Install dependencies
pip install -e .

# Download model
./download.sh

# Launch with menu
./launch_app.sh

# Check if model exists
ls -la Meta-Llama-3-8B-Instruct/

# Test Python import
python3 -c "import llama; print('Success!')"
```

## System Requirements

**Minimum:**
- Python 3.8+
- 16GB RAM
- CPU (will work, but slow)

**Recommended:**
- Python 3.10+
- 32GB+ RAM
- CUDA-capable GPU with 8GB+ VRAM
- 50GB+ free disk space

---

**Still stuck?** File an issue at: https://github.com/meta-llama/llama3/issues

**Ready to build?** Start with `./launch_app.sh` and have fun! 🎉
