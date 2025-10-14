# 🚀 HOW TO LAUNCH - Visual Guide

## The Fastest Way to Launch (3 Simple Steps)

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1: Run the Interactive Helper                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│    $ python3 launch_helper.py                           │
│                                                          │
│    ✅ It will check your setup                          │
│    ✅ It will tell you what's missing                   │
│    ✅ It can install dependencies for you              │
│    ✅ It will guide you through everything              │
│                                                          │
└─────────────────────────────────────────────────────────┘
           │
           │ (If dependencies are missing)
           ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 2: Install Dependencies (if needed)               │
├─────────────────────────────────────────────────────────┤
│                                                          │
│    $ pip install -e .                                   │
│                                                          │
│    This installs: torch, fairscale, fire, flask         │
│                                                          │
└─────────────────────────────────────────────────────────┘
           │
           │ (If model not downloaded)
           ▼
┌─────────────────────────────────────────────────────────┐
│  STEP 3: Download Model (if needed)                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│    1. Visit: https://llama.meta.com/llama-downloads/   │
│    2. Register and accept license                       │
│    3. Get download URL from email                       │
│    4. Run: ./download.sh                                │
│    5. Paste URL when prompted                           │
│                                                          │
└─────────────────────────────────────────────────────────┘
           │
           │ (Once setup is complete)
           ▼
┌─────────────────────────────────────────────────────────┐
│  🎉 LAUNCH YOUR APP!                                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│    $ ./launch_app.sh                                    │
│                                                          │
│    Choose from:                                         │
│    1. Story Generator                                   │
│    2. Interactive Chatbot                               │
│    3. Chat Completion Example                           │
│    4. Text Completion Example                           │
│    5. Hemp Seed Web App                                 │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Quick Command Reference

### First Time Setup (do once)
```bash
# Install dependencies
pip install -e .

# Download model
./download.sh
```

### Every Time You Want to Launch
```bash
# Option 1: Interactive helper (checks everything first)
python3 launch_helper.py

# Option 2: Direct launcher (faster if setup is done)
./launch_app.sh
```

---

## Example Launch Flow

### 📝 Scenario: First Time User

**You:** "I need help launching this app"

**Do this:**
```bash
python3 launch_helper.py
```

**What happens:**
```
🚀 Llama 3 Launch Helper
=====================
This tool will help you check your setup and launch Llama 3 apps.

System Check
============

✅ Python 3.12.3 detected
⚠️  torch is NOT installed
⚠️  llama package is NOT installed
⚠️  Model directory not found

Summary
=======

Some checks failed. Here's what you need to do:

2. Install dependencies:
   Run: pip install -e .
   
   Would you like me to install them now? (y/n): y
   
   [Installing...]
   
   ✅ Dependencies installed! Please run this script again.
```

**Then run it again:**
```bash
python3 launch_helper.py
```

**Now it says:**
```
✅ All checks passed! You're ready to launch! 🎉

Available Applications
======================

1. ✅ Story Generator (my_first_app.py)
   Generate creative stories on any topic

2. ✅ Interactive Chatbot (interactive_chatbot.py)
   Chat with AI in real-time

[more apps...]

Would you like to launch the app now? (y/n): y
```

**Success!** 🎉

---

## Troubleshooting Common Issues

### "python3: command not found"
**Problem:** Python is not installed  
**Solution:** Install Python 3.8+ from python.org

### "pip: command not found"
**Problem:** pip is not installed  
**Solution:** 
```bash
# Ubuntu/Debian
sudo apt install python3-pip

# Mac
brew install python
```

### "Permission denied: ./launch_app.sh"
**Problem:** Script is not executable  
**Solution:** 
```bash
chmod +x launch_app.sh
chmod +x download.sh
```

### "Model directory not found"
**Problem:** Model hasn't been downloaded  
**Solution:** Follow Step 3 in the visual guide above

### "Out of memory"
**Problem:** Not enough RAM/VRAM  
**Solution:** 
- Close other applications
- Use smaller parameters when launching
- Consider using a system with more resources

---

## Visual: What Each Launch Method Does

### Method 1: `python3 launch_helper.py`

```
┌─────────────────────────────────┐
│  launch_helper.py               │
├─────────────────────────────────┤
│  • Checks Python version        │
│  • Checks dependencies          │
│  • Checks llama package         │
│  • Checks model files           │
│  • Can auto-install deps        │
│  • Guides you step by step      │
│  • Then runs launch_app.sh      │
└─────────────────────────────────┘
```

**Best for:** First time users, troubleshooting

### Method 2: `./launch_app.sh`

```
┌─────────────────────────────────┐
│  launch_app.sh                  │
├─────────────────────────────────┤
│  • Shows app menu               │
│  • Gets model paths             │
│  • Runs selected app            │
└─────────────────────────────────┘
```

**Best for:** When setup is done, regular use

### Method 3: Direct Command

```
┌─────────────────────────────────┐
│  torchrun --nproc_per_node 1    │
│    my_first_app.py              │
│    --ckpt_dir ...               │
├─────────────────────────────────┤
│  • Runs app directly            │
│  • No checks or menus           │
│  • You provide all args         │
└─────────────────────────────────┘
```

**Best for:** Experienced users, automation

---

## Complete Example Session

Here's what a complete first-time launch looks like:

```bash
$ cd llama3
$ python3 launch_helper.py
🚀 Llama 3 Launch Helper
========================

System Check
============
✅ Python 3.12.3 detected
⚠️  Dependencies not installed

Install now? (y/n): y
[Installing...]
✅ Done! Run script again.

$ python3 launch_helper.py
System Check
============
✅ Python 3.12.3 detected
✅ All dependencies installed
⚠️  Model not found

Download instructions:
1. Visit https://llama.meta.com/llama-downloads/
2. Register and get URL
3. Run: ./download.sh

[After downloading model...]

$ python3 launch_helper.py
System Check
============
✅ Python 3.12.3 detected
✅ All dependencies installed
✅ Model found
✅ Ready to launch!

Launch now? (y/n): y

Choose an app:
1. Story Generator
2. Interactive Chatbot
...

Enter choice: 1

🚀 Launching Story Generator...
[App runs!]
```

---

## Summary: Choose Your Launch Method

| Method | Command | When to Use |
|--------|---------|-------------|
| **Interactive Helper** | `python3 launch_helper.py` | First time, troubleshooting |
| **Quick Launcher** | `./launch_app.sh` | Regular use, easy selection |
| **Direct Launch** | `torchrun ... my_first_app.py ...` | Automation, scripts |

---

## Need More Help?

📖 **Detailed Guides:**
- [LAUNCH_HELP.md](LAUNCH_HELP.md) - Complete launch guide
- [QUICKSTART.md](QUICKSTART.md) - 5-minute setup
- [TUTORIAL.md](TUTORIAL.md) - Full tutorial
- [README.md](README.md) - Main documentation

🆘 **Still Having Issues?**
- Check [LAUNCH_HELP.md](LAUNCH_HELP.md) troubleshooting section
- File an issue: https://github.com/meta-llama/llama3/issues

---

**Remember:** The easiest way is always:
```bash
python3 launch_helper.py
```

**Let it guide you! 🚀**
