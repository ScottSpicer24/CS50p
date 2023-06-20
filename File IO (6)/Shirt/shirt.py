'''
In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after
resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt with Image.paste,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like these demos, so that,
when they’re resized and cropped, the shirt appears to fit perfectly.
'''

import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit()

try:
    file_name1, file_type = sys.argv[1].split('.')
    file_type = file_type.strip().lower()
    if file_type != 'jpg' and file_type != 'jepg' and file_type != 'png':
        sys.exit()

    file_name1, file_type2 = sys.argv[2].split('.')
    file_type2 = file_type2.strip().lower()
    if file_type2 != 'jpg' and file_type2 != 'jepg' and file_type2 != 'png':
        sys.exit()

    if file_type != file_type2:
        sys.exit()
except FileNotFoundError:
    sys.exit()

try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit()

size = shirt.size
photo = Image.open(sys.argv[1])
muppet = ImageOps.fit(photo, size)
muppet.paste(shirt, shirt)
muppet.save(sys.argv[2])