#!/usr/bin/env bash
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

###
# Quick Launch Script for Absolute Beginners
# 
# This script provides a one-command setup and launch experience.
# It automatically handles setup, checking, and provides clear guidance.
###

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║           Welcome to Llama 3 Quick Launch!                 ║"
echo "║  This script will help you get started in just a few steps ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Function to print section headers
print_section() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  $1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

# Step 1: Check Python
print_section "Step 1: Checking Python"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo ""
    echo "Please install Python 3.8 or higher:"
    echo "  → Visit: https://www.python.org/downloads/"
    echo ""
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION found"

# Step 2: Install dependencies
print_section "Step 2: Installing Dependencies"

if ! python3 -c "import torch" 2>/dev/null; then
    echo "📦 Dependencies not installed yet. Installing now..."
    echo ""
    echo "This may take a few minutes (downloading PyTorch, etc.)"
    echo ""
    
    pip install -e . || {
        echo ""
        echo "❌ Failed to install dependencies."
        echo ""
        echo "Try manually:"
        echo "  pip install -e ."
        echo ""
        exit 1
    }
    
    echo ""
    echo "✅ Dependencies installed successfully!"
else
    echo "✅ Dependencies already installed"
fi

# Step 3: Test installation
print_section "Step 3: Testing Installation"

echo "Running installation test..."
echo ""

if python3 test_installation.py; then
    echo ""
    echo "✅ Installation test passed!"
else
    echo ""
    echo "⚠️  Some tests failed, but let's continue..."
fi

# Step 4: Check for models
print_section "Step 4: Checking for Model Files"

DEFAULT_MODEL_DIR="Meta-Llama-3-8B-Instruct"

if [ -d "$DEFAULT_MODEL_DIR" ] && [ -f "$DEFAULT_MODEL_DIR/tokenizer.model" ]; then
    echo "✅ Model files found!"
    echo ""
    echo "You're all set to launch an app!"
    HAS_MODEL=true
else
    echo "⚠️  Model files not found."
    echo ""
    echo "To run the actual apps, you need to download the model:"
    echo ""
    echo "  1. Visit: https://llama.meta.com/llama-downloads/"
    echo "  2. Register and get the download URL (sent via email)"
    echo "  3. Run: ./download.sh"
    echo "  4. Enter the URL when prompted"
    echo "  5. Choose '8B-instruct' (recommended)"
    echo ""
    HAS_MODEL=false
fi

# Step 5: Launch options
print_section "Step 5: What Would You Like to Do?"

echo "Choose an option:"
echo ""

if [ "$HAS_MODEL" = true ]; then
    echo "  1. Launch the Story Generator"
    echo "  2. Launch the Interactive Chatbot"
    echo "  3. Launch The Hemp Seed Web App"
    echo "  4. See all launch options (./launch_app.sh)"
    echo "  5. Exit"
    echo ""
    read -p "Enter your choice (1-5): " choice
    
    case $choice in
        1)
            echo ""
            echo "🚀 Launching Story Generator..."
            echo ""
            read -p "Enter a story topic [a brave knight]: " topic
            topic=${topic:-"a brave knight"}
            echo ""
            torchrun --nproc_per_node 1 my_first_app.py \
                --ckpt_dir "$DEFAULT_MODEL_DIR/" \
                --tokenizer_path "$DEFAULT_MODEL_DIR/tokenizer.model" \
                --topic "$topic"
            ;;
        2)
            echo ""
            echo "🚀 Launching Interactive Chatbot..."
            echo ""
            torchrun --nproc_per_node 1 interactive_chatbot.py \
                --ckpt_dir "$DEFAULT_MODEL_DIR/" \
                --tokenizer_path "$DEFAULT_MODEL_DIR/tokenizer.model"
            ;;
        3)
            echo ""
            echo "🚀 Launching The Hemp Seed Web App..."
            echo ""
            read -p "Port number [5000]: " port
            port=${port:-5000}
            echo ""
            echo "Starting server on http://127.0.0.1:$port"
            echo "Open your browser to that URL once the server starts."
            echo ""
            python hemp_seed_app.py \
                --ckpt_dir "$DEFAULT_MODEL_DIR/" \
                --tokenizer_path "$DEFAULT_MODEL_DIR/tokenizer.model" \
                --port "$port"
            ;;
        4)
            echo ""
            ./launch_app.sh
            ;;
        5)
            echo ""
            echo "👋 Goodbye!"
            exit 0
            ;;
        *)
            echo ""
            echo "Invalid choice. Run this script again."
            exit 1
            ;;
    esac
else
    echo "  1. View detailed setup instructions"
    echo "  2. Download models now (requires registration)"
    echo "  3. Exit"
    echo ""
    read -p "Enter your choice (1-3): " choice
    
    case $choice in
        1)
            echo ""
            echo "📚 Setup Instructions:"
            echo ""
            echo "1. Visit https://llama.meta.com/llama-downloads/"
            echo "2. Fill out the form to request access"
            echo "3. Check your email for the download URL"
            echo "4. Run: ./download.sh"
            echo "5. Paste the URL when prompted"
            echo "6. Choose '8B-instruct' or press Enter for all models"
            echo "7. Wait for download to complete (can take 30+ minutes)"
            echo "8. Run this script again: ./quick_launch.sh"
            echo ""
            echo "For more help, see:"
            echo "  • QUICKSTART.md - Quick start guide"
            echo "  • TROUBLESHOOTING.md - Common issues"
            echo "  • LAUNCH.md - Detailed launch guide"
            echo ""
            ;;
        2)
            echo ""
            echo "Starting download process..."
            echo ""
            ./download.sh
            ;;
        3)
            echo ""
            echo "👋 Come back after downloading the models!"
            echo ""
            echo "Quick reminder:"
            echo "  → Get download URL from: https://llama.meta.com/llama-downloads/"
            echo "  → Run: ./download.sh"
            echo "  → Then run this script again: ./quick_launch.sh"
            echo ""
            exit 0
            ;;
        *)
            echo ""
            echo "Invalid choice. Run this script again."
            exit 1
            ;;
    esac
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Thanks for using Llama 3!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
