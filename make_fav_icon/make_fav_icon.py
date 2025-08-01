#!/usr/bin/env python3
"""
Favicon Generator Script

This script converts a favicon.png image into all required favicon formats:
- favicon.ico (16x16, 32x32)
- favicon-32x32.png
- favicon-192x192.png
- favicon-512x512.png
- apple-touch-icon-180x180.png
- favicon.svg (converts PNG to SVG)

Usage:
    python make_fav_icon.py [input_image_path] [output_directory]
    
    If no arguments provided, it looks for favicon.png in current directory
    and outputs to ../images/
"""

import os
import sys
from PIL import Image
import base64

def create_svg_from_png(png_path, svg_path, size=512):
    """Convert PNG to SVG by embedding the PNG as base64"""
    with open(png_path, 'rb') as f:
        png_data = f.read()
    
    png_base64 = base64.b64encode(png_data).decode('utf-8')
    
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{size}" height="{size}" viewBox="0 0 {size} {size}">
  <image width="{size}" height="{size}" 
         xlink:href="data:image/png;base64,{png_base64}"/>
</svg>'''
    
    with open(svg_path, 'w') as f:
        f.write(svg_content)

def generate_favicons(input_path, output_dir):
    """Generate all favicon formats from input image"""
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the original image
    try:
        original = Image.open(input_path)
        print(f"✓ Loaded image: {input_path} ({original.size})")
    except Exception as e:
        print(f"✗ Error loading image: {e}")
        return False
    
    # Convert to RGBA if not already
    if original.mode != 'RGBA':
        original = original.convert('RGBA')
    
    # Define the sizes and formats we need
    formats = [
        # Format: (filename, size, format)
        ('favicon-32x32.png', 32, 'PNG'),
        ('favicon-192x192.png', 192, 'PNG'),
        ('favicon-512x512.png', 512, 'PNG'),
        ('apple-touch-icon-180x180.png', 180, 'PNG'),
    ]
    
    # Generate PNG formats
    for filename, size, format_type in formats:
        try:
            # Resize image maintaining aspect ratio
            resized = original.resize((size, size), Image.Resampling.LANCZOS)
            output_path = os.path.join(output_dir, filename)
            resized.save(output_path, format_type, optimize=True)
            print(f"✓ Created: {filename} ({size}x{size})")
        except Exception as e:
            print(f"✗ Error creating {filename}: {e}")
    
    # Generate ICO file (contains multiple sizes)
    try:
        ico_sizes = [(16, 16), (32, 32), (48, 48)]
        ico_images = []
        
        for size in ico_sizes:
            resized = original.resize(size, Image.Resampling.LANCZOS)
            ico_images.append(resized)
        
        ico_path = os.path.join(output_dir, 'favicon.ico')
        ico_images[0].save(ico_path, format='ICO', sizes=ico_sizes)
        print(f"✓ Created: favicon.ico (16x16, 32x32, 48x48)")
    except Exception as e:
        print(f"✗ Error creating favicon.ico: {e}")
    
    # Generate SVG file
    try:
        # First create a high-res PNG for the SVG
        high_res = original.resize((512, 512), Image.Resampling.LANCZOS)
        temp_png = os.path.join(output_dir, 'temp_for_svg.png')
        high_res.save(temp_png, 'PNG')
        
        svg_path = os.path.join(output_dir, 'favicon.svg')
        create_svg_from_png(temp_png, svg_path)
        
        # Clean up temp file
        os.remove(temp_png)
        print(f"✓ Created: favicon.svg")
    except Exception as e:
        print(f"✗ Error creating favicon.svg: {e}")
    
    # Generate manifest.json
    try:
        manifest_content = '''{
\t"name": "Website Favicon",
\t"icons": [
\t\t{
\t\t\t"src": "/images/favicon-192x192.png",
\t\t\t"sizes": "192x192",
\t\t\t"type": "image/png"
\t\t},
\t\t{
\t\t\t"src": "/images/favicon-512x512.png",
\t\t\t"sizes": "512x512",
\t\t\t"type": "image/png"
\t\t}
\t]
}'''
        manifest_path = os.path.join(output_dir, 'manifest.json')
        with open(manifest_path, 'w') as f:
            f.write(manifest_content)
        print(f"✓ Created: manifest.json")
    except Exception as e:
        print(f"✗ Error creating manifest.json: {e}")
    
    print(f"\n🎉 Favicon generation complete!")
    print(f"📁 Output directory: {output_dir}")
    print(f"\nGenerated files:")
    print(f"  - favicon.ico (multi-size)")
    print(f"  - favicon.svg")
    print(f"  - favicon-32x32.png")
    print(f"  - favicon-192x192.png")
    print(f"  - favicon-512x512.png")
    print(f"  - apple-touch-icon-180x180.png")
    print(f"  - manifest.json")
    
    return True

def main():
    """Main function"""
    # Parse command line arguments
    if len(sys.argv) == 3:
        input_path = sys.argv[1]
        output_dir = sys.argv[2]
    elif len(sys.argv) == 2:
        input_path = sys.argv[1]
        output_dir = "../images"
    else:
        input_path = "favicon.png"
        output_dir = "../images"
    
    print("🎨 Favicon Generator")
    print("=" * 40)
    print(f"📥 Input: {input_path}")
    print(f"📤 Output: {output_dir}")
    print("=" * 40)
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"✗ Error: Input file '{input_path}' not found!")
        print(f"\nUsage:")
        print(f"  python {sys.argv[0]} [input_image] [output_dir]")
        print(f"  python {sys.argv[0]} favicon.png ../images")
        print(f"  python {sys.argv[0]} my_icon.png /path/to/output")
        return 1
    
    # Generate favicons
    success = generate_favicons(input_path, output_dir)
    
    if success:
        print(f"\n💡 Next steps:")
        print(f"1. Copy the generated files to your website's images directory")
        print(f"2. Update your HTML <head> section with favicon links")
        print(f"3. Clear browser cache to see changes")
        return 0
    else:
        print(f"\n✗ Favicon generation failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())