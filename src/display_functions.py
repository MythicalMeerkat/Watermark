"""
Author: Jeff Wilson
Start Date: 6/27/2018

This python file hosts the display functions and UX improvements utilized by the main script.

"""


def print_intro_instructions():
    print("--- Water Marked Image Generator Script ---")
    print("Author: Jeff Wilson\n")
    print("This script can apply a user specified watermark template to other images and save it to a subfolder. The"
          " script currently supports .png and .jpg files.\n")

    return None


def display_time_elapsed(start, end):
    print("\nTOTAL SCRIPT RUN TIME:", (end - start), "seconds")

    return None
