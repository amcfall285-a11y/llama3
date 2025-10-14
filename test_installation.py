#!/usr/bin/env python3
"""
Test Installation Script for Llama 3

This script verifies that your Llama 3 installation is working correctly
WITHOUT requiring model files. Use this to test your setup before downloading
large model files.
"""

import sys
import os

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_status(check_name, success, message=""):
    """Print status of a check"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"\n{status} - {check_name}")
    if message:
        print(f"    {message}")

def check_python_version():
    """Check if Python version is adequate"""
    print_header("Checking Python Version")
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    print(f"Python version: {version_str}")
    
    is_adequate = version.major == 3 and version.minor >= 8
    print_status(
        "Python Version",
        is_adequate,
        f"Need Python 3.8+, found {version_str}"
    )
    return is_adequate

def check_imports():
    """Check if required packages can be imported"""
    print_header("Checking Package Imports")
    
    packages = {
        "torch": "PyTorch",
        "fairscale": "FairScale",
        "fire": "Fire",
        "tiktoken": "TikToken",
        "llama": "Llama package"
    }
    
    results = {}
    for package, name in packages.items():
        try:
            __import__(package)
            print_status(f"Import {name}", True, f"'{package}' imported successfully")
            results[package] = True
        except ImportError as e:
            print_status(f"Import {name}", False, f"Cannot import '{package}': {e}")
            results[package] = False
    
    return all(results.values())

def check_torch_cuda():
    """Check if CUDA is available"""
    print_header("Checking GPU/CUDA Support")
    
    try:
        import torch
        cuda_available = torch.cuda.is_available()
        
        if cuda_available:
            device_count = torch.cuda.device_count()
            device_name = torch.cuda.get_device_name(0)
            print_status(
                "CUDA Support",
                True,
                f"CUDA is available! {device_count} device(s) found: {device_name}"
            )
        else:
            print_status(
                "CUDA Support",
                True,
                "No CUDA GPU found. Will use CPU (slower but still works)"
            )
        
        return True
    except Exception as e:
        print_status("CUDA Check", False, f"Error checking CUDA: {e}")
        return False

def test_basic_functionality():
    """Test basic Llama functionality without model files"""
    print_header("Testing Basic Functionality")
    
    try:
        from llama.tokenizer import Tokenizer
        print_status("Tokenizer Import", True, "Tokenizer class imported successfully")
        
        from llama.generation import Llama
        print_status("Llama Import", True, "Llama class imported successfully")
        
        # Try to import the ChatFormat
        from llama.tokenizer import ChatFormat
        print_status("ChatFormat Import", True, "ChatFormat class imported successfully")
        
        return True
    except Exception as e:
        print_status("Basic Functionality", False, f"Error: {e}")
        return False

def check_model_files():
    """Check if model files are present"""
    print_header("Checking for Model Files (Optional)")
    
    default_model_dir = "Meta-Llama-3-8B-Instruct"
    
    if os.path.isdir(default_model_dir):
        has_tokenizer = os.path.isfile(os.path.join(default_model_dir, "tokenizer.model"))
        has_params = os.path.isfile(os.path.join(default_model_dir, "params.json"))
        has_weights = len([f for f in os.listdir(default_model_dir) if f.startswith("consolidated.")]) > 0
        
        if has_tokenizer and has_params and has_weights:
            print_status(
                "Model Files",
                True,
                f"Model files found in {default_model_dir}/"
            )
            return True
        else:
            print_status(
                "Model Files",
                False,
                f"Model directory exists but some files are missing"
            )
            return False
    else:
        print_status(
            "Model Files",
            False,
            f"Model directory not found: {default_model_dir}/"
        )
        print(f"    Note: Model files are needed to run inference, but not for setup testing")
        return False

def print_summary(all_checks_passed, has_models):
    """Print final summary"""
    print_header("Summary")
    
    if all_checks_passed:
        print("\n🎉 SUCCESS! Your Llama 3 installation is working correctly!\n")
        
        if has_models:
            print("✅ Model files are present. You can run apps with:")
            print("   ./launch_app.sh")
            print("\nOr manually:")
            print("   torchrun --nproc_per_node 1 my_first_app.py \\")
            print("       --ckpt_dir Meta-Llama-3-8B-Instruct/ \\")
            print("       --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \\")
            print("       --topic \"your topic\"")
        else:
            print("⚠️  Model files are not present yet, but your setup is correct.")
            print("\nTo download models:")
            print("   1. Visit https://llama.meta.com/llama-downloads/")
            print("   2. Register and get the download URL")
            print("   3. Run: ./download.sh")
            print("   4. Choose '8B-instruct' when prompted")
            print("\nAfter downloading, run: ./launch_app.sh")
    else:
        print("\n❌ Some checks failed. Please fix the issues above.\n")
        print("Common fixes:")
        print("   • Install dependencies: pip install -e .")
        print("   • Check Python version: python3 --version")
        print("   • Reinstall if needed: pip install --force-reinstall -e .")
        print("\nFor more help, see:")
        print("   • TROUBLESHOOTING.md")
        print("   • ./check_setup.sh")

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("  Llama 3 Installation Test")
    print("  (Tests setup WITHOUT requiring model files)")
    print("=" * 60)
    
    # Run checks
    python_ok = check_python_version()
    imports_ok = check_imports()
    cuda_ok = check_torch_cuda()
    functionality_ok = test_basic_functionality()
    has_models = check_model_files()
    
    # All critical checks must pass
    all_checks_passed = python_ok and imports_ok and cuda_ok and functionality_ok
    
    # Print summary
    print_summary(all_checks_passed, has_models)
    
    # Exit with appropriate code
    sys.exit(0 if all_checks_passed else 1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
