
"""
This module contains a function to validate user input for ArticleName and ShortTitle based on:
1. Uniqueness in the database.
2. Input length.

The function interacts with the database to ensure the inputted value doesn't already exist in a specified column.
Additionally, it checks if the input adheres to a specified maximum length.
"""

import mysql.connector

def get_input_with_validation(cursor, prompt, column_name, table_name, max_length):

    while True:
        value = input(prompt)

        # Check length of the input
        if len(value) > max_length:
            print(f"Your input is too long. Please enter a value less than {max_length} characters.")
            continue

        # Check for uniqueness in the database
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = %s"
        try:
            cursor.execute(query, (value,))
            count = cursor.fetchone()[0]
            print(f"Count for {value} in {column_name}: {count}")
            if count > 0:
                print(f"The {column_name} '{value}' already exists. Please enter a unique value.")
            else:
                return value
        except Exception as e:
            print(f"Error checking uniqueness of {value}: {e}")
            continue
