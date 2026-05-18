#!/usr/bin/env python3
"""Test imageio for video creation capabilities"""

try:
    import imageio
    import imageio.plugins.ffmpeg
    print("✅ imageio is available")
    
    # Check available writers
    print("Available video writers:", imageio.get_writer_formats())
    
    # Check if ffmpeg is available through imageio
    try:
        reader = imageio.get_reader('<video0>')
        print("✅ imageio can access video devices")
    except:
        print("❌ No video device access (expected)")
        
except ImportError as e:
    print(f"❌ imageio not available: {e}")

# Also check OpenCV
try:
    import cv2
    print("✅ OpenCV is available")
    print(f"OpenCV version: {cv2.__version__}")
except ImportError:
    print("❌ OpenCV not installed")
