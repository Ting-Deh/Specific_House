import mysql.connector


def get_author_id(cursor):
    """
    Prompts the user for the author's name and determines whether the author is a freelancer or permanent staff.
    Returns the appropriate author ID, or None if the author is not found in the database.
    """
    while True:
        author_name = input("Enter the author's name (or type 'exit' to stop): ").strip()

        if author_name.lower() == 'exit':
            print("Article submission process stopped by the user.")
            return None

        # Check the Freelancers table
        query = "SELECT FreelancerID FROM Freelancers WHERE LOWER(Name) = LOWER(%s)"
        cursor.execute(query, (author_name,))
        freelancer_id = cursor.fetchone()

        if freelancer_id:
            return ('Freelancer', freelancer_id[0])

        # Check the PermanentStaff table
        query = "SELECT StaffID FROM PermanentStaff WHERE LOWER(Name) = LOWER(%s)"
        cursor.execute(query, (author_name,))
        staff_id = cursor.fetchone()

        if staff_id:
            return ('Staff', staff_id[0])

        # If we reach here, the author was not found in either table
        print(f"Author '{author_name}' not found in the database.")
        while True:
            choice = input(
                "Would you like to try again, or stop the article submission process? (try/stop): ").strip().lower()
            if choice == 'stop':
                print("If this is a new author, please contact support to register them in the system.")
                return None
            elif choice == 'try':
                break
            else:
                print("Invalid choice. Please enter 'try' to continue or 'stop' to exit.")


