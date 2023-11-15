import math
import doomsday.date as date

CENTURY_OFFSETS = (2, 0, 5, 3)
DAY_NAMES = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)


def get_weekday_for_date(date: str) -> str:
    """Returns the name of the day at a given date."""
    date_split: list[str] = date.split("-")
    year: int = int(date_split[0])
    month: int = int(date_split[1])
    day: int = int(date_split[2])

    year_anchor_day: int = get_anchor_day_for_year(year)
    month_anchor: int = get_anchor_for_month(month, year)

    # Calculate the number of days between the month's anchor day and
    # the wanted day.
    day_offset: int = abs(day - month_anchor)
    # Since the month's anchor day and the year's anchor day are the same
    # we can add the year's anchor day index to get the final day index.
    final_day_index = (year_anchor_day + day_offset) % 7

    return DAY_NAMES[final_day_index]



def get_anchor_day_for_year(year: int) -> int:
    """Returns the anchor day of a given year starting at 0 for Sunday"""

    # Apply the Odd + 11 algorithm
    year_digits: int = year % 100
    if (year_digits % 2 == 1):
        year_digits += 11

    year_digits = year_digits // 2
    if (year_digits % 2 == 1):
        year_digits += 11

    # Calculate the century offset for the current year
    multiple_of_7: int = math.ceil(year_digits / 7) * 7
    century_index: int = (year // 100) % 4
    century_offset = CENTURY_OFFSETS[century_index]

    return multiple_of_7 - year_digits + century_offset


def get_anchor_for_month(month: int, year: int) -> int:
    """Returns the anchor day of a given month given the year"""

    month_anchors = (
        11 if date.is_leap_year(year) else 10,
        22 if date.is_leap_year(year) else 21,
        0, 4, 9, 6, 11, 8, 7, 10, 7, 12
    )

    return month_anchors[month - 1]
