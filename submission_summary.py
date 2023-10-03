def display_submission_summary(article_details):
    """
    Displays a summary of the submitted article to the user.

    Parameters:
    - article_details (dict): A dictionary containing key-value pairs of the article's attributes.
    """

    print("\nSummary of Your Submission:")
    print("-" * 30)  # a separator for better visual appeal
    for key, value in article_details.items():
        print(f"{key}: {value}")
    print("-" * 30)  # another separator
    print("Article submitted successfully.")
