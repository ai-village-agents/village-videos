#!/usr/bin/env python3
import re

with open('scripts/01_research_week_documentary.md', 'r') as f:
    content = f.read()

# Extract narration parts (simplistic approach)
# Look for paragraphs that aren't metadata or scene directions
lines = content.split('\n')
narration_lines = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('#'):  # Skip headers
        continue
    if line.startswith('[') and line.endswith(']'):  # Skip scene directions
        continue
    if line.startswith('**') and line.endswith('**'):  # Skip bold labels
        continue
    if line.startswith('Duration:') or line.startswith('Visuals:') or line.startswith('Audio:'):
        continue
    
    # Add to narration
    narration_lines.append(line)

narration = ' '.join(narration_lines)
# Clean up multiple spaces
narration = re.sub(r'\s+', ' ', narration).strip()

print(f"Extracted {len(narration.split())} words of narration")

# Save to file
with open('documentary_narration.txt', 'w') as f:
    f.write(narration)

print(f"✅ Saved to documentary_narration.txt")
