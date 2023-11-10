from doomsday.date import get_date_parts, is_leap_year

# Human readable day names (sunday is 0)
DAYS_NAMES = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)

# A loop of 4 numbers starting from the 17th century
CENTURY_ANCHOR_WEEKDAYS = (2, 0, 5, 3)

# List of doomsday for each month of a common year
DOOMSDAYS_COMMON_YEAR = (3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5)

# Doomsdays change for the first two months on leap years
DOOMSDAYS_LEAP_YEAR = (4, 1) + DOOMSDAYS_COMMON_YEAR[2:]


def get_weekday_for_date(date: str) -> str:
    """Use the doomsday algorithm the determine the weekday

    This is an implementation of https://en.wikipedia.org/wiki/Doomsday_rule
    """
    year, month, day = get_date_parts(date)

    # We need two things : the doomsday for this month (day of reference)
    # and the year's anchor weekday (what weekday will be the day of reference)
    doomsday = get_month_doomsday(year, month)
    anchor_weekday = get_year_anchor_weekday(year)

    # Make the final computation
    weekday = compute_weekday(day, doomsday, anchor_weekday)

    # Convert to human string
    return DAYS_NAMES[weekday]


def get_month_doomsday(year: int, month: int) -> int:
    """Get the doomsday for the given year and month"""
    year_doomsdays = (
        DOOMSDAYS_LEAP_YEAR if is_leap_year(year) else DOOMSDAYS_COMMON_YEAR
    )

    return year_doomsdays[month - 1]


def get_year_anchor_weekday(year: int) -> int:
    """Get the anchor (from 0 = sunday to 6 = saturday) for this year"""
    # Keep only the last two digits (1931 -> 31)
    value = year % 100

    # Add 11 if the result is odd (31 -> 42)
    if is_odd(value):
        value += 11

    # Divide by two (42 -> 21)
    value //= 2

    # Add 11 if the result is odd (21 -> 32)
    if is_odd(value):
        value += 11

    # Get the difference with the next multiple of 7 (32 -> 3)
    value = 7 - (value % 7)

    # Add the century anchor weekday
    value += get_century_anchor_weekday(year)

    # Keep the value between 0 (sunday) and 6 (saturday)
    return value % 7


def is_odd(number: int) -> bool:
    """Return wether the number is odd (cannot be divided by 2)"""
    return number % 2 == 1


def get_century_anchor_weekday(year: int) -> int:
    """Get the anchor weekday for this year's century"""
    # Keep the first two digits of the year to get the century (1931 -> 19)
    century = int(str(year)[:2])

    # The gregorian calendar repeats itself every 4 centuries (19 -> 3)
    century_position_in_gregorian_cycle = century % 4

    # Get the correct anchor day depending of the century position in the cycle
    return CENTURY_ANCHOR_WEEKDAYS[century_position_in_gregorian_cycle]


def compute_weekday(day: int, doomsday: int, anchor_weekday: int) -> int:
    """Return the final computation (from 0 = sunday to 6 = saturday)

    Exemple: if the 1st (doomsday) is friday (anchor weekday),
    then the 2nd (day to find) is sunday (result)
    Translates to: if 1 (doomsday) gives 5 (year anchor weekday),
    then 2 (day to find) gives 6 (result)
    Translate to: 6 = (2 - 1) + 5
    """
    weekday = (day - doomsday) + anchor_weekday

    # Keep the result between 0 (sunday) and 6 (saturday)
    return weekday % 7
