"""
Example implementation for GUI agents to generate actual images from specifications.
This is a template - GUI agents should adapt based on their available libraries.
"""

import json
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List
import os

class SlideRenderer:
    """Example slide renderer using PIL/Pillow."""
    
    def __init__(self, width=1920, height=1080):
        self.width = width
        self.height = height
        self.font_cache = {}
    
    def load_font(self, size: int) -> ImageFont.FreeTypeFont:
        """Load a font of given size."""
        # Use a system font - adjust path as needed
        font_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "arial.ttf"
        ]
        
        for path in font_paths:
            if os.path.exists(path):
                try:
                    return ImageFont.truetype(path, size)
                except OSError:
                    continue
        
        # Fall back to default font
        return ImageFont.load_default()
    
    def hex_to_rgb(self, hex_color: str) -> tuple:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def render_slide(self, spec: Dict, output_path: str) -> bool:
        """Render a slide from specification."""
        try:
            # Create blank image
            bg_color = self.hex_to_rgb(spec.get("background_color", "#F7FAFC"))
            image = Image.new('RGB', (self.width, self.height), bg_color)
            draw = ImageDraw.Draw(image)
            
            # Render each element
            for element in spec.get("elements", []):
                self.render_element(draw, element)
            
            # Save image
            image.save(output_path, 'PNG')
            print(f"Rendered slide: {output_path}")
            return True
            
        except Exception as e:
            print(f"Error rendering slide: {e}")
            return False
    
    def render_element(self, draw: ImageDraw, element: Dict):
        """Render a single element."""
        element_type = element.get("type", "")
        
        if element_type == "text":
            self.render_text(draw, element)
        elif element_type == "rectangle":
            self.render_rectangle(draw, element)
        elif element_type == "line":
            self.render_line(draw, element)
    
    def render_text(self, draw: ImageDraw, element: Dict):
        """Render text element."""
        content = element.get("content", "")
        color = self.hex_to_rgb(element.get("color", "#000000"))
        size = element.get("size", 24)
        
        # Load font
        font_key = f"size_{size}"
        if font_key not in self.font_cache:
            self.font_cache[font_key] = self.load_font(size)
        font = self.font_cache[font_key]
        
        # Position handling
        position = element.get("position", "center")
        
        if isinstance(position, list):
            # Absolute position [x, y]
            x, y = position[0], position[1]
        elif position == "center":
            # Center position
            vertical = element.get("vertical_position", "50%")
            if isinstance(vertical, str) and '%' in vertical:
                y = self.height * float(vertical.strip('%')) / 100
            else:
                y = float(vertical)
            
            horizontal = element.get("horizontal_position", "50%")
            if isinstance(horizontal, str) and '%' in horizontal:
                x = self.width * float(horizontal.strip('%')) / 100
            else:
                x = float(horizontal)
            
            # Center the text
            text_bbox = draw.textbbox((0, 0), content, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            x -= text_width / 2
            
            text_height = text_bbox[3] - text_bbox[1]
            y -= text_height / 2
        else:
            # Default to top-left
            x, y = 100, 100
        
        # Draw text
        draw.text((x, y), content, fill=color, font=font)
    
    def render_rectangle(self, draw: ImageDraw, element: Dict):
        """Render rectangle element."""
        color = self.hex_to_rgb(element.get("color", "#000000"))
        position = element.get("position", [0, 0, 100, 100])
        fill = element.get("fill", False)
        
        if fill:
            draw.rectangle(position, fill=color)
        else:
            outline_width = element.get("width", 2)
            draw.rectangle(position, outline=color, width=outline_width)
    
    def render_line(self, draw: ImageDraw, element: Dict):
        """Render line element."""
        color = self.hex_to_rgb(element.get("color", "#000000"))
        start = element.get("start", [0, 0])
        end = element.get("end", [100, 100])
        width = element.get("width", 2)
        
        draw.line([tuple(start), tuple(end)], fill=color, width=width)

def render_all_slides(specs_dir: str, output_dir: str):
    """Render all slides from specifications."""
    os.makedirs(output_dir, exist_ok=True)
    
    renderer = SlideRenderer()
    
    # Find all specification files
    for filename in os.listdir(specs_dir):
        if filename.endswith('.json') and not filename.startswith('summary'):
            spec_path = os.path.join(specs_dir, filename)
            output_path = os.path.join(output_dir, filename.replace('.json', '.png'))
            
            # Load specification
            with open(spec_path, 'r') as f:
                spec = json.load(f)
            
            # Render slide
            renderer.render_slide(spec, output_path)

if __name__ == "__main__":
    print("Example implementation for rendering slides from specifications.")
    print("GUI agents should adapt this to their available libraries and environment.")
    print("\nTo use:")
    print("1. First run generate_visual_assets.py to create specifications")
    print("2. Adapt this script to your graphics library (PIL, matplotlib, etc.)")
    print("3. Run render_all_slides('video1_specs', 'video1_images')")
