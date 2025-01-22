from PIL import Image
import numpy as np

class AsciiArtGenerator:
    def __init__(self, image_path, output_width=100, style="default", contrast_scale=1.0, invert=False):
        self.image_path = image_path
        self.output_width = output_width
        self.contrast_scale = contrast_scale
        self.invert = invert
        self.styles = {
            "default": "@%#*+=-:. ",
            "blocky": "█▓▒░ ",
            "minimal": "@. ",
        }

        if style not in self.styles:
            raise ValueError(f"Invalid style '{style}'. Choose from {list(self.styles.keys())}.")
        
        self.charset = self.styles[style]

        if self.invert:
            self.charset = self.charset[::-1]

    def _resize_image(self, img):
        """Resize w maintaining aspect ratio."""
        aspect_ratio = img.height / img.width
        new_height = int(self.output_width * aspect_ratio * 0.55)
        return img.resize((self.output_width, new_height))
    
    def _map_pixels_to_ascii(self, img):
        """Pixel to ascii"""
        pixels = np.array(img, dtype=np.float32) * self.contrast_scale
        pixels = np.clip(pixels, 0, 255)
        normalized_pixels = (pixels / 255.0) * (len(self.charset) - 1)
        ascii_art = np.array([self.charset[int(val)] for val in normalized_pixels.flatten()])
        return ascii_art
    
    def generate_ascii(self):
        """Put everything together."""
        img = Image.open(self.image_path).convert("L")
        img_resized = self._resize_image(img)
        ascii_art = self._map_pixels_to_ascii(img_resized)
        
        # Reshaper
        ascii_art = ascii_art.reshape((img_resized.height, img_resized.width))
        return "\n".join("".join(row) for row in ascii_art)
