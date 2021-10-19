import re


def is_valid_date(input_date: str) -> bool:

    if not is_valid_format(input_date):
        return False
    elif not is_valid_year(input_date):
        print("Error: Invalid year")
        return False
    elif not is_valid_count_day(input_date):
        print("Error: Invalid day")
        return False
    return True


def is_valid_format(target) -> bool:

    is_valid_input_type: bool = False if type(target) != str else True
    format = re.compile("(1[5-9][0-9][0-9]|2[0-9][0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])")

    if not is_valid_input_type:
        print("Error: Invalid input type")
    elif not format.match(target):
        print("Error: Invalid date syntaxe")

    return True if is_valid_input_type and format.match(target) else False


def is_valid_count_day(target) -> bool:

    year, month, day = get_split_date(target)
    has_leap_year: bool = is_leap_year(year)
    is_valid_day_count: bool = True

    if day <= 31:
        if month % 2 == 0 and month != 8:
            if month == 2 and not has_leap_year and day > 28:
                is_valid_day_count = False
            elif month == 2 and has_leap_year and day > 29:
                is_valid_day_count = False
            elif day > 30:
                is_valid_day_count = False
    else:
        is_valid_day_count = False

    return is_valid_day_count


def is_valid_year(target) -> bool:
    year: int = get_split_date(target)[0]
    return year >= 1583


def get_split_date(target) -> tuple:
    split_date: list[str] = target.split('-')

    year: int = int(split_date[0])
    month: int = int(split_date[1])
    day: int = int(split_date[2])

    return year, month, day


def is_leap_year(target):
    return (target % 400 == 0) or (target % 4 == 0 and target % 100 != 0)