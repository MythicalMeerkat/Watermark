"""
Author: Jeff Wilson
Start Date: 6/25/2018

This script can a Watermark Template/Image (User Specified Path) on to the Original Image (User Specified Path) and
saves it to a subfolder of the original image path. The user also has the option to resize their original image
before adding the watermark.

"""

import os
import time
from src import display_functions
from src import resizing_functions
from src import watermarking_functions
from src import os_functions

###########################################
# Entry point for running the script (main)
###########################################

# Print Script Header

display_functions.print_intro_instructions()

# Get Base Images Folder

base_images_folder_path = input("Enter the path to your base images folder: ")
while not os.path.exists(base_images_folder_path):
    print("Invalid File Path! Ensure the directory is written correctly and is not empty.")
    base_images_folder_path = input("Enter the path to your base images folder: ")


print("\nBase Image Directory Found Successfully: ", base_images_folder_path, "\n")
resize_request = False
watermark_request = False
delete_request = False

# Does the user want to resize images?

request = input("Your base image and watermark template MUST BE THE SAME SIZE, if you choose to add one. "
                "Would you like to resize your base images[Y/N]: ")

if request == "Y" or request == "y":
    resize_request = True
    request = None
    print("Script will resize images.")
else:
    print("Script will not resize images.")

# Does the user want to keep their resized images once the script is over?

request = input("\nWould you like to DELETE the resized images once the script is finished[Y/N]: ")
if request == "Y" or request == "y":
        delete_request = True
if request == "N" or request == "n":
    pass
else:
    print("Unexpected input, keeping images.")


# Does the user want to watermark images?

request = input("\nWould you like to add a watermark to your images[Y/N]: ")
if request == "Y" or request == "y":
    watermark_request = True
    watermark_template_image_path = input("\nEnter the path to your watermark "
                                          "template (including file name and extension): ")
    while not os.path.exists(watermark_template_image_path):
        print("Invalid File Path! Ensure the directory is written correctly and is not empty.")
        watermark_template_image_path = input("Enter the path to your watermark template (image): ")

    print("Watermark path SUCCESSFULLY found at:", watermark_template_image_path, "\n")
else:
    print("Images will not be watermarked.")

# The user wants to do some sort of file manipulation, therefore we should specify a directory name.

if resize_request or watermark_request:
    directory_name = input("Enter a directory name for the images. "
                           "Make sure it is a unique suffix, otherwise already existing files may be written over: ")

# We will resize and watermark images

if resize_request and watermark_request:
    print("\nWatermark template path: ", watermark_template_image_path)
    print("\nBASE IMAGE DIRECTORY: ", base_images_folder_path)
    request = None
    request = input("Are you sure you want to add a watermark to your images "
                    "located in the above base directory[Y/N]: ")
    if request == "Y" or request == "y":
        start = time.time()
        watermark_images_save_path = resizing_functions.resize_images(base_images_folder_path, directory_name)
        watermarking_functions.add_watermark(watermark_images_save_path, watermark_template_image_path)
        request = None
        if delete_request:
            os_functions.delete_images(watermark_images_save_path)
        end = time.time()
    else:
        request = input("Would you like to specify another base path[Y/N]: ")
        if request == "Y" or request == "y":
            start = time.time()
            watermark_images_save_path = resizing_functions.resize_images(base_images_folder_path, directory_name)
            watermarking_functions.add_watermark(watermark_images_save_path, watermark_template_image_path)
            request = None
            if delete_request:
                os_functions.delete_images(watermark_images_save_path)
            end = time.time()
        else:
            print("\nThank you for using this script!")

# We will resize images only

if resize_request and not watermark_request:
    print("\nBASE IMAGE DIRECTORY: ", base_images_folder_path)
    request = None
    request = input("Are you sure you want to resize your images "
                    "located in the above base directory[Y/N]: ")
    if request == "Y" or request == "y":
        start = time.time()
        watermark_images_save_path = resizing_functions.resize_images(base_images_folder_path, directory_name)
        request = None
        end = time.time()
    else:
        print("\nResizing Process Aborted!")

# We will watermark images only

if watermark_request and not resize_request:
    print("\nBASE IMAGE DIRECTORY: ", base_images_folder_path)
    request = None
    request = input("Are you sure you want to watermark your images "
                    "located in the above base directory[Y/N]: ")
    if request == "Y" or request == "y":
        start = time.time()
        watermarking_functions.add_watermark(base_images_folder_path, watermark_template_image_path)
        request = None
        end = time.time()
    else:
        print("\nWatermarking Process Aborted!")

# We chose not to utilize the script; therefore the total script run time is 0

if not resize_request and not watermark_request:
    start = 0
    end = 0


# Display the total script Run time
display_functions.display_time_elapsed(start, end)

print("\nThank you for using this script!")


##############################################
# End of script
##############################################
