# Frequently Asked Questions (FAQ)

## Quick Answers

### What is the easiest way to launch an app?

**The easiest way to launch an app is using the launcher script:**

```bash
./launch_app.sh
```

This interactive script:
- ✅ Checks your Python installation automatically
- ✅ Installs dependencies if needed
- ✅ Guides you through choosing which app to run
- ✅ Helps you configure model paths
- ✅ Launches the app with proper settings

**That's it!** Just run `./launch_app.sh` and follow the prompts.

### How can I literally launch my app? 🚀

**Want to launch in the MOST LITERAL way with zero configuration?**

```bash
./literally_launch.sh
```

This script:
- 🚀 Launches immediately - no questions asked
- 🎯 Uses sensible defaults automatically
- ⚡ Perfect for quick demos or "just make it work" moments

See [LAUNCH.md](LAUNCH.md) for more details about both launchers.

---

## Installation & Setup

### Do I need to download the model first?

Yes, you need to download the Llama 3 model before running any apps:

1. Visit https://llama.meta.com/llama-downloads/
2. Register and get download URL
3. Run `./download.sh` and follow prompts
4. Choose Meta-Llama-3-8B-Instruct (recommended for beginners)

### What are the minimum system requirements?

- **Python:** 3.8 or higher
- **RAM:** 16GB+ (for 8B model)
- **GPU:** CUDA-capable GPU recommended (will use CPU if not available)
- **Storage:** ~20GB for the 8B model

### How do I install dependencies?

```bash
pip install -e .
```

Run this command from the repository root directory.

---

## Launching Apps

### What apps are available?

The repository includes 5 example applications:

1. **Story Generator** (`my_first_app.py`) - Generates creative stories
2. **Interactive Chatbot** (`interactive_chatbot.py`) - Multi-turn conversations
3. **Chat Completion Example** (`example_chat_completion.py`) - Official examples
4. **Text Completion Example** (`example_text_completion.py`) - Text generation
5. **The Hemp Seed Web App** (`hemp_seed_app.py`) - Business web application

### Can I launch apps manually without the launcher script?

Yes! You can launch apps manually using `torchrun`:

```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

See [LAUNCH.md](LAUNCH.md) for manual launch commands for each app.

### Which app should I try first?

For beginners, we recommend:

1. **First choice:** Story Generator (`my_first_app.py`) - Simple and fast
2. **Second choice:** Interactive Chatbot (`interactive_chatbot.py`) - More interactive

Both are easy to understand and demonstrate core Llama 3 capabilities.

---

## Troubleshooting

### "Model directory not found"

This means you haven't downloaded the model yet. Run `./download.sh` to download it.

### "Module 'llama' not found"

Install dependencies with: `pip install -e .`

### "Out of memory" error

Try these solutions:
- Reduce `max_seq_len` to 128 or 256
- Reduce `max_batch_size` to 1
- Close other applications
- Use a machine with more RAM

### The app is very slow

- **Check GPU usage:** Make sure you have a CUDA-capable GPU
- **CPU mode is slower:** If no GPU is detected, the app will use CPU automatically
- **Reduce parameters:** Lower `max_seq_len` for faster inference

### How do I stop a running app?

Press `Ctrl+C` to stop most apps. For the interactive chatbot, you can also type `quit`.

---

## Advanced Usage

### Can I change the model parameters?

Yes! All apps support command-line arguments:

```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --max_seq_len 1024 \
    --max_batch_size 2
```

See [LAUNCH.md](LAUNCH.md#command-line-arguments) for all available parameters.

### How do I use a different model?

Change the `--ckpt_dir` and `--tokenizer_path` parameters to point to your model:

```bash
--ckpt_dir Meta-Llama-3-70B-Instruct/ \
--tokenizer_path Meta-Llama-3-70B-Instruct/tokenizer.model
```

### Can I run multiple apps at the same time?

Yes, but be mindful of memory usage. Each app loads the model into memory.

---

## Getting Help

### Where can I find more documentation?

- **Quick Start:** [QUICKSTART.md](QUICKSTART.md) - 5-minute setup
- **Launch Guide:** [LAUNCH.md](LAUNCH.md) - How to launch apps
- **Full Tutorial:** [TUTORIAL.md](TUTORIAL.md) - Complete guide
- **Code Reference:** [CHEATSHEET.md](CHEATSHEET.md) - Quick code patterns
- **Examples:** [EXAMPLES.md](EXAMPLES.md) - Overview of all apps
- **Getting Started:** [GETTING_STARTED.md](GETTING_STARTED.md) - Navigation guide

### Where do I report bugs?

Report issues at: https://github.com/meta-llama/llama3/issues

### Where can I find more examples?

See the [Llama Cookbook](https://github.com/meta-llama/llama-recipes) for more advanced examples and recipes.

---

## Quick Command Reference

### Install everything and launch an app (recommended):
```bash
pip install -e .
./launch_app.sh
```

### Launch Story Generator:
```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### Launch Interactive Chatbot:
```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

---

**Still have questions?** Check out our comprehensive guides:
- [GETTING_STARTED.md](GETTING_STARTED.md) - Choose your learning path
- [TUTORIAL.md](TUTORIAL.md) - Step-by-step guide
- [LAUNCH.md](LAUNCH.md) - Detailed launch instructions
