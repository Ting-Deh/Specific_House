import mysql.connector

def get_photographer_id(cursor):
    """
    Prompts the user for the photographer's name and determines whether the photographer is a freelancer or permanent staff.
    Returns the appropriate photographer ID, or None if the photographer is not found in the database.
    """
    while True:
        photographer_name = input("Enter the photographer's name (or type 'exit' to stop): ").strip().title()

        if photographer_name.lower() == 'exit':
            print("Article submission process stopped by the user.")
            print("If the photographer is not registered, please contact support.")
            return None

        # Check the Freelancers table for photographers
        query = "SELECT FreelancerID FROM Freelancers WHERE Name = %s AND Role = 'Photographer'"
        cursor.execute(query, (photographer_name,))
        freelancer_id = cursor.fetchone()

        if freelancer_id:
            return ('Freelancer', freelancer_id[0])

        # Check the PermanentStaff table for photographers
        query = "SELECT StaffID FROM PermanentStaff WHERE Name = %s AND Role = 'Photographer'"
        cursor.execute(query, (photographer_name,))
        staff_id = cursor.fetchone()

        if staff_id:
            return ('Staff', staff_id[0])

        # If I reach here, the photographer was not found in either table
        print(f"Photographer '{photographer_name}' not found in the database.")
        choice = input(
            "Would you like to try again, or stop the article submission process? (try/stop): ").strip().lower()
        if choice == 'stop':
            print("If the photographer is not registered, please contact support.")
            return None
