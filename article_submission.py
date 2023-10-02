from get_next_article_id import get_next_article_id
from input_validation import get_input_with_validation

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
            magazine_id = input("Enter Magazine ID (e.g., M1, M2, M3, M4): ")
            edition = input("Enter edition: ")
            release_date = input("Enter release date (YYYY-MM-DD): ")

            inhouse_author = input("Is the author in-house? (Y/N): ")
            freelancer_author_id = input("Enter Freelancer Author ID or 'NULL': ")
            permanent_staff_author_id = input("Enter Permanent Staff Author ID or 'NULL': ")

            inhouse_photos = input("Are the photos in-house? (Y/N): ")
            freelancer_photographer_id = input("Enter Freelancer Photographer ID or 'NULL': ")
            permanent_staff_photographer_id = input("Enter Permanent Staff Photographer ID or 'NULL': ")

            filename = input("Enter Filename: ")

            # Get today's date
            upload_date = datetime.now().date()

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

# To submit an article, simply call the function
article_submission()
