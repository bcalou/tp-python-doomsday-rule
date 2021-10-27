from doomsday.utils import is_leap_year, get_date_parts
from doomsday.days import DAYS


def get_weekday_for_date(date: str) -> str:
    """Use the doomsday algorithm the determine the day of the week"""

    year, month, day = get_date_parts(date)

    # Compute the day of the week with the doomsday method
    anchor: int = get_year_anchor_day(year)
    doomsday: int = get_doomsday_for_month(year, month)
    day_of_week: int = get_day_of_week(day, anchor, doomsday)

    return DAYS[day_of_week]


def get_century_anchor(year: int) -> int:
    """Get the anchor (from 0 = sunday to 6 = saturday) for this century"""
    # Keep the first two digits of the year to get the century (1931 -> 19)
    century: int = int(str(year)[:2])

    # The gregorian calendar repeats itself every 4 centuries (19 -> 3)
    century_position_in_cycle = century % 4

    # Get the correct anchor day (2 = tuesday, ...)
    # depending of the century position in the cycle
    return [2, 0, 5, 3][century_position_in_cycle]


def get_year_anchor_day(year: int) -> int:
    """Get the anchor day (from 0 = sunday to 6 = saturday) for this year"""
    # Keep only the last two digits (1931 -> 31)
    anchor: int = year % 100

    # Add 11 if the result is odd (31 -> 42)
    if (anchor % 2 == 1):
        anchor += 11

    # Divide by two (42 -> 21)
    anchor //= 2

    # Add 11 if the result is odd (21 -> 32)
    if (anchor % 2 == 1):
        anchor += 11

    # Keep the difference between the anchor and the next multiple of 7
    # Exemple : for 32, the next multiple of 7 is 35 so the difference is 3
    # 7 - (32 % 7) = 3
    anchor = 7 - (anchor % 7)

    # Add the century anchor and use a modulo in case in goes above 7
    return (anchor + get_century_anchor(year)) % 7


def get_doomsday_for_month(year: int, month: int) -> int:
    """Get the doomsday for the given month and year"""
    # Special january and february cases for leap years
    if month <= 2 and is_leap_year(year):
        return [4, 1][month - 1]

    # Common year doomsdays
    return [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5][month - 1]


def get_day_of_week(day: int, anchor: int, doomsday: int) -> int:
    """Get the day of the week (from 0 = sunday to 6 = saturday) for the given
    day, using the associated anchor and doomsday
    """
    # Get the difference between the actual day and the doomsday
    # Add the anchor and find the matching day with a mod 7 (8 will become 1)
    return (day - doomsday + anchor) % 7
