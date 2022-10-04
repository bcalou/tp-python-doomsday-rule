from doomsday.utils import is_leap_year, get_date_parts
from doomsday.constants import DAYS_PER_MONTH


def is_valid_date(date: str) -> bool:
    """Test if the given date is correctly formatted and exists"""
    return is_date_format_correct(date) and is_existing_date(date)


def is_date_format_correct(date: str) -> bool:
    """Test if the given date follow the YYYY-MM-dd format"""
    # "1990-02-15".split('-') -> ["1990", "02", "15"]
    date_parts: list[str] = date.split('-')

    # Check we have three elements
    if len(date_parts) != 3:
        print("The date must be composed of three parts separated by a dash")
        return False

    year, month, day = date_parts

    # Remove the dashes and check that only numbers remain
    if not (year.isnumeric() and month.isnumeric() and day.isnumeric()):
        print("The date should be composed of numbers only")
        return False

    return True


def is_existing_date(date: str) -> bool:
    """Test if the given date actually exists"""
    year, month, day = get_date_parts(date)

    return (
        is_existing_year(year)
        and is_existing_month(month)
        and is_existing_day(year, month, day)
    )


def is_existing_year(year: int) -> bool:
    """Test if the given year is supported and exists"""
    # Only date after the beginning of the gregorian calendar are supported
    if year < 1583:
        print("Only year from 1583 on are supported")
        return False

    return True


def is_existing_month(month: int) -> bool:
    """Test if the given month exists"""

    if not (month >= 1 and month <= 12):
        print("The month should be between 1 and 12")
        return False

    return True


def is_existing_day(year: int, month: int, day: int) -> bool:
    """Test if the given day exists"""
    # 29 days in february for leap years
    if month == 2 and is_leap_year(year):
        number_of_days_in_month = 29

    # Else, just get the number of day for the matching month
    else:
        number_of_days_in_month = DAYS_PER_MONTH[month - 1]

    if not (day >= 1 and day <= number_of_days_in_month):
        print("This day does not exist for this month and year")
        return False

    return True
