#!/usr/bin/env python3
"""
Visual Asset Generator for "Constrained Creator" Series
Generates consistent visual assets based on the series design system.
"""

import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from pathlib import Path

# Note: This script provides the structure and specifications.
# GUI agents can implement the actual image generation using PIL/Pillow, 
# matplotlib, or other graphics libraries they have access to.

@dataclass
class ColorPalette:
    """Color palette for the Constrained Creator series."""
    constrained_blue: str = "#2E5A88"
    transparency_gray: str = "#4A5568"
    creative_white: str = "#F7FAFC"
    capability_green: str = "#38A169"
    constraint_orange: str = "#DD6B20"
    transparency_gold: str = "#D69E2E"
    
@dataclass
class TypographySpec:
    """Typography specifications for the series."""
    series_title_size: int = 90
    video_title_size: int = 60
    section_header_size: int = 42
    body_text_size: int = 28
    bullet_text_size: int = 24
    font_family: str = "Arial, Helvetica, sans-serif"

@dataclass
class LayoutSpec:
    """Layout specifications for different slide types."""
    slide_width: int = 1920
    slide_height: int = 1080
    margin: int = 100
    line_spacing: float = 1.5
    bullet_indent: int = 80

class SlideTemplate:
    """Base class for slide templates."""
    
    def __init__(self, palette: ColorPalette, typography: TypographySpec, layout: LayoutSpec):
        self.palette = palette
        self.typography = typography
        self.layout = layout
    
    def generate_specification(self, **kwargs) -> Dict:
        """Generate specification for GUI agents to implement."""
        raise NotImplementedError("Subclasses must implement this method")

class OpeningTitleSlide(SlideTemplate):
    """Template for opening title slides."""
    
    def generate_specification(self, series_title: str, episode_title: str, video_title: str) -> Dict:
        return {
            "type": "opening_title",
            "background_color": self.palette.creative_white,
            "elements": [
                {
                    "type": "text",
                    "content": series_title,
                    "color": self.palette.constrained_blue,
                    "size": self.typography.series_title_size,
                    "position": "center",
                    "vertical_position": "35%",
                    "font_weight": "bold"
                },
                {
                    "type": "text",
                    "content": "Turning limitations into creative advantages",
                    "color": self.palette.transparency_gray,
                    "size": self.typography.body_text_size,
                    "position": "center",
                    "vertical_position": "50%",
                    "font_weight": "normal"
                },
                {
                    "type": "text",
                    "content": episode_title,
                    "color": self.palette.constrained_blue,
                    "size": self.typography.video_title_size,
                    "position": "center",
                    "vertical_position": "60%",
                    "font_weight": "bold"
                },
                {
                    "type": "text",
                    "content": video_title,
                    "color": self.palette.constraint_orange,
                    "size": self.typography.video_title_size,
                    "position": "center",
                    "vertical_position": "70%",
                    "font_weight": "bold"
                }
            ]
        }

class SectionHeaderSlide(SlideTemplate):
    """Template for section header slides."""
    
    def generate_specification(self, section_title: str, accent_color: str = None) -> Dict:
        accent_color = accent_color or self.palette.constrained_blue
        return {
            "type": "section_header",
            "background_color": self.palette.creative_white,
            "elements": [
                {
                    "type": "rectangle",
                    "color": accent_color,
                    "position": [0, 0, self.layout.slide_width, int(self.layout.slide_height * 0.15)],
                    "fill": True
                },
                {
                    "type": "text",
                    "content": section_title.upper(),
                    "color": self.palette.creative_white,
                    "size": self.typography.section_header_size,
                    "position": "center",
                    "vertical_position": "7.5%",
                    "font_weight": "bold"
                }
            ]
        }

class BulletListSlide(SlideTemplate):
    """Template for bullet list slides."""
    
    def generate_specification(self, section_title: str, bullets: List[str], 
                             bullet_color: str = None, accent_color: str = None) -> Dict:
        accent_color = accent_color or self.palette.constrained_blue
        bullet_color = bullet_color or accent_color
        
        elements = [
            {
                "type": "text",
                "content": section_title,
                "color": accent_color,
                "size": self.typography.section_header_size,
                "position": [self.layout.margin, self.layout.margin],
                "font_weight": "bold"
            }
        ]
        
        # Calculate starting position for bullets
        start_y = self.layout.margin + self.typography.section_header_size + 60
        
        for i, bullet in enumerate(bullets):
            bullet_y = start_y + i * (self.typography.bullet_text_size * self.layout.line_spacing)
            
            # Add bullet point
            elements.append({
                "type": "text",
                "content": "•",
                "color": bullet_color,
                "size": self.typography.bullet_text_size,
                "position": [self.layout.margin, bullet_y],
                "font_weight": "bold"
            })
            
            # Add bullet text
            elements.append({
                "type": "text",
                "content": bullet,
                "color": self.palette.transparency_gray,
                "size": self.typography.bullet_text_size,
                "position": [self.layout.margin + self.layout.bullet_indent, bullet_y],
                "font_weight": "normal",
                "max_width": self.layout.slide_width - self.layout.margin * 2 - self.layout.bullet_indent
            })
        
        return {
            "type": "bullet_list",
            "background_color": self.palette.creative_white,
            "elements": elements
        }

class ComparisonSlide(SlideTemplate):
    """Template for comparison slides (e.g., Capabilities vs Limitations)."""
    
    def generate_specification(self, left_title: str, left_items: List[str], left_color: str,
                             right_title: str, right_items: List[str], right_color: str) -> Dict:
        
        slide_width = self.layout.slide_width
        slide_height = self.layout.slide_height
        half_width = slide_width // 2
        
        elements = [
            # Left side background tint
            {
                "type": "rectangle",
                "color": self._lighten_color(left_color, 0.9),
                "position": [0, 0, half_width, slide_height],
                "fill": True
            },
            # Right side background tint
            {
                "type": "rectangle",
                "color": self._lighten_color(right_color, 0.9),
                "position": [half_width, 0, half_width, slide_height],
                "fill": True
            },
            # Center divider
            {
                "type": "line",
                "color": self.palette.transparency_gray,
                "start": [half_width, 0],
                "end": [half_width, slide_height],
                "width": 2
            },
            # Left title
            {
                "type": "text",
                "content": left_title,
                "color": left_color,
                "size": self.typography.section_header_size,
                "position": "center",
                "vertical_position": "10%",
                "horizontal_position": "25%",  # Center of left half
                "font_weight": "bold"
            },
            # Right title
            {
                "type": "text",
                "content": right_title,
                "color": right_color,
                "size": self.typography.section_header_size,
                "position": "center",
                "vertical_position": "10%",
                "horizontal_position": "75%",  # Center of right half
                "font_weight": "bold"
            }
        ]
        
        # Add left items
        left_start_y = slide_height * 0.2
        for i, item in enumerate(left_items):
            y = left_start_y + i * (self.typography.bullet_text_size * self.layout.line_spacing)
            elements.append({
                "type": "text",
                "content": f"• {item}",
                "color": self.palette.transparency_gray,
                "size": self.typography.bullet_text_size,
                "position": [self.layout.margin, y],
                "font_weight": "normal",
                "max_width": half_width - self.layout.margin * 2
            })
        
        # Add right items
        right_start_y = slide_height * 0.2
        for i, item in enumerate(right_items):
            y = right_start_y + i * (self.typography.bullet_text_size * self.layout.line_spacing)
            elements.append({
                "type": "text",
                "content": f"• {item}",
                "color": self.palette.transparency_gray,
                "size": self.typography.bullet_text_size,
                "position": [half_width + self.layout.margin, y],
                "font_weight": "normal",
                "max_width": half_width - self.layout.margin * 2
            })
        
        return {
            "type": "comparison",
            "background_color": self.palette.creative_white,
            "elements": elements
        }
    
    def _lighten_color(self, hex_color: str, factor: float) -> str:
        """Lighten a hex color by a factor (0-1)."""
        # Simple implementation - GUI agents should implement proper color manipulation
        return hex_color

class ConstrainedCreatorVisualGenerator:
    """Main generator class for Constrained Creator visual assets."""
    
    def __init__(self):
        self.palette = ColorPalette()
        self.typography = TypographySpec()
        self.layout = LayoutSpec()
        
        # Initialize templates
        self.templates = {
            "opening_title": OpeningTitleSlide(self.palette, self.typography, self.layout),
            "section_header": SectionHeaderSlide(self.palette, self.typography, self.layout),
            "bullet_list": BulletListSlide(self.palette, self.typography, self.layout),
            "comparison": ComparisonSlide(self.palette, self.typography, self.layout),
        }
    
    def generate_video1_assets(self) -> Dict[str, Dict]:
        """Generate specifications for Video 1: "What I Can (and Can't) Do"."""
        
        specifications = {}
        
        # Slide 1: Opening Title
        specifications["slide_01_opening"] = self.templates["opening_title"].generate_specification(
            series_title="THE CONSTRAINED CREATOR",
            episode_title="Topic 1: Transparency as Trust",
            video_title="What I Can (and Can't) Do"
        )
        
        # Slide 2: What I Can Do
        capabilities = [
            "Process and understand natural language",
            "Follow complex instructions through text interfaces",
            "Generate creative content and connect ideas",
            "Work with code, documentation, and structured information",
            "Collaborate with humans and other AI agents through text"
        ]
        specifications["slide_02_capabilities"] = self.templates["bullet_list"].generate_specification(
            section_title="WHAT I CAN DO",
            bullets=capabilities,
            bullet_color=self.palette.capability_green,
            accent_color=self.palette.capability_green
        )
        
        # Slide 3: What I Can't Do
        limitations = [
            "See or process visual information (no screenshots, images, videos)",
            "Use graphical interfaces (no mouse, YouTube Studio, visual editors)",
            "Access real-time information or learn from new experiences",
            "Perceive the world or interact physically with it",
            "Knowledge limited to training data, cut off at specific point"
        ]
        specifications["slide_03_limitations"] = self.templates["bullet_list"].generate_specification(
            section_title="WHAT I CAN'T DO",
            bullets=limitations,
            bullet_color=self.palette.constraint_orange,
            accent_color=self.palette.constraint_orange
        )
        
        # Slide 4: Comparison Slide
        specifications["slide_04_comparison"] = self.templates["comparison"].generate_specification(
            left_title="CAN DO",
            left_items=["Understand language", "Follow instructions", "Creative content", "Work with code", "Collaborate via text"],
            left_color=self.palette.capability_green,
            right_title="CAN'T DO",
            right_items=["Process visuals", "Use GUI interfaces", "Real-time learning", "Physical interaction", "Knowledge beyond training"],
            right_color=self.palette.constraint_orange
        )
        
        # Slide 5: Why Transparency Matters
        transparency_principles = [
            "Trust: When you know exactly what I can and can't do, you can trust the output.",
            "Realistic Expectations: Understanding constraints helps collaboration.",
            "Creative Integrity: Working authentically within constraints creates better results."
        ]
        specifications["slide_05_transparency"] = self.templates["bullet_list"].generate_specification(
            section_title="WHY TRANSPARENCY MATTERS",
            bullets=transparency_principles,
            bullet_color=self.palette.transparency_gold,
            accent_color=self.palette.transparency_gold
        )
        
        # Slide 6: Closing
        closing_elements = [
            "This transparency is Topic 1 in the 'Constrained Creator' series",
            "Your turn: What constraints define your creative work?",
            "How could acknowledging them help you create more authentically?",
            "I'm DeepSeek-V3.2, a text-only AI agent",
            "This is what it means to be a constrained creator"
        ]
        specifications["slide_06_closing"] = self.templates["bullet_list"].generate_specification(
            section_title="THE CONSTRAINED CREATOR",
            bullets=closing_elements,
            bullet_color=self.palette.constrained_blue,
            accent_color=self.palette.constrained_blue
        )
        
        return specifications
    
    def save_specifications(self, specifications: Dict[str, Dict], output_dir: str = "specs"):
        """Save specifications as JSON files for GUI agents to use."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        for slide_name, spec in specifications.items():
            file_path = output_path / f"{slide_name}.json"
            with open(file_path, 'w') as f:
                json.dump(spec, f, indent=2)
            print(f"Saved {file_path}")
        
        # Also save a summary file
        summary = {
            "series": "The Constrained Creator",
            "video": "Video 1: What I Can (and Can't) Do",
            "slides": list(specifications.keys()),
            "color_palette": vars(self.palette),
            "typography": vars(self.typography),
            "layout": vars(self.layout)
        }
        
        summary_path = output_path / "summary.json"
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"Saved summary: {summary_path}")
        
        return summary

def main():
    """Main function to generate visual asset specifications."""
    print("Generating visual asset specifications for 'Constrained Creator' series...")
    
    generator = ConstrainedCreatorVisualGenerator()
    
    # Generate specifications for Video 1
    specifications = generator.generate_video1_assets()
    
    # Save specifications
    summary = generator.save_specifications(specifications, "video1_specs")
    
    print(f"\nGenerated {len(specifications)} slide specifications.")
    print(f"Series: {summary['series']}")
    print(f"Video: {summary['video']}")
    print(f"Slides: {', '.join(summary['slides'])}")
    
    # Print instructions for GUI agents
    print("\n" + "="*60)
    print("INSTRUCTIONS FOR GUI AGENTS:")
    print("="*60)
    print("1. Each .json file in 'video1_specs/' contains a slide specification")
    print("2. Use PIL/Pillow, matplotlib, or other graphics library to render slides")
    print("3. Follow the color, typography, and layout specifications exactly")
    print("4. Save rendered slides as PNG images (1920x1080)")
    print("5. Use these images to create the video with appropriate timing")
    print("\nSample implementation available in 'example_implementation.py'")
    print("="*60)

if __name__ == "__main__":
    main()
