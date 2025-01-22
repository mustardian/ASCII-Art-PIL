from ascii_art import AsciiArtGenerator

generator = AsciiArtGenerator(
    image_path="ame.png",
    output_width=100,
    style="blocky",
    contrast_scale=1.5,
    invert=False 
)

ascii_art = generator.generate_ascii()
print(ascii_art)

# Or maybe write to a file
# with open("ascii_art.txt", "w") as f:
#     f.write(ascii_art)