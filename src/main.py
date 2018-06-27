"""
Author: Jeff Wilson
Start Date: 6/25/2018

This script applies a Watermark Template/Image (User Specified Path) on to the Original Image (User Specified Path) and
saves it to a subfolder of the original image path. The user also has the option to resize their original image
before adding the watermark.

"""

import os
import time
from src import display_functions
from src import resizing_functions
from src import watermarking_functions

###########################################
# Entry point for running the script (main)
###########################################

display_functions.print_intro_instructions()

base_images_folder_path = input("Enter the path to your base images folder: ")
while not os.path.exists(base_images_folder_path):
    print("Invalid File Path! Ensure the directory is written correctly and is not empty.")
    base_images_folder_path = input("Enter the path to your base images folder: ")


print("\nBase Image Directory Found Successfully: ", base_images_folder_path, "\n")
resize_request = False
watermark_request = False
request = input("It is HIGHLY RECOMMENDED that your base image and watermark template are the same size. "
                "Would you like to resize your base image[Y/N]: ")

if request == "Y" or request == "y":
    resize_request = True
    request = None

request = input("\nWould you like to add a watermark to your images[Y/N]: ")
if request == "Y" or request == "y":
    watermark_request = True
    watermark_template_image_path = input("\nEnter the path to your watermark "
                                          "template (including file name and extension): ")
    while not os.path.exists(watermark_template_image_path):
        print("Invalid File Path! Ensure the directory is written correctly and is not empty.")
        watermark_template_image_path = input("Enter the path to your watermark template (image): ")

    print("Watermark path SUCCESSFULLY found at:", watermark_template_image_path, "\n")

if resize_request or watermark_request:
    suffix = input("Enter a suffix to be added to the file. "
                   "Make sure it is unique to the folder, otherwise files may be written over: ")

if resize_request and watermark_request:
    print("\nWatermark template successfully found at: ", watermark_template_image_path)
    print("Base image directory: ", base_images_folder_path)
    request = None
    request = input("\nAre you sure you want to add a watermark to your images "
                    "located in the above base directory[Y/N]: ")
    if request == "Y" or request == "y":
        start = time.time()
        watermark_images_save_path = resizing_functions.resize_images(base_images_folder_path, suffix)
        watermarking_functions.add_watermark(watermark_images_save_path, watermark_template_image_path, suffix)
        request = None
        end = time.time()
    else:
        request = input("Would you like to specify another base path[Y/N]: ")
        if request == "Y" or request == "y":
            start = time.time()
            watermark_images_save_path = resizing_functions.resize_images(base_images_folder_path)
            watermarking_functions.add_watermark(watermark_images_save_path, watermark_template_image_path, suffix)
            request = None
            end = time.time()
        else:
            print("\nThank you for using this script!")


if resize_request and not watermark_request:
    print("Base image directory: ", base_images_folder_path)
    request = None
    request = input("\nAre you sure you want to resize your images "
                    "located in the above base directory[Y/N]: ")
    if request == "Y" or request == "y":
        start = time.time()
        resizing_functions.resize_images(base_images_folder_path, suffix)
        request = None
        end = time.time()
    else:
        print("\nResizing Process Aborted!")


if watermark_request and not resize_request:
    print("Base image directory: ", base_images_folder_path)
    request = None
    request = input("\nAre you sure you want to watermark your images "
                    "located in the above base directory[Y/N]: ")
    if request == "Y" or request == "y":
        start = time.time()
        watermarking_functions.add_watermark(base_images_folder_path, watermark_template_image_path, suffix)
        request = None
        end = time.time()
    else:
        print("\nWatermarking Process Aborted!")

if not resize_request and not watermark_request:
    start = 0
    end = 0


display_functions.display_time_elapsed(start, end)

print("\nThank you for using this script!")


##############################################
# End of script
##############################################
