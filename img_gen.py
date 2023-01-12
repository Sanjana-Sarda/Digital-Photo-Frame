#Program to convert bitmap images into bitmap image blocks for use in the Pico ePaper 7.5" display

from PIL import Image

# Open the image
image = Image.open('IMG-20200725-WA0000.pbm')

# Get the width and height of the image
width, height = image.size

# Calculate the number of 160x160 images that can be created
rows = height // 160
cols = width // 160

# Create the 160x160 images
for i in range(rows):
    for j in range(cols):
        # Calculate the left, upper, right, and lower coordinates of the image
        left = j * 160
        upper = i * 160
        right = left + 160
        lower = upper + 160
        # Crop the image
        img = image.crop((left, upper, right, lower))
        # Save the image
        img.save(f'image_{i}_{j}.bmp')