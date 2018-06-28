"""
Author: Jeff Wilson
Start Date: 6/27/2018

This python file hosts the functions used for manipulating files in the OS. (Utilized by main script)

"""

import os
import shutil


def delete_images(folder_path):

    delete_path = folder_path + "resized/"
    if os.path.exists(delete_path):
        print("\nDeleting directory at path: ", delete_path)
        try:
            shutil.rmtree(delete_path)
        except OSError:
            print("\nFatal Error! Unable to delete unwanted filed at path: ", delete_path)

