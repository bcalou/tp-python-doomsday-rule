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


def get_anchor_day_for_year(year: int) -> int:
    """Returns the anchor day of a given year starting at 0 for Sunday"""

    # The last two digits of the year in order to apply the Odd + 11 algorithm
    year_digits: int = year % 100
    if (year_digits % 2 == 1):
        year_digits += 11

    year_digits = int(year_digits / 2)
    if (year_digits % 2 == 1):
        year_digits += 11

    multiple_of_7: int = math.ceil(year_digits / 7) * 7
    # Calculate the century offset for the current year
    century_index: int = int(year / 100) % 4
    century_offset = CENTURY_OFFSETS[century_index]

    return multiple_of_7 - year_digits + century_offset


def get_anchor_for_month(month: int, year: int) -> int:
    """Returns the anchor day of a given month given the year"""

    match (month):
        case 4, 6, 8, 10, 12:
            return month
        case 1:
            return 11 if date.is_leap_year(year) else 10
        case 2:
            return 22 if date.is_leap_year(year) else 21
        case 3:
            return 0
        case 5:
            return 9
        case 7:
            return 11
        case 9:
            return 5
        case 11:
            return 7

    return 0


def get_weekday_for_date(date: str) -> str:
    date_split: list[str] = date.split("-")
    year: int = int(date_split[0])
    month: int = int(date_split[1])
    day: int = int(date_split[2])

    year_anchor_day: int = get_anchor_day_for_year(year)
    month_anchor: int = get_anchor_for_month(month, year)
    day_offset: int = abs(day - month_anchor)

    final_day_index = (year_anchor_day + day_offset) % 7

    return DAY_NAMES[final_day_index]
