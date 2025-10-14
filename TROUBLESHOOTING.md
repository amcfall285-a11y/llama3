# Troubleshooting Guide

This guide helps you resolve common issues when trying to launch Llama 3 applications.

## Quick Diagnostics

**Run this first to check your setup:**

```bash
python3 verify_setup.py
```

This will tell you exactly what's missing or misconfigured.

---

## Common Issues and Solutions

### 1. "I can't launch the app"

**Step 1: Check your setup**
```bash
python3 verify_setup.py
```

**Step 2: Install dependencies**
```bash
pip install -e .
```

**Step 3: Verify installation**
```bash
python3 -c "import llama; import torch; print('✅ Dependencies OK')"
```

**Step 4: Try launching**
```bash
./launch_app.sh
```

---

### 2. "Permission denied" when running scripts

**Solution:** Make scripts executable
```bash
chmod +x launch_app.sh
chmod +x download.sh
chmod +x verify_setup.py
```

---

### 3. "No module named 'torch'" or dependency errors

**Solution 1: Install all dependencies at once**
```bash
pip install -e .
```

**Solution 2: If you get permission errors**
```bash
pip install -e . --user
```

**Solution 3: Use a virtual environment (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

---

### 4. "Model directory not found"

You need to download the Llama 3 model files first.

**Steps:**
1. Visit https://llama.meta.com/llama-downloads/
2. Register and accept the license
3. You'll receive a download URL via email
4. Run the download script:
   ```bash
   chmod +x download.sh
   ./download.sh
   ```
5. Paste your download URL when prompted
6. Choose "8B-instruct" when asked which model

**Note:** Download is ~15GB and may take 10-30 minutes depending on your internet speed.

---

### 5. "torchrun: command not found"

**Check if torch is installed:**
```bash
python3 -c "import torch; print(torch.__version__)"
```

**If torch is not installed:**
```bash
pip install torch
```

**If torch is installed but torchrun not found:**

The torchrun command should be available after installing PyTorch. Try:
```bash
python3 -m torch.distributed.run --help
```

If that works, you can replace `torchrun` with `python3 -m torch.distributed.run` in commands.

---

### 6. "Out of memory" or "CUDA out of memory"

**Solution 1: Reduce memory usage**

Edit the launch command to use smaller parameters:
```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --max_seq_len 128 \
    --max_batch_size 1
```

**Solution 2: Close other applications**

Free up RAM/VRAM by closing unnecessary programs.

**Solution 3: Use CPU instead of GPU**

If you have limited VRAM, the app will automatically fall back to CPU (slower but uses regular RAM).

---

### 7. "No GPU detected" or CUDA errors

**Check CUDA availability:**
```bash
python3 -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

**If False:**
- The app will automatically use CPU (slower)
- This is normal if you don't have a NVIDIA GPU
- Everything will still work, just slower

**If you have a NVIDIA GPU but it's not detected:**
- Ensure CUDA drivers are installed
- Check if your PyTorch installation includes CUDA support
- You may need to reinstall PyTorch with CUDA: https://pytorch.org/get-started/locally/

---

### 8. "Import error" or "ModuleNotFoundError"

**For any missing module:**
```bash
pip install <module-name>
```

**For llama module:**
```bash
# Make sure you're in the llama3 directory
cd /path/to/llama3
pip install -e .
```

---

### 9. App starts but crashes immediately

**Check the error message carefully.** Common causes:

**Missing model files:**
```bash
ls Meta-Llama-3-8B-Instruct/
# Should show: consolidated.00.pth, params.json, tokenizer.model, etc.
```

**Corrupted download:**
```bash
cd Meta-Llama-3-8B-Instruct/
md5sum -c checklist.chk  # Verify file integrity
```

**If files are corrupted, re-download:**
```bash
./download.sh
```

---

### 10. Hemp Seed Web App won't start

**Check if port is already in use:**
```bash
# On Linux/Mac:
lsof -i :5000

# On Windows:
netstat -ano | findstr :5000
```

**Solution: Use a different port**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --port 5001
```

---

## Still Having Issues?

1. **Run full diagnostics:**
   ```bash
   python3 verify_setup.py
   ```

2. **Check your Python version:**
   ```bash
   python3 --version  # Should be 3.8 or higher
   ```

3. **Verify you're in the right directory:**
   ```bash
   pwd
   ls -la  # Should see launch_app.sh, setup.py, llama/ directory
   ```

4. **Check available disk space:**
   ```bash
   df -h .  # Need ~20GB for model files
   ```

5. **Review the full error message** - it usually contains clues about what went wrong

6. **Check the logs** - some apps create log files with more details

---

## Quick Reference Commands

```bash
# Verify setup
python3 verify_setup.py

# Install dependencies
pip install -e .

# Make scripts executable
chmod +x launch_app.sh download.sh

# Download model
./download.sh

# Launch an app
./launch_app.sh

# Or manually:
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "your topic here"
```

---

## Getting Help

- **LAUNCH.md** - General launch instructions
- **QUICKSTART.md** - Quick start guide
- **TUTORIAL.md** - Detailed tutorial
- **README.md** - Main documentation
- **verify_setup.py** - Automated setup verification

For more specific issues, check the error message carefully - it usually tells you exactly what's wrong!
