#!/bin/bash
set -e

echo "Rendering Scene 1..."
python3 generate_scene1_mha.py

echo "Rendering Scene 2..."
python3 generate_scene2_mha.py

echo "Rendering Scene 3..."
python3 generate_scene3_mha.py

echo "Rendering Scene 4..."
python3 generate_scene4_mha.py

echo "Rendering Scene 5..."
python3 generate_scene5_mha.py

echo "Trimming and Concat..."
./trim_scenes.sh
