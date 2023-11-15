def is_valid_date(date_str):
    from datetime import datetime

    try:
        # Attempt to convert the input string to a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        # Check if the year is greater than or equal to 1583
        if date_obj.year < 1583:
            print("The year must be greater than or equal to 1583.")
            return False

        # Additional checks for the existence of the date can be added here if needed

        return True

    except ValueError:
        # If the conversion fails, print an error message
        print("Incorrect date format. Please use the format YYYY-MM-dd.")
        return False

    return True
