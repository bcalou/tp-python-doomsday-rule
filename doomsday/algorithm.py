from doomsday.date import is_valid_date, WEEK_DAYS, is_leap_year, MONTHS


def is_even(number: int) -> bool:
    """Returns true if the number is even
    """
    return number % 2 == 0


def get_higher_multiple_of_7(number: int) -> int:
    """Returns the closest multiple of 7 above a given number
    """
    return (number // 7) + 1


def get_week_doomsday_of_year(year: str) -> str:
    """Returns the "doomsday" week day from a given year
    """

    year_2_last_digits: int = int(year[2:])

    if is_even(year_2_last_digits):
        year_2_last_digits /= 2
    else:
        year_2_last_digits += 11

    if not is_even(year_2_last_digits):
        year_2_last_digits += 11

    number_to_multiple_of_7: int = (get_higher_multiple_of_7(
        year_2_last_digits) * 7) - year_2_last_digits

    # TODO : FUNCTION TO GET THE CENTURY NUMBER
    number_to_multiple_of_7 += 2

    number_to_multiple_of_7 %= 7

    return WEEK_DAYS[int(number_to_multiple_of_7)]


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


def get_weekday_for_date(date: str) -> str:
    """Returns the week day of a given date
    """

    if not is_valid_date(date):
        return "The date is not valid."

    year: str = date[:4]
    month: str = date[5:7]
    day: str = date[8:]

    week_doomsday: str = get_week_doomsday_of_year(year)

    anchor_day: int = get_anchor_day_of_the_month(int(month), int(year))

    print("The", anchor_day, MONTHS[int(month) - 1], "of the year", year,
          "was a", week_doomsday)

    # TODO : FUNCTION TO DETERMINE THE DAY ACCORDING TO THE ANCHOR DAY

    return "Monday"


get_weekday_for_date("2016-03-01")
