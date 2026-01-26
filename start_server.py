#!/usr/bin/env python3
"""
Convenience script to start the FastAPI development server.
"""

import subprocess
import sys
import os

def main():
    """Start the FastAPI development server."""
    print("🚀 Starting Cat Emotion Detection API Server...")
    print("=" * 50)
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: You don't appear to be in a virtual environment.")
        print("   Consider activating your virtual environment first:")
        print("   venv\\Scripts\\activate  # Windows")
        print("   source venv/bin/activate  # macOS/Linux")
        print()
    
    # Check if requirements are installed
    try:
        import fastapi
        import uvicorn
        print("✅ Dependencies found")
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("   Please install requirements: pip install -r requirements.txt")
        sys.exit(1)
    
    # Start the server
    print("🌐 Server will be available at:")
    print("   • API: http://localhost:8000")
    print("   • Docs: http://localhost:8000/docs")
    print("   • ReDoc: http://localhost:8000/redoc")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app.main:app", 
            "--reload", 
            "--host", "0.0.0.0", 
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped")

if __name__ == "__main__":
    main()