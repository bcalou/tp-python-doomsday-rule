from doomsday.date import is_leap_year

# Constant variable
LIST_WEEKDAYS: tuple = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
    )


def get_day_for_date(date: str) -> str:
    '''finds the day from a date with Doomsday rule by John Horton Conway'''
    year: str
    month: str
    day: str

    # Get Each elements
    year, month, day = date.split("-")

    anchor_weekday: int = get_anchor_weekday(int(year))
    month_anchor: int = get_doomsday_month(int(year), int(month))
    index_weekday: int = (anchor_weekday + (int(day) - month_anchor)) % 7

    return LIST_WEEKDAYS[index_weekday]


def get_anchor_weekday(year: int) -> int:
    '''Calculates the anchor day for the given year'''
    # Get the subsecular part of the date (two last numbers)
    subsecular_year: int = year % 100

    if not is_even(subsecular_year):
        subsecular_year += 11

    subsecular_year //= 2

    if not is_even(subsecular_year):
        subsecular_year += 11

    anchor_weekday: int = get_century_number(year)\
        + (7 - (subsecular_year % 7))
    return anchor_weekday % 7


def get_doomsday_month(year: int, month: int) -> int:
    '''Get the doomsday accord the month'''
    DOOMSDAY_MONTH: list[int]
    if is_leap_year(year):
        DOOMSDAY_MONTH = [32, 29, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    else:
        DOOMSDAY_MONTH = [31, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    return DOOMSDAY_MONTH[month-1]


def get_century_number(year: int) -> int:
    '''To get the century number for getting anchor weekday'''
    # Get the century and calculate the century number
    return (2 + 5 * (year // 100 % 4)) % 7


def is_even(number: int) -> bool:
    '''If a number is even or not(odd)'''
    return number % 2 == 0