from datetime import datetime
import mysql.connector

def get_valid_release_date():
    """
    Prompt the user for a valid release date in the format YYYY-MM-DD.
    """
    while True:
        date_input = input("Enter release date (YYYY-MM-DD): ")
        try:
            # Try to convert the input into a datetime object. If successful, it's a valid date.
            valid_date = datetime.strptime(date_input, '%Y-%m-%d').date()
            return valid_date
        except ValueError:
            # If the conversion fails, it means the date format is wrong.
            print("Invalid date format. Please enter a valid date in the format YYYY-MM-DD.")
