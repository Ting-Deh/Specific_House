def get_valid_filename():
    """
    Prompts the user for a valid filename and then allows the user to select a file extension
    from a predefined list (pdf, png, jpg). Returns the complete filename with the chosen extension.

    This function ensures that the filename:
    - Doesn't contain forbidden characters
    - Is of a reasonable length (not too long)
    - Ends with a user-selected, valid extension
    """

    # List of forbidden characters in filenames
    forbidden_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

    while True:
        # Ask the user for a filename
        filename = input("Enter the filename (without extension): ").strip()

        # Check for forbidden characters
        if any(char in filename for char in forbidden_chars):
            print("Filename contains forbidden characters. Please try again.")
            continue

        # Check for reasonable length
        if len(filename) > 50:
            print("Filename is too long. Please keep it under 50 characters.")
            continue

        # If the filename passed the checks, break the loop
        break

    # Now, let the user select a file extension
    while True:
        print("Select a file extension:")
        print("1. pdf")
        print("2. png")
        print("3. jpg")
        choice = input("Enter the number corresponding to your choice: ").strip()

        if choice == '1':
            return filename + ".pdf"
        elif choice == '2':
            return filename + ".png"
        elif choice == '3':
            return filename + ".jpg"
        else:
            print("Invalid choice. Please select a valid file extension.")
