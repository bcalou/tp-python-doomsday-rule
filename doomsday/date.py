import re


def is_valid_date(input_date: str) -> bool:
    """
    Return boolean.
    Check the validity of the date.
    Keyword arguments:
    input_date -- Date input by the user
    """

    if not is_valid_format(input_date):
        return False
    elif not is_valid_year(input_date):
        print("Error: Invalid year")
        return False
    elif not is_valid_count_day(input_date):
        print("Error: Invalid day")
        return False
    return True


def is_valid_format(target) -> bool:
    """
    Return boolean.
    Check the validity of the date format.
    Keyword arguments:
    target -- date input by the user.
    """

    is_valid_input_type: bool = True if type(target) == str else False
    """A regular  expression for the format (YYYY-MM-dd)"""
    format = re.compile("(1[5-9][0-9]{2}|2[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])")

    if not is_valid_input_type:
        print("Error: Invalid input type")
    elif not format.match(target):
        print("Error: Invalid date syntaxe.")

    return True if is_valid_input_type and format.match(target) else False


def is_valid_count_day(target) -> bool:
    """
    Return boolean.
    Check the number of days in the month.
    Keyword arguments:
    target -- date input by the user.
    """

    year, month, day = get_split_date(target)
    has_leap_year: bool = is_leap_year(year)
    if month % 2 == 0 and month != 8:
        if month == 2 and not has_leap_year and day > 28:
            return False
        elif month == 2 and has_leap_year and day > 29:
            return False
        elif day > 30:
            return False

    return True


def is_valid_year(target) -> bool:
    """
    Return boolean.
    Checked the date is later than 1583
    Keyword arguments:
    target -- date input by the user.
    """
    year: int = get_split_date(target)[0]
    return year >= 1583


def get_split_date(target) -> tuple:
    """
    Return tuple
    Split the data into three variables.
    Keyword arguments:
    target -- date input by the user.
    """
    split_date: list[str] = target.split('-')

    year: int = int(split_date[0])
    month: int = int(split_date[1])
    day: int = int(split_date[2])

    return year, month, day


def is_leap_year(target) -> bool:
    """
    Return boolean
    Checked if the year is a leap year
    Keyword arguments:
    target -- the year of data input by the user.
    """

    """It is a leap year if it's a multiple of 4 but not of 100 and is a multiple of 400"""
    return (target % 400 == 0) or (target % 4 == 0 and target % 100 != 0)
