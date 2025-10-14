# Llama 3 Launch Options - Quick Reference

This guide shows all the ways you can launch Llama 3 apps, from easiest to most advanced.

## 🎯 Choose Your Launch Method

```
┌─────────────────────────────────────────────────────────────┐
│                    ABSOLUTE BEGINNER                         │
│  Just want it to work? Start here!                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ./quick_launch.sh
                              │
                    Handles everything for you!
                    (setup, testing, launching)


┌─────────────────────────────────────────────────────────────┐
│                    NEED TO DEBUG?                            │
│  Having issues? Use these diagnostic tools                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                     ./check_setup.sh
                              │
                    Checks your setup and
                    identifies problems
                              │
                              ▼
                python3 test_installation.py
                              │
                    Tests setup WITHOUT
                    needing model files


┌─────────────────────────────────────────────────────────────┐
│                    INTERACTIVE LAUNCHER                      │
│  Want to choose which app to run?                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ./launch_app.sh
                              │
                    Menu-driven launcher
                    Choose app, configure paths


┌─────────────────────────────────────────────────────────────┐
│                    MANUAL LAUNCH                             │
│  For developers who want full control                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        torchrun --nproc_per_node 1 my_first_app.py \
            --ckpt_dir Meta-Llama-3-8B-Instruct/ \
            --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
            --topic "your topic"
```

---

## 📋 Quick Command Reference

### For Absolute Beginners
```bash
# One command to rule them all
./quick_launch.sh
```

### Having Trouble?
```bash
# Check what's wrong with your setup
./check_setup.sh

# Test installation without model files
python3 test_installation.py

# Read troubleshooting guide
cat TROUBLESHOOTING.md
```

### Want to Choose an App?
```bash
# Interactive launcher with menu
./launch_app.sh
```

### Manual Control
```bash
# Story generator
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "a space explorer"

# Interactive chatbot
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model

# Web app (The Hemp Seed)
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --port 5000
```

---

## 🔧 Setup Commands

### First Time Setup
```bash
# Install dependencies
pip install -e .

# Download models (requires registration)
./download.sh
```

### Verification
```bash
# Check if everything is installed
./check_setup.sh

# Test installation (no model needed)
python3 test_installation.py

# Check Python version
python3 --version

# Check if packages are installed
python3 -c "import torch; print('PyTorch:', torch.__version__)"
python3 -c "import llama; print('Llama package installed!')"
```

---

## 🎓 Learning Path

### 1. Complete Beginner
```bash
# Step 1: Run quick launch
./quick_launch.sh

# Step 2: Follow the prompts
# The script will guide you through everything

# Step 3: Once models are downloaded, launch an app
./quick_launch.sh
# Choose option 1, 2, or 3
```

### 2. Some Experience
```bash
# Step 1: Check your setup
./check_setup.sh

# Step 2: Install if needed
pip install -e .

# Step 3: Download models
./download.sh

# Step 4: Use the interactive launcher
./launch_app.sh
```

### 3. Developer
```bash
# Install
pip install -e .

# Verify
python3 -c "import llama; import torch; print('Ready!')"

# Launch manually
torchrun --nproc_per_node 1 example_chat_completion.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

---

## 🆘 Troubleshooting Quick Reference

### Problem: "Can't launch the app"
```bash
# Solution: Run the setup checker
./check_setup.sh
```

### Problem: "Dependencies not installed"
```bash
# Solution: Install them
pip install -e .
```

### Problem: "Model files not found"
```bash
# Solution: Download models
./download.sh
# Need URL from: https://llama.meta.com/llama-downloads/
```

### Problem: "Want to test without model files"
```bash
# Solution: Run the test
python3 test_installation.py
```

### Problem: "Don't know what's wrong"
```bash
# Solution: Read the troubleshooting guide
cat TROUBLESHOOTING.md
# Or view in browser/editor: TROUBLESHOOTING.md
```

---

## 📚 Documentation Quick Links

- **Complete Beginner?** → [GETTING_STARTED.md](GETTING_STARTED.md)
- **Want Quick Setup?** → [QUICKSTART.md](QUICKSTART.md)
- **Launch Issues?** → [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Detailed Guide?** → [TUTORIAL.md](TUTORIAL.md)
- **Launch Help?** → [LAUNCH.md](LAUNCH.md)
- **Code Examples?** → [CHEATSHEET.md](CHEATSHEET.md)

---

## ✅ Success Checklist

Before trying to launch, make sure you have:

- [ ] Python 3.8 or higher installed
- [ ] Dependencies installed (`pip install -e .`)
- [ ] Model files downloaded (via `./download.sh`)
- [ ] Verified setup (`./check_setup.sh` passes)

Once all are checked, you can:
- Run `./quick_launch.sh` for guided experience
- Run `./launch_app.sh` for interactive menu
- Run apps manually with `torchrun`

---

## 🎉 Quick Win

Want to see if everything works RIGHT NOW?

```bash
# This tests your setup without needing model files!
python3 test_installation.py
```

Green checkmarks = you're good to go! 🚀

Red X's = run `./check_setup.sh` to see what needs fixing.

---

**Remember:** When in doubt, run `./quick_launch.sh` - it handles everything! 🎯
