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

echo "✓ Python $(python3 --version | cut -d' ' -f2) detected"

# Check if package is installed
if ! python3 -c "import llama" 2>/dev/null; then
    echo ""
    echo "📦 Installing dependencies..."
    echo "This will install the llama3 package and its dependencies."
    pip install -e . || {
        echo "❌ Failed to install dependencies"
        echo "Please run: pip install -e ."
        exit 1
    }
    echo "✅ Dependencies installed successfully!"
fi

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
    echo "To download the model:"
    echo "1. Visit https://llama.meta.com/llama-downloads/"
    echo "2. Register and get the download URL"
    echo "3. Run: ./download.sh"
    echo "4. Follow the prompts to download Meta-Llama-3-8B-Instruct"
    echo ""
    read -p "Continue anyway? (y/n): " continue_choice
    if [ "$continue_choice" != "y" ]; then
        echo "Exiting..."
        exit 1
    fi
fi

echo ""
echo "🎬 Launching app..."
echo ""

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
            --topic "$TOPIC"
        ;;
    2)
        echo "Running: torchrun --nproc_per_node 1 interactive_chatbot.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH"
        echo ""
        torchrun --nproc_per_node 1 interactive_chatbot.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH"
        ;;
    3)
        echo "Running: torchrun --nproc_per_node 1 example_chat_completion.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH"
        echo ""
        torchrun --nproc_per_node 1 example_chat_completion.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH" \
            --max_seq_len 512 \
            --max_batch_size 6
        ;;
    4)
        echo "Running: torchrun --nproc_per_node 1 example_text_completion.py --ckpt_dir $CKPT_DIR --tokenizer_path $TOKENIZER_PATH"
        echo ""
        torchrun --nproc_per_node 1 example_text_completion.py \
            --ckpt_dir "$CKPT_DIR" \
            --tokenizer_path "$TOKENIZER_PATH" \
            --max_seq_len 128 \
            --max_batch_size 4
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
            --port "$PORT"
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac
