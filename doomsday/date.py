def is_valid_date(date_str: str) -> bool:
    from datetime import datetime

    try:
        date_obj: datetime = datetime.strptime(date_str, '%Y-%m-%d')

        # Check if the year is greater than or equal to 1583
        # If it is not, return False and print an error message
        if date_obj.year < 1583:
            print("The year must be greater than or equal to 1583.")

            return False

        return True

    # If the date is not in the correct format (YYYY-MM-dd) or if the date
    # doesn't exist (for example : 2021-18-45), then return False and print
    # an error message
    except ValueError:
        print(
            f"Incorrect date {date_str}."
            " Please use the format YYYY-MM-dd or check if the date exists.")

        return False

    except Exception as e:
        # Handle any other exception
        print(e)

        return False
