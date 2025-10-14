#!/usr/bin/env bash
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

###
# Pre-flight Check Script for Llama 3
# 
# This script verifies your environment is ready to launch Llama 3 apps.
# Run this before trying to launch apps to identify any issues.
###

set -e

echo "🔍 Llama 3 Setup Checker"
echo "========================"
echo ""

ISSUES_FOUND=0

# Check Python
echo "1. Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "   ✅ Python $PYTHON_VERSION detected"
    
    # Check if version is 3.8+
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
        echo "   ⚠️  Warning: Python 3.8+ recommended, you have $PYTHON_VERSION"
        ISSUES_FOUND=$((ISSUES_FOUND+1))
    fi
else
    echo "   ❌ Python 3 not found"
    echo "   → Install Python 3.8+ from https://www.python.org/"
    ISSUES_FOUND=$((ISSUES_FOUND+1))
fi

echo ""

# Check pip
echo "2. Checking pip installation..."
if command -v pip &> /dev/null || command -v pip3 &> /dev/null; then
    echo "   ✅ pip is installed"
else
    echo "   ❌ pip not found"
    echo "   → Install pip to manage Python packages"
    ISSUES_FOUND=$((ISSUES_FOUND+1))
fi

echo ""

# Check llama package
echo "3. Checking llama package installation..."
if python3 -c "import llama" 2>/dev/null; then
    echo "   ✅ llama package is installed"
else
    echo "   ❌ llama package not installed"
    echo "   → Run: pip install -e ."
    ISSUES_FOUND=$((ISSUES_FOUND+1))
fi

echo ""

# Check dependencies
echo "4. Checking dependencies..."
MISSING_DEPS=()

if ! python3 -c "import torch" 2>/dev/null; then
    MISSING_DEPS+=("torch")
fi

if ! python3 -c "import fairscale" 2>/dev/null; then
    MISSING_DEPS+=("fairscale")
fi

if ! python3 -c "import fire" 2>/dev/null; then
    MISSING_DEPS+=("fire")
fi

if ! python3 -c "import tiktoken" 2>/dev/null; then
    MISSING_DEPS+=("tiktoken")
fi

if [ ${#MISSING_DEPS[@]} -eq 0 ]; then
    echo "   ✅ All dependencies installed"
else
    echo "   ❌ Missing dependencies: ${MISSING_DEPS[*]}"
    echo "   → Run: pip install -e ."
    ISSUES_FOUND=$((ISSUES_FOUND+1))
fi

echo ""

# Check for torchrun
echo "5. Checking torchrun availability..."
if command -v torchrun &> /dev/null; then
    echo "   ✅ torchrun is available"
else
    echo "   ⚠️  torchrun not found (will be available after installing PyTorch)"
    if [ ${#MISSING_DEPS[@]} -eq 0 ]; then
        ISSUES_FOUND=$((ISSUES_FOUND+1))
    fi
fi

echo ""

# Check for model files
echo "6. Checking for model files..."
DEFAULT_MODEL_DIR="Meta-Llama-3-8B-Instruct"
if [ -d "$DEFAULT_MODEL_DIR" ]; then
    echo "   ✅ Default model directory found: $DEFAULT_MODEL_DIR"
    
    # Check for required files
    if [ -f "$DEFAULT_MODEL_DIR/tokenizer.model" ]; then
        echo "   ✅ Tokenizer found"
    else
        echo "   ⚠️  tokenizer.model not found in $DEFAULT_MODEL_DIR"
        ISSUES_FOUND=$((ISSUES_FOUND+1))
    fi
    
    if [ -f "$DEFAULT_MODEL_DIR/params.json" ]; then
        echo "   ✅ Model config found"
    else
        echo "   ⚠️  params.json not found in $DEFAULT_MODEL_DIR"
        ISSUES_FOUND=$((ISSUES_FOUND+1))
    fi
    
    if ls $DEFAULT_MODEL_DIR/consolidated.*.pth 1> /dev/null 2>&1; then
        echo "   ✅ Model weights found"
    else
        echo "   ⚠️  Model weights (consolidated.*.pth) not found in $DEFAULT_MODEL_DIR"
        ISSUES_FOUND=$((ISSUES_FOUND+1))
    fi
else
    echo "   ⚠️  Default model directory not found: $DEFAULT_MODEL_DIR"
    echo "   → Download models:"
    echo "     1. Visit https://llama.meta.com/llama-downloads/"
    echo "     2. Register and get the download URL"
    echo "     3. Run: ./download.sh"
    echo "     4. Choose '8B-instruct' when prompted"
    echo ""
    echo "   Note: You can still install dependencies and test the code,"
    echo "         but you'll need the model files to run inference."
    ISSUES_FOUND=$((ISSUES_FOUND+1))
fi

echo ""
echo "========================================"
echo ""

if [ $ISSUES_FOUND -eq 0 ]; then
    echo "🎉 SUCCESS! Your setup is complete."
    echo ""
    echo "You're ready to launch apps:"
    echo "  → Run: ./launch_app.sh"
    echo ""
    echo "Or manually:"
    echo "  → torchrun --nproc_per_node 1 my_first_app.py \\"
    echo "      --ckpt_dir Meta-Llama-3-8B-Instruct/ \\"
    echo "      --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \\"
    echo "      --topic \"your topic\""
else
    echo "⚠️  Found $ISSUES_FOUND issue(s) that need attention."
    echo ""
    echo "Next steps:"
    echo "  1. Fix the issues listed above"
    echo "  2. Run this script again to verify"
    echo "  3. Once all checks pass, run: ./launch_app.sh"
    echo ""
    echo "Quick fixes:"
    echo "  • Install dependencies: pip install -e ."
    echo "  • Download models: ./download.sh"
    echo ""
    echo "Need help? Check:"
    echo "  • LAUNCH.md - Launch guide"
    echo "  • QUICKSTART.md - Quick start guide"
    echo "  • TROUBLESHOOTING.md - Common issues"
fi

echo ""
exit 0
