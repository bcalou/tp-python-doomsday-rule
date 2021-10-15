import re
from .utils import get_split_date


def is_valid_date(date: str) -> bool:
    # Check if format is correct
    match = re.search(r'(\d+-\d+-\d+)', str(date))
    if match is None or match.group(0) != date:
        return False

    # Check if the date exists
    year, month, day = get_split_date(date)
    # Check if the year is in Gregorian calendar
    if year < 1583:
        return False
    if month not in range(1, 13):
        return False
    if day not in range(1, get_day_max(month, year) + 1):
        return False
    return True


# Get the last day number depending on the month
def get_day_max(month: int, year: int):
    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif int(month) == 2:
        return (28, 29)[is_leap(int(year))]
    else:
        return 30


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

