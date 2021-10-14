from .common import is_leap_year


def get_max_month_day(year: int, month: int) -> int:
    """ Returns the maximum possible day number for a month and a year 
    (ex: 29 for february for a leap year) """
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month <= 7:
        return 30 + month % 2
    else:
        return 30 + (month + 1) % 2


def is_valid_date(date: str) -> bool:
    """ Returns true if the date format is valid """
    if not type(date) is str:
        return False

    # The split method works even if there is no '-' separator: a list with
    # only one item will be returned
    date_list: list[str] = date.split('-')

    if len(date_list) != 3:
        return False

    # Checks if all the date entries are digits
    if (not date_list[0].isdigit() or
        not date_list[1].isdigit() or
            not date_list[2].isdigit()):

        return False

    year: int = int(date_list[0])
    month: int = int(date_list[1])
    day: int = int(date_list[2])

    # Checks if the year is superior of 1583 (Gregorian calendar)
    # and the month and day are in the correct range
    if (not year >= 1583 or
        not 1 <= month <= 12 or
            not 1 <= day <= get_max_month_day(year, month)):
        return False

    return True
