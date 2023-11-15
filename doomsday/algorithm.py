DAYS: tuple[str, str, str, str, str, str, str] = (
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
)


def get_weekday_for_date(date: str) -> str:
    """Returns the weekday for the given date in the format YYYY-MM-dd."""
    year, month, day = (int(i) for i in date.split('-'))

    anchor_day_index = get_anchor_of_the_year(year)

    doomsday_month: list[int] = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]

    if is_leap_year(year):
        doomsday_month[0] = 4
        doomsday_month[1] = 1

    # Calculate the difference between the day and the doomsday of the month
    difference = day - doomsday_month[month - 1]
    # Calculate the weekday index by using the anchor day index and the difference
    weekday_index = (anchor_day_index + difference) % 7

    return DAYS[weekday_index]


def is_leap_year(year: int):
    """Checks if the given year is a leap year."""
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def get_anchor_of_the_year(year: int):
    """Calculates the anchor day index for the given year."""
    value: int = year % 100

    if value % 2 == 1:
        value += 11
    value //= 2
    if value % 2 == 1:
        value += 11

    # multiple of 7 equals or greater than century year
    difference_multiple_of_7: int = (7 - value) % 7

    numbers_to_add_by_century_year: list[int] = [2, 0, 5, 3]

    return (difference_multiple_of_7 + numbers_to_add_by_century_year[(year // 100) % 4]) % 7
