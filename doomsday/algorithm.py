"""
John Conway's Doomsday Algorithm
This is an implementation of https://en.wikipedia.org/wiki/Doomsday_rule
"""

from doomsday.utils import is_leap_year, get_date_parts
from doomsday.constants import (
    DAYS_NAMES,
    CENTURY_ANCHORS,
    COMMON_YEAR_DOOMSDAYS,
    LEAP_YEAR_DOOMSDAYS
)


def get_weekday_for_date(date: str) -> str:
    """Use the doomsday algorithm the determine the weekday

    This is an implementation of https://en.wikipedia.org/wiki/Doomsday_rule
    """
    year, month, day = get_date_parts(date)

    # We need two things : the doomsday for this month (day of reference)
    # and the year's anchor weekday (what weekday will be the day of reference)
    doomsday: int = get_month_doomsday(year, month)
    anchor_weekday: int = get_year_anchor_weekday(year)

    # Make the final computation
    weekday = compute_weekday(day, doomsday, anchor_weekday)

    return DAYS_NAMES[weekday]


def get_month_doomsday(year: int, month: int) -> int:
    """Get the doomsday for the given year and month"""
    year_doomsdays: tuple[int, ...] = (
        LEAP_YEAR_DOOMSDAYS if is_leap_year(year) else COMMON_YEAR_DOOMSDAYS
    )

    return year_doomsdays[month - 1]


def get_year_anchor_weekday(year: int) -> int:
    """Get the anchor (from 0 = sunday to 6 = saturday) for this year"""
    # Keep only the last two digits (1931 -> 31)
    value: int = year % 100

    # Add 11 if the result is odd (31 -> 42)
    if is_odd(value):
        value += 11

    # Divide by two (42 -> 21)
    value //= 2

    # Add 11 if the result is odd (21 -> 32)
    if is_odd(value):
        value += 11

    # Get the difference with the next multiple of 7 (32 -> 3)
    value = get_difference_with_next_multiple_of_7(value)

    # Add the century anchor weekday
    value += get_century_anchor_weekday(year)

    # Keep the value between 0 (sunday) and 6 (saturday)
    return value % 7


def get_difference_with_next_multiple_of_7(value: int) -> int:
    """Keep the difference between the anchor and the next multiple of 7

    Exemple : for 32, the next multiple of 7 is 35 so the difference is 3.
    3 = 7 - (32 % 7)
    """
    return 7 - (value % 7)


def get_century_anchor_weekday(year: int) -> int:
    """Get the anchor weekday for this year's century"""
    # Keep the first two digits of the year to get the century (1931 -> 19)
    century: int = int(str(year)[:2])

    # The gregorian calendar repeats itself every 4 centuries (19 -> 3)
    century_position_in_cycle: int = century % 4

    # Get the correct anchor day depending of the century position in the cycle
    return CENTURY_ANCHORS[century_position_in_cycle]


def compute_weekday(day: int, doomsday: int, anchor_weekday: int) -> int:
    """Return the final computation (from 0 = sunday to 6 = saturday)

    Exemple : if the 1st (doomsday) is friday (year anchor weekday),
    then the 2nd (day to find) is sunday (result)
    Translates to : if 1 (doomsday) gives 5 (year anchor weekday),
    then 2 (day to find) gives 6 (result)
    Translate to : 6 = (2 - 1) + 5
    """
    weekday: int = (day - doomsday) + anchor_weekday

    # Keep the result between 0 (sunday) and 6 (saturday)
    return weekday % 7


def is_odd(number: int) -> bool:
    """Return wether the number is odd (cannot be divided by 2)"""
    return number % 2 == 1
