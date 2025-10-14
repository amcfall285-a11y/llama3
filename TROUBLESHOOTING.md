# Troubleshooting Guide

This guide helps you resolve common issues when launching Llama 3 apps.

## Quick Diagnosis

**Run the setup checker first:**
```bash
./check_setup.sh
```

This will identify most issues automatically and tell you how to fix them.

## Common Issues and Solutions

### 1. "Cannot launch the app" / "Nothing happens"

**Symptoms:** Running `./launch_app.sh` doesn't work or gives errors.

**Solutions:**

1. **Make the script executable:**
   ```bash
   chmod +x launch_app.sh
   chmod +x download.sh
   chmod +x check_setup.sh
   ```

2. **Check your setup:**
   ```bash
   ./check_setup.sh
   ```

3. **Install dependencies first:**
   ```bash
   pip install -e .
   ```

4. **Try the test mode (no model needed):**
   ```bash
   python3 test_installation.py
   ```

---

### 2. "Module 'llama' not found" or "ModuleNotFoundError"

**Symptoms:** Error message about missing modules.

**Solutions:**

1. **Install the package:**
   ```bash
   pip install -e .
   ```

2. **If pip fails, try with user flag:**
   ```bash
   pip install --user -e .
   ```

3. **Check Python version (need 3.8+):**
   ```bash
   python3 --version
   ```

4. **Verify installation:**
   ```bash
   python3 -c "import llama; print('Success!')"
   ```

---

### 3. "Model directory not found" / "No such file or directory"

**Symptoms:** Can't find model files or checkpoint directory.

**Solutions:**

1. **You need to download the model first:**
   ```bash
   ./download.sh
   ```

2. **Get download URL:**
   - Visit https://llama.meta.com/llama-downloads/
   - Register and accept the license
   - You'll receive an email with a download URL
   - Use that URL with `./download.sh`

3. **Choose the right model:**
   - When prompted, select: `8B-instruct` (recommended for beginners)
   - Or press Enter to download all models (takes longer)

4. **Verify download:**
   ```bash
   ls -la Meta-Llama-3-8B-Instruct/
   ```
   Should see: `tokenizer.model`, `params.json`, `consolidated.00.pth`

5. **If you can't download models yet:**
   - Use the test mode: `python3 test_installation.py`
   - This verifies your setup without needing model files

---

### 4. "Out of memory" / "CUDA out of memory"

**Symptoms:** App crashes with memory errors.

**Solutions:**

1. **Reduce sequence length:**
   ```bash
   torchrun --nproc_per_node 1 my_first_app.py \
       --ckpt_dir Meta-Llama-3-8B-Instruct/ \
       --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
       --max_seq_len 128 \
       --max_batch_size 1
   ```

2. **Close other applications** to free up RAM/VRAM

3. **Use CPU instead of GPU** (slower but uses system RAM):
   - PyTorch will automatically fall back to CPU if no GPU is available

4. **Use a smaller model** if you downloaded multiple versions

---

### 5. "torchrun: command not found"

**Symptoms:** Can't find torchrun command.

**Solutions:**

1. **Install PyTorch:**
   ```bash
   pip install -e .
   ```

2. **Verify PyTorch installation:**
   ```bash
   python3 -c "import torch; print(torch.__version__)"
   ```

3. **Check if torchrun is available:**
   ```bash
   which torchrun
   ```

4. **Alternative: Use python directly for some scripts:**
   ```bash
   python3 hemp_seed_app.py --ckpt_dir Meta-Llama-3-8B-Instruct/ --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
   ```

---

### 6. "Permission denied" when running scripts

**Symptoms:** Can't execute .sh scripts.

**Solutions:**

1. **Make scripts executable:**
   ```bash
   chmod +x launch_app.sh
   chmod +x download.sh
   chmod +x check_setup.sh
   ```

2. **Or run with bash explicitly:**
   ```bash
   bash launch_app.sh
   ```

---

### 7. "wget: command not found"

**Symptoms:** download.sh fails because wget is missing.

**Solutions:**

1. **Install wget:**
   - **Ubuntu/Debian:** `sudo apt-get install wget`
   - **macOS:** `brew install wget`
   - **Windows:** Use WSL or download from https://eternallybored.org/misc/wget/

2. **Alternative: Use curl:**
   - Modify download.sh to use curl instead
   - Or download from Hugging Face (see README.md)

---

### 8. Scripts require interaction / "How do I run this automatically?"

**Symptoms:** Scripts ask for input and you want to automate them.

**Solutions:**

1. **Use the test mode:**
   ```bash
   python3 test_installation.py
   ```

2. **For automated setups, install dependencies directly:**
   ```bash
   pip install -e .
   ```

3. **Set environment variables for model paths:**
   ```bash
   export CKPT_DIR="Meta-Llama-3-8B-Instruct/"
   export TOKENIZER_PATH="Meta-Llama-3-8B-Instruct/tokenizer.model"
   ```

4. **Run apps directly:**
   ```bash
   torchrun --nproc_per_node 1 my_first_app.py \
       --ckpt_dir "$CKPT_DIR" \
       --tokenizer_path "$TOKENIZER_PATH" \
       --topic "test topic"
   ```

---

### 9. "It's too slow" / Performance issues

**Symptoms:** App runs but takes a very long time.

**Solutions:**

1. **Check if GPU is being used:**
   ```bash
   python3 -c "import torch; print('CUDA available:', torch.cuda.is_available())"
   ```

2. **If no GPU:**
   - Responses will be slower on CPU
   - Consider using cloud GPU services (AWS, Google Cloud, etc.)
   - Or rent GPU time from services like Colab, RunPod, etc.

3. **Reduce parameters for faster inference:**
   ```bash
   --max_seq_len 256 --max_batch_size 1
   ```

4. **Use shorter prompts** to reduce processing time

---

### 10. "I don't have a GPU" / "No CUDA device"

**Symptoms:** Warning about missing GPU.

**Solutions:**

1. **It's okay!** The app will run on CPU (just slower)

2. **Optimize for CPU:**
   - Use smaller max_seq_len (128-256)
   - Set max_batch_size to 1
   - Be patient with generation times

3. **Alternative: Use cloud GPU:**
   - Google Colab (free tier available)
   - AWS, Azure, Google Cloud
   - Paperspace, RunPod, Lambda Labs

---

## Step-by-Step Launch Process

If nothing works, follow this from scratch:

```bash
# 1. Verify Python version
python3 --version  # Should be 3.8 or higher

# 2. Install dependencies
pip install -e .

# 3. Test installation (no model needed)
python3 test_installation.py

# 4. Check setup
./check_setup.sh

# 5. Download models (if needed)
./download.sh

# 6. Launch an app
./launch_app.sh
```

---

## Still Having Issues?

### Check These Resources:

1. **Run the setup checker:**
   ```bash
   ./check_setup.sh
   ```

2. **Read the guides:**
   - [LAUNCH.md](LAUNCH.md) - Launch instructions
   - [QUICKSTART.md](QUICKSTART.md) - Quick start
   - [GETTING_STARTED.md](GETTING_STARTED.md) - Full guide

3. **Try the test installation:**
   ```bash
   python3 test_installation.py
   ```

4. **Get help:**
   - GitHub Issues: https://github.com/meta-llama/llama3/issues
   - Check existing issues for similar problems
   - Create a new issue with:
     - Your Python version
     - Your operating system
     - Error messages (full output)
     - What you've already tried

---

## Quick Command Reference

```bash
# Check setup
./check_setup.sh

# Install dependencies
pip install -e .

# Test without model
python3 test_installation.py

# Download models
./download.sh

# Launch app (interactive)
./launch_app.sh

# Launch app directly
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "your topic"
```

---

## Need More Help?

- 📖 [Full Documentation](README.md)
- 🚀 [Quick Start Guide](QUICKSTART.md)
- 💡 [Tutorial](TUTORIAL.md)
- 🔧 [Code Cheatsheet](CHEATSHEET.md)
