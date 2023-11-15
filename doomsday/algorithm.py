days: list[str] = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]


def get_weekday_for_date(date: str) -> str:
    """
    Returns the weekday for the given date in the format YYYY-MM-dd.
    """
    year, month, day = (int(i) for i in date.split('-'))

    anchor_day_index = get_anchor_year(year)

    doomsday_month: list[int] = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]

    if is_leap_year(year):
        doomsday_month[0] = 4
        doomsday_month[1] = 1

    difference = day - doomsday_month[month - 1]
    weekday_index = (anchor_day_index + difference) % 7

    return days[weekday_index]


def is_leap_year(year):
    """Checks if the given year is a leap year."""
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def get_anchor_year(year):
    """Calculates the anchor day index for the given year."""
    century_year: int = year % 100

    if century_year % 2 == 1:
        century_year += 11
    century_year //= 2
    if century_year % 2 == 1:
        century_year += 11

    difference_multiple_of_7: int = century_year % 7
    # multiple of 7 equals or greater than century year
    if difference_multiple_of_7 != 0:
        difference_multiple_of_7 = 7 - difference_multiple_of_7

    numbers_to_add_by_century_year: list[int] = [2, 0, 5, 3]

    return (difference_multiple_of_7 + numbers_to_add_by_century_year[(year // 100) % 4]) % 7


print(get_weekday_for_date('2021-02-01'))