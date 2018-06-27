"""
Author: Jeff Wilson
Start Date: 6/27/2018

This python file hosts the display functions and UX improvements utilized by the main script.

"""


def print_intro_instructions():
    print("--- Water Marked Image Generator Script ---\n")
    print("Author: Jeff Wilson\n")
    print("This script can apply a user specified watermark template to another image and save it to a subfolder.\n")


def display_time_elapsed(start, end):
    print("\nTOTAL SCRIPT RUN TIME:", (end - start), "seconds")