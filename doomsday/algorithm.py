from doomsday.date import is_valid_date, WEEK_DAYS, is_leap_year


def is_even(number: int) -> bool:
    """Returns true if the number is even
    """
    return number % 2 == 0


def get_higher_multiple_of_7(number: int) -> int:
    """Returns the closest multiple of 7 above a given number
    """
    return (number // 7) + 1


def get_century_index(century: int) -> int:
    """Returns the index of a given century
    """
    number_of_the_century = (century // 100) % 4
    if number_of_the_century == 0:
        return 2
    elif number_of_the_century == 1:
        return 0
    elif number_of_the_century == 2:
        return 5
    else:
        return 3


def get_week_anchor_day_of_year(year: str) -> int:
    """Returns the number of the week day corresponding to the anchor day from
    a given year
    """
    year_2_last_digits: int = int(year[2:])

    if not is_even(year_2_last_digits):
        year_2_last_digits += 11

    year_2_last_digits /= 2

    if not is_even(year_2_last_digits):
        year_2_last_digits += 11

    number_to_multiple_of_7: int = (get_higher_multiple_of_7(
        year_2_last_digits) * 7) - year_2_last_digits

    number_to_multiple_of_7 += get_century_index(int(year) -
                                                 year_2_last_digits)

    # Get the day between 0 and 6
    number_to_multiple_of_7 %= 7

    return int(number_to_multiple_of_7)


def get_anchor_day_of_the_month(month: int, year: int) -> int:
    """Returns the anchor day of a given month number
    """
    # April, June, August, October and December
    if month == 4 or month == 6 or month == 8 or month == 10 or month == 12:
        return month

    # January and February
    if month == 1 or month == 2:
        if is_leap_year(year):
            return 11 if month == 1 else 22
        else:
            return 10 if month == 1 else 21

    # March, May, July, September, November
    if month == 3:
        return 0
    elif month == 5:
        return 9
    elif month == 7:
        return 11
    elif month == 9:
        return 5
    else:
        return 7


def get_week_day(day_in_month: int, anchor_day: int,
                 week_doomsday: int) -> str:
    """Returns the week day of a day in a month using the week day of the
    anchor day
    """
    return WEEK_DAYS[(week_doomsday + (day_in_month - anchor_day)) % 7]


def get_weekday_for_date(date: str) -> str:
    """Returns the week day of a given date
    """
    if not is_valid_date(date):
        return "The date is not valid."

    year: str = date[:4]
    # We check if the 7th character of the date is a number or a separator
    # because the month can have one or two digits
    if date[6].isnumeric():
        month: int = int(date[5:7])
        day: int = int(date[8:])
    else:
        month: int = int(date[5])
        day: int = int(date[7:])

    # The week day of the anchor day of the year
    anchor_week_day: int = get_week_anchor_day_of_year(year)

    # The number of the anchor day of the month
    anchor_day: int = get_anchor_day_of_the_month(month, int(year))

    return get_week_day(day, anchor_day, anchor_week_day)
