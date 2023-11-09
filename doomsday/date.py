from doomsday.constants import (DAYS_PER_MONTH_COMMON_YEAR,
                                DAYS_PER_MONTH_LEAP_YEAR)
from doomsday.utils import get_date_parts, is_leap_year


def is_valid_date(date: str) -> bool:
    """Test if the given date is correctly formatted and exists"""
    return is_date_format_correct(date) and is_existing_date(date)


def is_date_format_correct(date: str) -> bool:
    """Test if the given date follow the YYYY-MM-dd format"""
    # "1990-02-15".split('-') -> ["1990", "02", "15"]
    date_parts = date.split('-')

    # Check that we have three elements
    if len(date_parts) != 3:
        print("The date must be composed of three parts separated by a dash")
        return False

    year, month, day = date_parts

    # Check that only numbers remain
    if not (year.isdecimal() and month.isdecimal() and day.isdecimal()):
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
    """Test if the given year is supported"""
    if year < 1583:
        print("Only years from 1583 on are supported")
        return False

    return True


def is_existing_month(month: int) -> bool:
    """Test if the given month exists"""

    if not (1 <= month <= 12):
        print("The month should be between 1 and 12")
        return False

    return True


def is_existing_day(year: int, month: int, day: int) -> bool:
    """Test if the given day exists"""
    days_per_month = (
        DAYS_PER_MONTH_LEAP_YEAR if is_leap_year(year)
        else DAYS_PER_MONTH_COMMON_YEAR
    )

    if not (1 <= day <= days_per_month[month - 1]):
        print("This day does not exist for this month and year")
        return False

    return True
