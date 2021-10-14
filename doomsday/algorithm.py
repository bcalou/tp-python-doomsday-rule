import math

from .common import is_leap_year


def is_even(number: int) -> bool:
    """Returns True if the number is even"""
    return number % 2 == 0


def get_year_day(year: int) -> int:
    """ Returns the anchor day name for a year (0 for sunday, 1 for monday, etc...) """
    century_tag: int = get_century_tag(year)

    # Calculates the anchor day
    anchor: int = year % 100
    if not is_even(anchor):
        anchor += 11
    anchor //= 2
    if not is_even(anchor):
        anchor += 11
    cpt: int = 7 - anchor % 7
    anchor = cpt + century_tag
    anchor = anchor % 7
    return anchor


def get_anchoring_day(year: int, month: int) -> int:
    """ Returns the anchor day for a month and a year (10 or 11 for january, 21 for february, etc...) """
    anchoring_days: list = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    if is_leap_year(year):
        anchoring_days[0] = 11
        anchoring_days[1] = 22
    return anchoring_days[month - 1]


def get_century_tag(year: int) -> int:
    """ Returns the century tag """
    tags: list = [2, 0, 5, 3]
    index: int = math.floor(year/100) % 4
    return tags[index]


def get_day_name(day: int) -> str:
    """ Returns a day name for an index (sunday for 0) """
    return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][day]


def get_day_for_date(date: str) -> str:
    """ Returns the day name for a date in "YYYY-MM-dd" format """
    date_list: list = date.split("-")
    day: int = int(date_list[2])
    month: int = int(date_list[1])
    year: int = int(date_list[0])

    year_day: int = get_year_day(year)
    anchoring_day: int = get_anchoring_day(year, month)

    day = day % 7

    return get_day_name(((day - anchoring_day + year_day) % 7))
