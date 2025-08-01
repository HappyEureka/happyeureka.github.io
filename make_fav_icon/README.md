# Favicon Generator

This script converts a single PNG image into all the favicon formats needed for your website.

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Default usage
Place your `favicon.png` in this directory and run:
```bash
python make_fav_icon.py
```
This will output all favicon files to `../images/` directory.

### Method 2: Custom input file
```bash
python make_fav_icon.py your_icon.png
```

### Method 3: Custom input and output
```bash
python make_fav_icon.py your_icon.png /path/to/output/directory
```

## Generated Files

The script will create:
- `favicon.ico` (16x16, 32x32, 48x48 multi-size)
- `favicon.svg` (scalable vector format)
- `favicon-32x32.png`
- `favicon-192x192.png` 
- `favicon-512x512.png`
- `apple-touch-icon-180x180.png`
- `manifest.json`

## Tips

- Use a high-resolution PNG (at least 512x512) for best results
- Make sure your image has a transparent background if needed
- The script will automatically resize and optimize all formats
- Clear your browser cache after updating favicons to see changes

## Example

```bash
# Place favicon.png in this directory
python make_fav_icon.py

# Or specify a different source image
python make_fav_icon.py my_logo.png ../images
```
