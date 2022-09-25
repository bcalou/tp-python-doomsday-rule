from doomsday.date import is_valid_date, WEEK_DAYS


def is_even(number: int) -> bool:
    """Returns true if the number is even
    """
    return number % 2 == 0


def get_higher_multiple_of_7(number: int) -> int:
    """Returns the closest multiple of 7 above a number
    """
    return (number // 7) + 1


def get_doomsday(year: str) -> str:
    """Returns the "doomsday" from a given year
    """

    # TODO : REFACTOR THIS

    year_2_last_digits: int = int(year[2:])

    if is_even(year_2_last_digits):
        year_2_last_digits /= 2
        if not is_even(year_2_last_digits):
            year_2_last_digits += 11
    else:
        year_2_last_digits += 11
        if not is_even(year_2_last_digits):
            year_2_last_digits += 11

    difference: int = (get_higher_multiple_of_7(year_2_last_digits) * 7) - year_2_last_digits

    return WEEK_DAYS[int((difference + 2) % 7)]


def get_weekday_for_date(date: str) -> str:
    """Returns the week day of a given date
    """

    if not is_valid_date(date):
        return "The date is not valid."

    year: str = date[:4]
    month: str = date[5:7]
    day: str = date[8:]

    doomsday: str = get_doomsday(year)
    print(doomsday)

    return "Monday"


get_weekday_for_date("2022-11-22")