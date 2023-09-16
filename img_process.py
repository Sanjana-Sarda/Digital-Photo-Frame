from PIL import Image, ImageOps, ImageFilter
import os

def batch_process_images(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of files in the input folder
    input_files = os.listdir(input_folder)

    # Iterate over the files in the input folder
    for filename in input_files:
        # Load the image
        img = Image.open(os.path.join(input_folder, filename))

        # Resize the image to 800x480
        img = img.resize((800, 480), Image.Resampling.LANCZOS)

        # Convert the image to grayscale
        img = ImageOps.grayscale(img)

        # Apply Floyd-Steinberg dithering
        img = img.convert("1", dither=Image.Dither.FLOYDSTEINBERG)

        # Save the image as PBM
        img.save(os.path.join(output_folder, filename.split('.')[0] + ".pbm"))

# Specify the input and output folders
input_folder = "input"
output_folder = "output"

# Call the batch_process_images function
batch_process_images(input_folder, output_folder)
