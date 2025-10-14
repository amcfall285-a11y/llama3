# 🚀 Llama 3 Quick Reference Card

**Keep this handy!** One-page reference for launching Llama 3 apps.

---

## 🎯 Three Ways to Launch

### 1️⃣ Easiest (Recommended for Everyone)
```bash
./quick_launch.sh
```
Handles EVERYTHING automatically!

### 2️⃣ Interactive Menu
```bash
./launch_app.sh
```
Choose which app to run from a menu.

### 3️⃣ Manual Command
```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "your topic"
```

---

## 🆘 Having Issues?

### Check Setup
```bash
./check_setup.sh
```

### Test Installation (No Model Needed!)
```bash
python3 test_installation.py
```

### Read Troubleshooting
```bash
cat TROUBLESHOOTING.md
```

---

## 📦 First Time Setup

```bash
# 1. Install dependencies
pip install -e .

# 2. Download models (requires registration)
./download.sh

# 3. Launch!
./quick_launch.sh
```

Get download URL from: https://llama.meta.com/llama-downloads/

---

## ✅ Prerequisites

- [ ] Python 3.8+
- [ ] Dependencies installed
- [ ] Model files downloaded
- [ ] Setup verified

---

## 🔧 Common Commands

```bash
# Check Python version
python3 --version

# Install dependencies
pip install -e .

# Verify installation
python3 -c "import llama; print('OK!')"

# Check GPU
python3 -c "import torch; print('CUDA:', torch.cuda.is_available())"

# Run setup check
./check_setup.sh

# Test without models
python3 test_installation.py
```

---

## 📱 Example Apps

**Story Generator:**
```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "space adventure"
```

**Interactive Chatbot:**
```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

**Web App:**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --port 5000
```

---

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| Can't launch | `./check_setup.sh` |
| Module not found | `pip install -e .` |
| Model not found | `./download.sh` |
| Out of memory | Add `--max_seq_len 128` |
| Permission denied | `chmod +x *.sh` |

---

## 📚 Documentation

- **Quick Start:** `QUICKSTART.md`
- **Tutorial:** `TUTORIAL.md`
- **Troubleshooting:** `TROUBLESHOOTING.md`
- **Launch Guide:** `LAUNCH.md`
- **All Options:** `LAUNCH_OPTIONS.md`

---

## 💡 Pro Tips

1. **Test first:** Run `python3 test_installation.py` before downloading models
2. **Save time:** Use `./quick_launch.sh` - it's the easiest!
3. **Stuck?** Read `TROUBLESHOOTING.md` - most issues are covered
4. **No GPU?** That's OK! It'll use CPU (just slower)

---

## 🎓 Learning Path

1. Run `./quick_launch.sh`
2. Try the story generator
3. Try the chatbot
4. Read `TUTORIAL.md`
5. Build your own app!

---

## 🌟 Remember

**When in doubt:**
```bash
./quick_launch.sh
```

**This ONE command handles everything!** 🚀

---

_For detailed help, see TROUBLESHOOTING.md or visit https://github.com/meta-llama/llama3_
