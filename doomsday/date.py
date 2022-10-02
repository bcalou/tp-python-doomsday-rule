import doomsday.utils as utils


def is_valid_date(date: str) -> bool:
    """
    Checking if entered string format is correct, if year >= 1583
    and if the date exists.
    """

    utils.init_global_variables()

    if not is_string_format_correct(date):
        return False
    else:
        utils.parse_string_date_to_variables(date)
    
    if not does_year_exists(utils.year):
        return False
    
    if not does_month_exists(utils.month):
        return False
    
    if not does_day_exists(utils.day):
        return False
    
    return True


def is_string_format_correct(given_string: str) -> bool:
    """Checking if the string given by the user fits the requested format."""

    dash_quantity_in_given_string: int = 0

    for character in given_string:
        if character == "-":
            dash_quantity_in_given_string += 1
    
    if dash_quantity_in_given_string != 2:
        print("Please input a correct date format (YYYY-MM-dd) with dashes")
        return False
    
    date_list: list[str] = given_string.split('-')
    year: str = date_list[0]
    month: str = date_list[1]
    day: str = date_list[2]

    if not year.isdecimal():
        print("Please enter a correct year")
        return False
    
    if not month.isdecimal():
        print("Please enter a correct month")
        return False
    
    if not day.isdecimal():
        print("Please input a correct day")
        return False
    
    return True


def does_year_exists(given_year: int) -> bool:
    if given_year >= 1583:
        return True
    else:
        print("Please enter a year after 1583")
        return False


def does_month_exists(given_month: int) -> bool:
    if 0 < given_month <= 12:
        return True
    else:
        print("This month doesn't exist")
        return False


def does_day_exists(given_day: int) -> bool:
    """Checking if the day exists in the specified month."""

    MONTHS_WITH_30_DAYS: list[int] = [4, 6, 9, 11]
    MONTHS_WITH_31_DAYS: list[int] = [1, 3, 5, 7, 8, 10, 12]
    
    if (
        (utils.month in MONTHS_WITH_30_DAYS) and (not 0 < given_day <= 30) or
        (utils.month in MONTHS_WITH_31_DAYS) and (not 0 < given_day <= 31)
    ):
        print("This day doesn't exist in this month")
        return False
    
    elif (
        utils.month == 2 and
        ((is_leap_year(utils.year) and not 0 < given_day <= 29) or
        (not is_leap_year(utils.year) and not 0 < given_day <= 28))
    ):
        print("This day doesn't exist in this month (please check if year is leap)")
        return False
    
    return True


def is_leap_year(given_year: int) -> bool:
    """
    Checking whether the year is leap or not.
    See https://www.mathsisfun.com/leap-years.html for calculation rules.
    """

    return (given_year % 4 == 0 and not given_year % 100 == 0) or (given_year % 400 == 0)
