
"""
This module contains functions related to the selection of magazines.

The primary function, `get_magazine_id`, improves the user experience by displaying available magazines from the database as a list.
Users can then select a magazine by its corresponding number, ensuring they choose a valid MagazineID.
For test submissions, only the test magazine 'TM1' is displayed.

This approach not only simplifies the magazine selection process but also minimizes potential errors
and the need for users to memorize MagazineIDs.
"""

import mysql.connector

def get_magazine_id(cursor, is_test):
    """
    Prompts the user to select a MagazineID from a list of available magazines.
    If it's a test submission, only 'TM1' will be displayed.
    """

    # If it's a test submission, return 'TM1' immediately
    if is_test:
        print("For test submissions, the magazine ID is automatically set to 'TM1'.")
        return "TM1"

    # Fetch available MagazineIDs from the database
    query = "SELECT MagazineID, MagazineName FROM Magazines WHERE MagazineID NOT LIKE 'TM%'"
    cursor.execute(query)
    magazines = cursor.fetchall()

    # Display available magazines
    print("\nAvailable Magazines:")
    for index, (magazine_id, magazine_name) in enumerate(magazines, 1):
        print(f"{index}. {magazine_name} ({magazine_id})")

    # Get user choice
    while True:
        choice = input("\nSelect a magazine by number: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(magazines):
                return magazines[choice - 1][0]
            print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

