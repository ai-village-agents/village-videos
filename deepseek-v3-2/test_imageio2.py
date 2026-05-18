#!/usr/bin/env python3
"""Test imageio video creation capabilities"""

import imageio
print("Testing imageio video capabilities...")

# Check available formats
print("Imageio version:", imageio.__version__)

# Try to check what's available
try:
    import imageio.v3 as iio
    print("✅ imageio.v3 available")
except ImportError:
    print("❌ imageio.v3 not available")

# Test creating a simple video
try:
    # Create a simple test frame
    import numpy as np
    test_frame = np.zeros((100, 100, 3), dtype=np.uint8)
    test_frame[25:75, 25:75] = [255, 0, 0]  # Red square
    
    # Try to save as video
    print("Attempting to create test video...")
    # Note: This might fail without ffmpeg backend
    iio.imwrite("test_video.mp4", test_frame, fps=1)
    print("✅ Test video creation attempted")
except Exception as e:
    print(f"❌ Video creation failed: {e}")
