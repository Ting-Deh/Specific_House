import mysql.connector

def get_photographer_id(cursor):
    """
    Prompts the user for the photographer's name and determines whether the photographer is a freelancer or permanent staff.
    Returns the appropriate photographer ID, or None if the photographer is not found in the database.
    """
    while True:
        photographer_name = input("Enter the photographer's name (or type 'exit' to stop): ").strip()

        if photographer_name.lower() == 'exit':
            print("Article submission process stopped by the user.")
            print("If the photographer is not registered, please contact support.")
            return None, None

        # Check the Freelancers table for photographers
        query = "SELECT FreelancerID FROM Freelancers WHERE LOWER(Name) = LOWER(%s)"
        cursor.execute(query, (photographer_name,))
        freelancer_id = cursor.fetchone()

        if freelancer_id:
            return 'Freelancer', freelancer_id[0]

        # Check the PermanentStaff table for photographers
        query = "SELECT StaffID FROM PermanentStaff WHERE LOWER(Name) = LOWER(%s)"
        cursor.execute(query, (photographer_name,))
        staff_id = cursor.fetchone()

        if staff_id:
            return 'Staff', staff_id[0]

        # If we reach here, the photographer was not found in either table
        print(f"Photographer '{photographer_name}' not found in the database.")
        while True:
            choice = input(
                "Would you like to try again, or stop the article submission process? (try/stop): ").strip().lower()
            if choice == 'stop':
                print("If this is a new photographer, please contact support to register them in the system.")
                return None, None
            elif choice == 'try':
                break
            else:
                print("Invalid choice. Please enter 'try' to continue or 'stop' to exit.")

