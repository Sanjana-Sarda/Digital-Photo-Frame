#Program to convert bitmap images into bitmap image blocks for use in the Pico ePaper 7.5" display

from PIL import Image

import os

def batch_process_images(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    # Get a list of files in the input folder
    input_files = os.listdir(input_folder)
    
    # Iterate over the files in the input folder
    for filename in input_files:
    # Open the image
        image = Image.open(os.path.join(input_folder, filename))

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
                try:
                    os.mkdir(os.path.join(output_folder+"/"+filename[:-4]))
                except:
                    pass
                img.save(os.path.join(output_folder+"/"+filename[:-4], f'image_{i}_{j}.bmp'))
        
# Specify the input and output folders
input_folder = "output"
output_folder = "bmp" 

# Call the batch_process_images function
batch_process_images(input_folder, output_folder)