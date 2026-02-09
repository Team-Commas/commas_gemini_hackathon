#!/usr/bin/env python3
"""
Generate extension icons
Creates simple icons for the Chrome extension
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    """Create a simple icon with a magnifying glass design"""
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background circle
    padding = size // 8
    draw.ellipse(
        [padding, padding, size - padding, size - padding],
        fill='#4285f4',
        outline='#3367d6',
        width=max(1, size // 32)
    )
    
    # Magnifying glass
    center = size // 2
    glass_radius = size // 4
    
    # Glass circle
    draw.ellipse(
        [center - glass_radius, center - glass_radius - size//16,
         center + glass_radius, center + glass_radius - size//16],
        fill=None,
        outline='white',
        width=max(2, size // 16)
    )
    
    # Handle
    handle_start_x = center + int(glass_radius * 0.7)
    handle_start_y = center + int(glass_radius * 0.7) - size//16
    handle_end_x = center + int(glass_radius * 1.5)
    handle_end_y = center + int(glass_radius * 1.5) - size//16
    
    draw.line(
        [handle_start_x, handle_start_y, handle_end_x, handle_end_y],
        fill='white',
        width=max(2, size // 16)
    )
    
    # Save
    img.save(filename, 'PNG')
    print(f"✓ Created {filename} ({size}x{size})")

def main():
    """Generate all required icon sizes"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    sizes = [
        (16, 'icon16.png'),
        (48, 'icon48.png'),
        (128, 'icon128.png')
    ]
    
    print("Generating extension icons...")
    print()
    
    for size, filename in sizes:
        filepath = os.path.join(script_dir, filename)
        create_icon(size, filepath)
    
    print()
    print("✓ All icons generated successfully!")
    print()
    print("Icons created:")
    print("  - icon16.png  (toolbar icon)")
    print("  - icon48.png  (extension management)")
    print("  - icon128.png (Chrome Web Store)")

if __name__ == "__main__":
    main()
