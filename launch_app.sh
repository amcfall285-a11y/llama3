#!/usr/bin/env bash
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

###
# Launcher Script for Llama 3 Apps
# 
# This script helps you easily launch the Llama 3 applications.
# It checks for dependencies and provides clear instructions.
###

set -e

echo "🚀 Llama 3 App Launcher"
echo "======================="
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Python $PYTHON_VERSION detected"

# Check Python version is 3.8 or higher
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    echo "⚠️  Warning: Python 3.8+ is recommended. You have $PYTHON_VERSION"
fi

# Check if pip is available
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip is not installed"
    echo "Please install pip and try again"
    exit 1
fi

# Use pip3 if available, otherwise pip
PIP_CMD="pip3"
if ! command -v pip3 &> /dev/null; then
    PIP_CMD="pip"
fi

echo "✓ pip detected"
echo ""

# Check if package is installed
echo "🔍 Checking dependencies..."
if ! python3 -c "import llama" 2>/dev/null; then
    echo ""
    echo "📦 Installing llama3 package and dependencies..."
    echo "This may take a few minutes. Installing: torch, fairscale, fire, tiktoken, blobfile, flask"
    echo ""
    $PIP_CMD install -e . || {
        echo ""
        echo "❌ Failed to install dependencies"
        echo ""
        echo "Troubleshooting tips:"
        echo "1. Try running manually: pip install -e ."
        echo "2. If you get permission errors, try: pip install -e . --user"
        echo "3. Consider using a virtual environment:"
        echo "   python3 -m venv venv"
        echo "   source venv/bin/activate"
        echo "   pip install -e ."
        echo ""
        exit 1
    }
    echo ""
    echo "✅ Dependencies installed successfully!"
fi

# Verify torch installation
echo "✓ Checking torch installation..."
if ! python3 -c "import torch" 2>/dev/null; then
    echo "⚠️  Warning: torch is not properly installed"
    echo "Attempting to install torch..."
    $PIP_CMD install torch || {
        echo "❌ Failed to install torch. Please install manually:"
        echo "   pip install torch"
        exit 1
    }
fi

# Check for torchrun
if ! command -v torchrun &> /dev/null; then
    echo "⚠️  Warning: torchrun not found in PATH"
    echo "Checking if torch.distributed is available..."
    if ! python3 -c "import torch.distributed" 2>/dev/null; then
        echo "❌ torch.distributed not found. Please ensure torch is properly installed."
        exit 1
    fi
    echo "✓ torch.distributed available (torchrun should work)"
fi

echo "✅ All dependencies verified!"

echo ""
echo "💡 Tip: You can run 'python3 verify_setup.py' anytime to check your setup"
echo ""

echo ""
echo "Choose an app to launch:"
echo ""
echo "1. Story Generator (my_first_app.py)"
echo "   - Generates creative stories based on a topic"
echo ""
echo "2. Interactive Chatbot (interactive_chatbot.py)"
echo "   - Chat interactively with the AI"
echo ""
echo "3. Chat Completion Example (example_chat_completion.py)"
echo "   - Run predefined conversation examples"
echo ""
echo "4. Text Completion Example (example_text_completion.py)"
echo "   - Complete text prompts"
echo ""
echo "5. The Hemp Seed Web App (hemp_seed_app.py)"
echo "   - AI-powered web app for The Hemp Seed business"
echo ""

read -p "Enter your choice (1-5): " choice

# Default model paths - user can override
DEFAULT_CKPT_DIR="Meta-Llama-3-8B-Instruct/"
DEFAULT_TOKENIZER="Meta-Llama-3-8B-Instruct/tokenizer.model"

echo ""
echo "Model Configuration:"
echo "-------------------"
read -p "Checkpoint directory [${DEFAULT_CKPT_DIR}]: " CKPT_DIR
CKPT_DIR=${CKPT_DIR:-$DEFAULT_CKPT_DIR}

read -p "Tokenizer path [${DEFAULT_TOKENIZER}]: " TOKENIZER_PATH
TOKENIZER_PATH=${TOKENIZER_PATH:-$DEFAULT_TOKENIZER}

# Check if model files exist
if [ ! -d "$CKPT_DIR" ]; then
    echo ""
    echo "⚠️  Warning: Model directory '$CKPT_DIR' not found!"
    echo ""
    echo "📥 To download the Llama 3 model:"
    echo "   1. Visit https://llama.meta.com/llama-downloads/"
    echo "   2. Register and accept the terms to get a download URL"
    echo "   3. Run: ./download.sh"
    echo "   4. Paste your download URL when prompted"
    echo "   5. Select '8B-instruct' when asked which model to download"
    echo ""
    echo "⏱️  Note: Download size is ~15GB and may take 10-30 minutes"
    echo ""
    read -p "Continue anyway? (y/n): " continue_choice
    if [ "$continue_choice" != "y" ]; then
        echo ""
        echo "Exiting. Please download the model first."
        echo ""
        echo "Quick start:"
        echo "  1. Make download script executable: chmod +x download.sh"
        echo "  2. Run: ./download.sh"
        echo "  3. Then run this launcher again: ./launch_app.sh"
        exit 1
    fi
else
    echo "✓ Model directory found: $CKPT_DIR"
    
    # Check if tokenizer exists
    if [ ! -f "$TOKENIZER_PATH" ]; then
        echo "⚠️  Warning: Tokenizer file not found: $TOKENIZER_PATH"
        echo "The model directory exists but tokenizer is missing."
        echo "Please ensure the model was downloaded completely."
    else
        echo "✓ Tokenizer found: $TOKENIZER_PATH"
    fi
fi

echo ""
echo "🎬 Launching app..."
echo ""

# Function to handle launch errors
handle_launch_error() {
    local exit_code=$1
    echo ""
    echo "❌ Application exited with error code: $exit_code"
    echo ""
    echo "Common issues and solutions:"
    echo "  • Out of memory: Reduce max_seq_len (e.g., --max_seq_len 128)"
    echo "  • CUDA error: GPU may not be available, will use CPU (slower)"
    echo "  • Model not found: Verify model path and files are complete"
    echo "  • Import errors: Reinstall dependencies with: pip install -e ."
    echo ""
    echo "For more help, see LAUNCH.md and TROUBLESHOOTING section"
    exit $exit_code
}

case $choice in
    1)
        read -p "Story topic [a brave knight]: " TOPIC
        TOPIC=${TOPIC:-"a brave knight"}
        echo ""
        echo "Running: torchrun --nproc_per_node 1 my_first_app.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH --topic \"$TOPIC\""
        echo ""
        torchrun --nproc_per_node 1 my_first_app.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH" \
            --topic "$TOPIC" || handle_launch_error $?
        ;;
    2)
        echo "Running: torchrun --nproc_per_node 1 interactive_chatbot.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH"
        echo ""
        torchrun --nproc_per_node 1 interactive_chatbot.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH" || handle_launch_error $?
        ;;
    3)
        echo "Running: torchrun --nproc_per_node 1 example_chat_completion.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH"
        echo ""
        torchrun --nproc_per_node 1 example_chat_completion.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH" \
            --max_seq_len 512 \
            --max_batch_size 6 || handle_launch_error $?
        ;;
    4)
        echo "Running: torchrun --nproc_per_node 1 example_text_completion.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH"
        echo ""
        torchrun --nproc_per_node 1 example_text_completion.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH" \
            --max_seq_len 128 \
            --max_batch_size 4 || handle_launch_error $?
        ;;
    5)
        read -p "Port number [5000]: " PORT
        PORT=${PORT:-5000}
        echo ""
        echo "🌿 Starting The Hemp Seed web application..."
        echo ""
        echo "Running: python hemp_seed_app.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH --port $PORT"
        echo ""
        echo "After the server starts, open your browser to: http://127.0.0.1:$PORT"
        echo ""
        python hemp_seed_app.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH" \
            --port "$PORT" || handle_launch_error $?
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "✅ Application completed successfully!"
echo ""
