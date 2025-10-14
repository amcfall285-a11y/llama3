#!/usr/bin/env bash
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

###
# Literally Launch Your Llama 3 App 🚀
# 
# This is the MOST LITERAL way to launch your app.
# No questions. No configuration. Just launch.
###

set -e

echo "🚀🚀🚀 LITERALLY LAUNCHING YOUR APP 🚀🚀🚀"
echo ""
echo "This is launching in the most literal way possible:"
echo "  ✓ No questions asked"
echo "  ✓ No configuration needed"
echo "  ✓ Just... LAUNCH! 🚀"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Install Python 3.8+ first."
    exit 1
fi

# Auto-install dependencies if needed
if ! python3 -c "import llama" 2>/dev/null; then
    echo "📦 Installing dependencies (one time only)..."
    pip install -e . > /dev/null 2>&1 || {
        echo "❌ Failed to install. Run: pip install -e ."
        exit 1
    }
    echo "✅ Dependencies installed!"
fi

# Use default paths
CKPT_DIR="Meta-Llama-3-8B-Instruct/"
TOKENIZER_PATH="Meta-Llama-3-8B-Instruct/tokenizer.model"

# Check if model exists
if [ ! -d "$CKPT_DIR" ]; then
    echo ""
    echo "⚠️  Model not found at $CKPT_DIR"
    echo ""
    echo "To download the model:"
    echo "  1. Visit: https://llama.meta.com/llama-downloads/"
    echo "  2. Run: ./download.sh"
    echo ""
    echo "For now, launching anyway (will fail if model truly missing)..."
    echo ""
fi

echo "🎯 Launching Story Generator with default settings..."
echo "   Topic: 'a brave knight'"
echo "   Model: $CKPT_DIR"
echo ""
echo "▶▶▶ LAUNCHING NOW! ▶▶▶"
echo ""

# LITERALLY JUST LAUNCH IT
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir "$CKPT_DIR" \
    --tokenizer_path "$TOKENIZER_PATH" \
    --topic "a brave knight"
