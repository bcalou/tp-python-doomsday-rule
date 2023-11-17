from doomsday.algorithm_helper_function import *
from doomsday.does_date_exist import split_date, is_leap_year


MONTHS_ANCHOR: list[int] = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
WEEKDAYS: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                       "Friday", "Saturday"]


def get_weekday_for_date(date: str) -> str:
    """Return the weekday from a date

    date has to be of valid format and exist"""

    splitted_date: list[int] = split_date(date)

    year:   int = splitted_date[0]
    month:  int = splitted_date[1]
    day:    int = splitted_date[2]

    # Finds the doomsday of a given year
    doomsday: int = get_year_doomsday(year)

    # Retreive the anchor day of a given month
    anchor_day: int = MONTHS_ANCHOR[month - 1]

    # During a leap year the anchor for January and February changes
    # January: 10 -> 11      February: 21 -> 22
    if is_leap_year(year) and (month == 1 or month == 2):
        anchor_day += 1

    # Get the difference between the anchor day and the choosen day
    diff_with_anchor: int = day - anchor_day

    # Adds the doomsday to our diff as an offset and apply mod 7
    # to get our final answer
    weekday: int = (diff_with_anchor + doomsday) % 7

    return WEEKDAYS[weekday]
