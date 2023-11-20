from datetime import datetime

WEEKDAYS = (
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
)
# List of memorable dates that always land on doomsday for each month
# (except January and February)
doomsday_month: list[int] = [3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]


def get_weekday_for_date(date_str: str) -> str:
    """
    Returns the day of the week for the given date in the format YYYY-MM-dd.
    """
    # Convert date to datetime
    date = datetime.strptime(date_str, '%Y-%m-%d')
    # Get the doomsday of the year
    doomsday_of_year = get_doomsday_year(date.year)

    # Check if the year is a leap year
    # If it is, change the doomsday for January and February
    if date.year % 400 == 0 or (date.year % 100 != 0 and date.year % 4 == 0):
        doomsday_month[0] = 4
        doomsday_month[1] = 29

    # Get the difference between the doomsday of the month and the given date
    difference_doomsday_and_date = date.day - doomsday_month[date.month - 1]

    # Get the weekday of the date as an integer between 0 and 6
    weekday = (doomsday_of_year + difference_doomsday_and_date) % 7

    # Return the weekday as a string
    return WEEKDAYS[weekday]


def get_doomsday_year(year: int) -> int:
    """Gets the doomsday of the year as an integer between 0 and 6"""
    last_two_digits_of_year: int = year % 100

    if last_two_digits_of_year % 2 != 0:
        last_two_digits_of_year += 11
    last_two_digits_of_year //= 2
    if last_two_digits_of_year % 2 != 0:
        last_two_digits_of_year += 11

    # Get the difference between the last two numbers of the year and the
    # closest superior or equal multiple of 7
    difference_multiple_of_7 = last_two_digits_of_year % 7
    if difference_multiple_of_7 != 0:
        difference_multiple_of_7 = 7 - difference_multiple_of_7

    # Number to add to the difference to get the doomsday of the year
    numbers_to_add_by_century: list[int] = [2, 0, 5, 3]

    # Return the doomsday of the year as an integer between 0 and 6
    return (difference_multiple_of_7 + numbers_to_add_by_century[
        (year // 100) % 4]) % 7
