
"""
This module contains the get_next_article_id function which generates the next unique ArticleID.

Functionality:
1. Determines whether the article submission is a test or a real submission.
2. Queries the database to find the latest ArticleID based on the submission type.
3. Increments the ID to create a new unique ArticleID for the new submission.

For test submissions, the ArticleID format is 'test1', 'test2', etc.
For real submissions, the ArticleID format is 'A1', 'A2', etc.

The generated ArticleID ensures that each article in the database has a unique identifier.
"""

import mysql.connector

def get_next_article_id(cursor, is_test):
    prefix = "test" if is_test else "A"
    query = f'''
        SELECT ArticleID 
        FROM Articles 
        WHERE ArticleID LIKE '{prefix}%'
        ORDER BY ArticleID DESC 
        LIMIT 1
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    if not result:
        return f"{prefix}1"
    current_id = result[0]
    current_num = int(''.join(filter(str.isdigit, current_id)))
    next_num = current_num + 1
    return f"{prefix}{next_num}"
