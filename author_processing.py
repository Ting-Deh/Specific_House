import mysql.connector

def get_author_id(cursor):
    """
    Prompts the user for the author's name and determines whether the author is a freelancer or permanent staff.
    Returns the appropriate author ID, or None if the author is not found in the database.
    """
    author_name = input("Enter the author's name: ").strip()

    # Check the Freelancers table
    query = "SELECT FreelancerID FROM Freelancers WHERE AuthorName = %s"
    cursor.execute(query, (author_name,))
    freelancer_id = cursor.fetchone()

    if freelancer_id:
        return ('Freelancer', freelancer_id[0])

    # Check the PermanentStaff table
    query = "SELECT StaffID FROM PermanentStaff WHERE AuthorName = %s"
    cursor.execute(query, (author_name,))
    staff_id = cursor.fetchone()

    if staff_id:
        return ('Staff', staff_id[0])

    # If we reach here, the author was not found in either table
    print(f"Author '{author_name}' not found in the database. Please register the author first.")
    return None
