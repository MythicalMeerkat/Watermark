"""
Author: Jeff Wilson
Start Date: 6/27/2018

This python file hosts the resizing functions utilized by the main script.

"""

from PIL import Image
import os


def resize_images(folder_path, file_suffix):

    resized_images_save_path = folder_path + "/resized/"

    # Create subfolder in folder path for storing resized images
    if not os.path.exists(resized_images_save_path):
        os.makedirs(resized_images_save_path)
        print("\nDirectory created at: ", resized_images_save_path, " This path will be used for saving.\n")

    else:
        print("\nPath already exists at: ", resized_images_save_path, " This path Will be used for saving.\n")

    w_dim = int(input("Enter the new width of the base images(px): "))
    h_dim = int(input("Enter the new height of the base images(px): "))


# Iterate through items in base images folder
    image_count = 0
    print("\nImages to be copied and worked with:\n")
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            print(os.path.join(folder_path, filename))
            image_count += 1

    print("\nTotal Images: ", image_count)

    proceed = input("Continue? [Y/N]")
    if proceed == "Y" or proceed == "y":
        print("Images are now being resized. This may take some time...\n")
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                # Resize current image and save to resized_images_save_path
                img = Image.open(folder_path + "/" + filename)
                img_resized = img.resize((w_dim, h_dim), Image.LANCZOS)
                img_resized.save((resized_images_save_path + filename[:-4] + "_" + file_suffix + str(w_dim) + "x" +
                                  str(h_dim) + '.jpg'), "JPEG")
            if filename.endswith(".png"):
                img = Image.open(folder_path + "/" + filename)
                img_resized = img.resize((w_dim, h_dim), Image.LANCZOS)
                img_resized.save((resized_images_save_path + filename[:-4] + "_" + file_suffix + str(w_dim) + "x" +
                                  str(h_dim) + '.png'))

    if proceed == "Y" or proceed == "y":
        print(image_count, "images have been resized to", w_dim, "X", h_dim, "and saved to path: ",
              resized_images_save_path)

    if proceed == "N" or proceed == "n":
        print("\nResizing Process aborted!")
        try:
            os.rmdir(resized_images_save_path)
            print("Deleted last directory in path: ", resized_images_save_path)
        except OSError:
            print("Error: Could not delete directory at: ", resized_images_save_path, "Ensure the folder is empty.")


# Once all images have been resized, return the path to save watermarked images at

    return resized_images_save_path
