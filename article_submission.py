
"""
Handles article submissions to the database.

Functions:
article_submission(): Gathers user inputs for article attributes and adds the new article to the database.
Importantly, this module works with others like `get_next_article_id` and `magazine_selection` to enhance the submission process.
"""

from get_next_article_id import get_next_article_id
from input_validation import get_input_with_validation
from magazine_selection import get_magazine_id
from edition_validation import get_edition_input
from release_date_validation import get_valid_release_date
from author_processing import get_author_id
from photographer_processing import get_photographer_id


import mysql.connector
from datetime import datetime


# Define your database credentials
db_config = {
    "host": "data.estio.training",
    "user": "Oliver_Mahwing",
    "password": "Green_05!!",
    "database": "olim_spec_house3"
}

def article_submission():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            print("Connected to the MySQL database")

            cursor = conn.cursor()

            # Prompt the user for article information
            is_test_submission = input("Is this a test submission? (Y/N): ").strip().lower() == 'y'
            article_id = get_next_article_id(cursor, is_test_submission)
            article_name = get_input_with_validation(cursor, "Enter article name: ", "ArticleID", "Articles", 100)
            short_title = get_input_with_validation(cursor, "Enter short title: ", "ShortTitle", "Articles", 150)
            # is_test_submission = test_submission.lower() in ["y", "yes"]
            magazine_id = get_magazine_id(cursor, is_test_submission)
            #  magazine_id = input("Enter Magazine ID (e.g., M1, M2, M3, M4): ")
            edition = get_edition_input()
            release_date = get_valid_release_date()
            # release_date = input("Enter release date (YYYY-MM-DD): ")

            # author_name = input("Enter the author's name (or type 'exit' to stop): ")
            # inhouse_author = input("Is the author in-house? (Y/N): ")
            author_details = get_author_id(cursor)

            if not author_details:
                print("Article submission process terminated.")
                return

            author_type, author_id = author_details

            freelancer_author_id = None
            permanent_staff_author_id = None

            if author_type == 'Freelancer':
                freelancer_author_id = author_id
                inhouse_author = 'N'
            elif author_type == 'Staff':
                permanent_staff_author_id = author_id
                inhouse_author = 'Y'

            # freelancer_author_id = input("Enter Freelancer Author ID or 'NULL': ")
            # permanent_staff_author_id = input("Enter Permanent Staff Author ID or 'NULL': ")

            photographer_type, photographer_id = get_photographer_id(cursor)

            if not photographer_id:
                print("Article submission process terminated.")
                return

            freelancer_photographer_id = None
            permanent_staff_photographer_id = None

            if photographer_type == 'Freelancer':
                freelancer_photographer_id = photographer_id
            elif photographer_type == 'Staff':
                permanent_staff_photographer_id = photographer_id

            # inhouse_photos = input("Are the photos in-house? (Y/N): ")
            # freelancer_photographer_id = input("Enter Freelancer Photographer ID or 'NULL': ")
            # permanent_staff_photographer_id = input("Enter Permanent Staff Photographer ID or 'NULL': ")

            filename = input("Enter Filename: ")

            # Get today's date
            upload_date = datetime.now().date()

            if photographer_type == 'Freelancer':
                inhouse_photos = 'N'
            elif photographer_type == 'Staff':
                inhouse_photos = 'Y'

            # Insert the article into the database
            insert_query = """
            INSERT INTO Articles (
                ArticleID, ArticleName, ShortTitle, MagazineID, Edition, ReleaseDate,
                InhouseAuthor, FreelancerAuthorID, PermanentStaffAuthorID, InhousePhotos,
                FreelancerPhotographerID, PermanentStaffPhotographerID, UploadDate, Filename
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                article_id, article_name, short_title, magazine_id, edition, release_date,
                inhouse_author, freelancer_author_id, permanent_staff_author_id, inhouse_photos,
                freelancer_photographer_id, permanent_staff_photographer_id, upload_date, filename
            )
            cursor.execute(insert_query, data)

            # Commit the changes and close the connection
            conn.commit()
            cursor.close()
            conn.close()

            print("Article submitted successfully.")

    except mysql.connector.Error as e:
        print(f"Error connecting to the MySQL database: {e}")

# To submit an article, call the function
article_submission()
