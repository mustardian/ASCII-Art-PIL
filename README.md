# ASCII Art Generator

A Python-based tool to convert images into ASCII art with adjustable styles and parameters.

## Features

- Converts images to ASCII art.
- Adjustable output width.
- Multiple styles: **default**, **blocky**, **minimal**.
- Contrast and invert options for customization.

## Requirements

- Python 
- Required libraries:
  - Pillow
  - numpy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mustardian/ascii-art-pil.git
   cd ascii-art-generator
   ```
2. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your image in the project folder.
2. Run the script with your desired parameters:
   ```bash
   python ascii-art.py
   ```
3. Adjust the parameters at the top of the script:

- image_path: Path to your image file.
- output_width: Width of the ASCII art (default: 80).
- style: Choose from default, blocks, or minimal.
- contrast_scale: Adjust contrast (default: 1.0).
- invert: Set to True to invert brightness mapping.

## Example usage:

```python
from ascii_art import AsciiArtGenerator
'''
Needs to be same folder or under modules in your python folder to use 
'''
generator = AsciiArtGenerator(
    image_path="path_to_your_image.jpg",
    output_width=100,
    style="blocks",
    contrast_scale=1.2,
    invert=False
)
ascii_art = generator.generate_ascii()
print(ascii_art)
```

## Styles:
1. Default: Detailed, using characters like @%#*+=-:. .
2. Blocky: Bold, blocky characters like █▓▒░ .
3. Minimal: High contrast with fewer characters like @. .