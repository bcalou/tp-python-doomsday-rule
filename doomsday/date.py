from datetime import datetime


def is_valid_date(date_str: str) -> bool:
    """Checks if the given date is valid."""
    try:
        # Try to convert the string to a date object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        # Check if the year is greater than or equal to 1583
        if date_obj.year < 1583:
            print("Error: The year must be greater than or equal to 1583.")
            return False

        return True

    except ValueError:
        # Conversion error, the date is not in the expected format
        print("Error: The date does not follow the format YYYY-MM-dd.")
        return False

    except Exception as e:
        # Handle other potential errors
        print(f"An error occurred: {e}")
        return False
