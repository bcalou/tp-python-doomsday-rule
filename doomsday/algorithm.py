from doomsday.date import *


def get_year_pivots(month: int, year: int) -> int:
    """Return the date of the pivot day in the selected month and year"""
    year_pivots: list[int] = [
        (3, 4)[is_leap_year(year)],
        (0, 1)[is_leap_year(year)],
        0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    return year_pivots[month - 1]


def get_century_marker(year: int) -> int:
    """The century marker is an empirical value
    based on the hundred digit over a 4 century loop"""
    y: int = (year % 400) // 100
    return [2, 0, 5, 3][y]


def compute_date(year: int) -> int:
    """Compute the year to get a reference value based
    on the \"Odd + 11\" methode"""
    y_last_digit: int = year % 100
    y_last_digit = (y_last_digit + 11, y_last_digit)[y_last_digit % 2 == 0]
    y_last_digit //= 2
    y_last_digit = (y_last_digit + 11, y_last_digit)[y_last_digit % 2 == 0]
    y_last_digit = 7 - (y_last_digit % 7)
    return (y_last_digit + get_century_marker(year)) % 7


def get_day_for_date(date: str) -> str:
    """Return the day of the date passed in argument
    using John Conway's Doomsday Methode"""
    days: list[str] = [
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
        ]
    date_as_int : list[int] = convert_date(date)
    anchor_day: int = compute_date(date_as_int[0])
    month_pivots_day = get_year_pivots(date_as_int[1], date_as_int[0])
    # shift from the anchor day by the difference between day and pivot
    return days[(anchor_day + (date_as_int[2] - month_pivots_day)) % 7]
