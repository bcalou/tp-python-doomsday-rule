MONTHS: list[str] = ["January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November",
                     "December"]
WEEK_DAYS: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                        "Friday", "Saturday"]


def is_valid_year(year: str) -> bool:
    """Checks if the year is a valid number and greater than 1583
    """

    if not year.isnumeric():
        print("Error: the year must be a number of 4 digits")
        return False

    if not int(year) >= 1583:
        print("Error: the year must be greater than 1583")
        return False

    return True


def is_valid_separator(separator: str) -> bool:
    """Returns true if the date separator is -
    """

    if separator != '-':
        print("Error: the date separator must be -")
        return False

    return True


def is_valid_month(month: str) -> bool:
    """Checks if the month is a valid number and between 1 and 12
    """

    if not month.isnumeric():
        print("Error: the month must be a number of 1 or 2 digits")
        return False

    if not 1 <= int(month) <= 12:
        print("Error: the month must between 1 and 12")
        return False

    return True


def is_valid_day(day: str, month: str, year: str) -> bool:
    """Checks if the day is a valid number and between 1 and the last day of
    the month
    """

    if not day.isnumeric():
        print("Error: the day must be a number of 1 or 2 digits")
        return False

    if not 1 <= int(day):
        print("Error: the day must greater than 0")
        return False

    if not is_valid_day_in_month(int(day), int(month), int(year)):
        return False

    return True


def is_leap_year(year: int) -> bool:
    """Returns true if the year is a leap year
    """
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


def is_valid_day_in_month(day: int, month: int, year: int) -> bool:
    """Returns true if the day exists in its month
    """

    # Month with 30 days
    if month == 4 or month == 6 or month == 9 or month == 11:
        if not day <= 30:
            print("Error: the date is not valid, there are 30 days in",
                  MONTHS[month - 1])
            return False

    # Month with 31 days
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or
            month == 10 or month == 12):
        if not day <= 31:
            print("Error: the date is not valid, there are 31 days in",
                  MONTHS[month - 1])
            return False

    # February
    if is_leap_year(year):
        if month == 2 and not day <= 29:
            print("Error: the date is not valid, there are 29 days in "
                  "February this year")
            return False
    else:
        if month == 2 and not day <= 28:
            print("Error: the date is not valid, there are 28 days in "
                  "February this year")
            return False

    return True


def is_valid_date(date: str) -> bool:
    """Returns true if the date is valid
    """

    # The year is necessarily the first four characters of the date
    if not is_valid_year(date[:4]):
        return False

    year: str = date[:4]

    if not is_valid_separator(date[4]):
        return False

    # We check if the 7th character of the date is a number or a separator
    # because the month can have one or two digits
    if date[6].isnumeric():
        # The month has two digits
        if not is_valid_month(date[5:7]):
            return False

        if not is_valid_separator(date[7]):
            return False

        if not is_valid_day(date[8:], date[5:7], year):
            return False
    else:
        # The month has only one digit
        if not is_valid_month(date[5]):
            return False

        if not is_valid_separator(date[6]):
            return False

        if not is_valid_day(date[7:], date[5], year):
            return False

    return True
