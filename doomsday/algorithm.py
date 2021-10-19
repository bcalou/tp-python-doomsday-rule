from doomsday.date import *

days: list[str] = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
    ]
common_year_pivots: list[int] = [3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
leap_year_pivots: list[int] = [4, 1, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]


# The century marker is an empirical value
# based on the hundred digit over a 4 century loop
def get_century_marker(year: int) -> int:
    y: int = (year % 400) // 100
    return [2, 0, 5, 3][y]


# "Odd + 11" methode
def compute(year: int) -> int:
    y_last_digit: int = year % 100
    y_last_digit = y_last_digit if y_last_digit % 2 == 0 else y_last_digit + 11
    y_last_digit //= 2
    y_last_digit = y_last_digit if y_last_digit % 2 == 0 else y_last_digit + 11
    y_last_digit = 7 - (y_last_digit % 7)
    return (y_last_digit + get_century_marker(year)) % 7


# return the day of the date passed in argument
# using John Conway's Doomsday Methode
def get_day_for_date(date: str) -> str:
    year, month, day = convert_date(date)
    anchor_day: int = compute(year)
    if is_leap_year(year):
        month_pivots_day = leap_year_pivots[month - 1]
    else:
        month_pivots_day = common_year_pivots[month - 1]
    # shift from the anchor day by the difference between day and pivot
    return days[(anchor_day + (day - month_pivots_day)) % 7]
