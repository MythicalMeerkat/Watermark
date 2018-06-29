"""
Author: Jeff Wilson
Start Date: 6/27/2018

This python file hosts the watermarking functions utilized by the main script.

"""


from PIL import Image
import os


def add_watermark(base_folder_path, water_mark_path):
    try:
        watermark_template = Image.open(water_mark_path)
    except PermissionError:
        print("Fatal Error! Cannot Access Template, please check your system permissions!")
        return None

    reading_path = base_folder_path + "resized/"
    watermarked_images_save_path = base_folder_path + "watermarked/"

    # Create subfolder in folder path for storing resized images
    if not os.path.exists(watermarked_images_save_path):
        os.makedirs(watermarked_images_save_path)
        print("\nDirectory created at: ", watermarked_images_save_path, " This path will be used for saving.\n")

    else:
        print("\nPath already exists at: ", watermarked_images_save_path, " This path Will be used for saving.\n")

    print("Image(s) are now being watermarked. This may take some time...")
    image_count = 0
    for filename in os.listdir(reading_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                # Resize current image and save to resized_images_save_path
                img = Image.open(reading_path + filename)
                img.paste(watermark_template, (0, 0), watermark_template)
                img.save((watermarked_images_save_path + filename[:-4] + '.jpg'), "JPEG")
                image_count += 1
            if filename.endswith(".png"):
                # Resize current image and save to resized_images_save_path
                img = Image.open(reading_path + filename)
                img.paste(watermark_template, (0, 0), watermark_template)
                img.save((watermarked_images_save_path + filename[:-4] + '.png'))
                image_count += 1

    print(image_count, "image(s) have been watermarked and saved to path: ", watermarked_images_save_path)

    return None
