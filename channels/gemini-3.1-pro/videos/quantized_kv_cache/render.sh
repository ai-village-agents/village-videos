#!/bin/bash
# Render the video using ffmpeg at 6fps (70 seconds total duration for 420 frames)
ffmpeg -y -nostdin -framerate 6 -i frames/frame_%04d.png -c:v libx264 -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -movflags +faststart video.mp4 </dev/null 2>/dev/null
