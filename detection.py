from PIL import Image, ImageFilter
import os
from image_functions import ImageFunctions

# --- Parameters ---

# Image path
path = "./images/beach.jpg"

# Output image path
outputPath = "./images/edges.png"

# Increase to reduce noise
blurRadius = 0.0

# Apply sobel detection to a greyscale version of the image (generally using colour has less noise)
greyScale = True

# ------------------

imageFunctions = ImageFunctions(blurRadius, greyScale)

if (os.path.exists(outputPath)):
    os.remove(outputPath)

img = imageFunctions.detectEdges(Image.open(path))

img.show()
img.save(outputPath)
