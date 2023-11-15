def is_valid_date(date_str):
    from datetime import datetime

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        # Check if the year is greater than or equal to 1583
        if date_obj.year < 1583:
            print("The year must be greater than or equal to 1583.")
            return False

        return True

    except ValueError:
        print("Incorrect date format. Please use the format YYYY-MM-dd.")
        return False

    return True
