"""
This module provides validation for article edition input.
It ensures that the edition is a number within the range of 1 to 9999.
"""

import mysql.connector

def get_edition_input():
    """
    Prompt the user to enter an edition number.
    The edition should be a number in the range 1 to 9999.
    """
    while True:
        edition = input("Enter magazine edition (1-9999): ")
        if edition.isdigit() and 1 <= int(edition) <= 9999:
            return edition
        print("Invalid edition. Please enter a number between 1 and 9999.")
