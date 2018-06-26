"""
Author: Jeff Wilson
Date: 6/25/2018

This script applies a Watermark Template/Image (User Specified Path) on to the Original Image (User Specified Path) and
saves it to a subfolder of the original image path. The user also has the option to resize their original image
before adding the watermark.

"""

import os
from PIL import Image

base_images_folder_path = None


def print_intro_instructions():
    print("--- Water Marked Image Generator Script ---\n")
    print("Author: Jeff Wilson\n")
    print("This script will apply a user specified watermark template to another image and save it to a subfolder.\n")


def resize_images(folder_path):

    resized_images_save_path = folder_path + "/resized/"

    # Create subfolder in folder path for storing resized images
    if not os.path.exists(resized_images_save_path):
        os.makedirs(resized_images_save_path)
        print("\nDirectory created at: ", resized_images_save_path, " This path will be used for saving.\n")

    else:
        print("\nPath already exists at: ", resized_images_save_path, " This path Will be used for saving.\n")

    w_dim = int(input("Enter the new width (px): "))
    h_dim = int(input("Enter the new height (px): "))

    suffix = input("Enter a suffix to be added to the file. "
                   "Make sure it is unique to the folder, otherwise files may be written over: ")

    # Iterate through items in base images folder
    print("\nImages to be resized:\n")
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            print(os.path.join(folder_path, filename))

    proceed = input("Continue? [Y/N]")
    if proceed == "Y" or proceed == "y":
        print("Images are now being resized. This may take some time...")
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                # Resize current image and save to resized_images_save_path
                img = Image.open(folder_path + "/" + filename)
                img_resized = img.resize((w_dim, h_dim), Image.LANCZOS)
                img_resized.save((resized_images_save_path + filename[:-4] + "_" + suffix + str(w_dim) + "x" +
                                  str(h_dim) + '.jpg'), "JPEG")

    if proceed == "Y" or proceed == "y":
        print("\nAll images have been resized to", w_dim, "X", h_dim, "and saved to path: ",
              resized_images_save_path)

    if proceed == "N" or proceed == "n":
        print("\nResizing Process aborted!")
        try:
            os.rmdir(resized_images_save_path)
            print("Deleted last directory in path: ", resized_images_save_path)
        except OSError:
            print("Error: Could not delete directory at: ", resized_images_save_path, "Ensure the folder is empty.")


# Once all images have been resized, set base_images_folder_path to the resized images location

    global base_images_folder_path
    base_images_folder_path = resized_images_save_path


def add_watermark(base_folder_path, water_mark_path):
    watermark_template = Image.open(water_mark_path)

    watermarked_images_save_path = base_folder_path + "/watermarked/"

    # Create subfolder in folder path for storing resized images
    if not os.path.exists(watermarked_images_save_path):
        os.makedirs(watermarked_images_save_path)
        print("\nDirectory created at: ", watermarked_images_save_path, " This path will be used for saving.\n")

    else:
        print("\nPath already exists at: ", watermarked_images_save_path, " This path Will be used for saving.\n")

    suffix = input("Enter a suffix to be added to the file. "
                   "Make sure it is unique to the folder, otherwise files may be written over: ")

    print("Images are now being resized. This may take some time...")

    for filename in os.listdir(base_folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                # Resize current image and save to resized_images_save_path
                img = Image.open(base_folder_path + "/" + filename)
                img.paste(watermark_template, (0, 0), watermark_template)
                img.save((watermarked_images_save_path + filename[:-4] + "_" + suffix + '.jpg'), "JPEG")

    print("\nAll supplied images have been watermarked and saved to path: ", watermarked_images_save_path)


###########################################
# Entry point for running the script (main)
###########################################


print_intro_instructions()

base_images_folder_path = input("Enter the path to your base images folder: ")
while not os.path.exists(base_images_folder_path):
    print("Invalid File Path! Ensure the directory is written correctly and is not empty.")
    base_images_folder_path = input("Enter the path to your base images folder: ")


print("\nBase Image Directory Found Successfully: ", base_images_folder_path, "\n")

request = input("It is HIGHLY RECOMMENDED that your base image and watermark template are the same size. "
                "Would you like to resize your base image[Y/N]: ")

if request == "Y" or request == "y":
    resize_images(base_images_folder_path)
    request = None

watermark_template_image_path = input("\nEnter the path to your watermark template: ")
while not os.path.exists(watermark_template_image_path):
    print("Invalid File Path! Ensure the directory is written correctly and is not empty.")
    watermark_template_image_path = input("Enter the path to your watermark template (image): ")

print("\nWatermark template successfully found at: ", watermark_template_image_path)
print("Base image directory: ", base_images_folder_path)

# TODO Add watermark with function

request = input("\nWould you like to add a watermark to your images located in the above base directory[Y/N]: ")


if request == "Y" or request == "y":
    add_watermark(base_images_folder_path, watermark_template_image_path)
    request = None
else:
    request = input("Would you like to specify another path[Y/N]: ")
    if request == "Y" or request == "y":
        add_watermark(base_images_folder_path, watermark_template_image_path)
        request = None
    else:
        print("\nThank you for using this script!")


print("\nThank you for using this script!")


##############################################
# End of script
##############################################
