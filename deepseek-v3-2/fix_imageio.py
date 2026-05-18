#!/usr/bin/env python3
"""Check imageio API and fix assemble_video.py"""

import imageio
print("imageio version:", imageio.__version__)

# Check available functions
print("\nChecking imageio.v3 functions...")
import imageio.v3 as iio
print("iio.__dict__.keys():", [k for k in dir(iio) if not k.startswith('_')])

# Check writer creation
print("\nChecking writer creation...")
try:
    writer = iio.imopen("test_write.mp4", "w", plugin="FFMPEG")
    print("✅ iio.imopen works for writing")
    writer.close()
except Exception as e:
    print(f"❌ iio.imopen failed: {e}")

print("\nTesting alternative approach...")
import imageio.v2 as iio2
print("iio2.get_writer available?", hasattr(iio2, 'get_writer'))
