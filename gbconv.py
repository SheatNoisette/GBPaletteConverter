#!/usr/bin/env python3

"""
    Simple GameBoy - style image converter
"""

from PIL import Image
import sys, math, os

# Hex to RGB
def hex2rgb(hexa):
    """ Convert hexadecimal encoded color to rgb tuple """
    # Remove # at the beginning
    hexa = hexa.lstrip("#")
    return tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))

# Check args
if len(sys.argv) != 3:
    print("Usage:\n"+sys.argv[0]+" (inputimage) (outputimage)")
    sys.exit(1)

# Check if file exists
if not os.path.exists(sys.argv[1]):
    print("Input image not found")
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print("Output image path not given")
    sys.exit(1)

#Simple GB palette - https://lospec.com/palette-list/kirokaze-gameboy
palette = ["#332c50", "#46878f", "#94e344", "#e2f3e4"]
palette_rgb = [hex2rgb(e) for e in palette]

# Load image
img = Image.open(sys.argv[1])
# Load content into memory
img_content = img.load()
# Get image size
imgX, imgY = img.size
# Out image
output_img = Image.new("RGB", (imgX, imgY))
# Content of output
output_content = output_img.load()

for y in range(0, imgY):
    for x in range(0, imgX):
        _r, _g, _b = img_content[x, y]

        # Maximum diff
        diff = 256
        min_index = 0

        # Try every color on the palette and try to find the closest color
        for index in range(len(palette_rgb)):
            current_diff = math.sqrt(
                (_r - palette_rgb[index][0])**2 + 
                (_g - palette_rgb[index][1])**2 +
                (_b - palette_rgb[index][2])**2)

            if current_diff < diff:
                diff = current_diff
                min_index = index

        output_content[x, y] = palette_rgb[min_index]

# Save final image
output_img.save(sys.argv[2])
