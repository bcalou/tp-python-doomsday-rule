WRONG_FORMAT = "WRONG_FORMAT"
NAN = "NAN"
OK = "OK"


def is_valid_date(date: str) -> str:
    date_split: list[str] = date.split('-')

    if len(date_split) != 3:
        return WRONG_FORMAT

    if not is_valid_ymd(date_split[0], date_split[1], date_split[2]):
        return NAN

    return OK


def is_valid_ymd(year, month, day) -> bool:
    return is_valid_year(year) and is_valid_month(month) and is_valid_day(day)


def is_valid_year(year) -> bool:
    return year.isdigit() and 1583 <= int(year)


def is_valid_month(month) -> bool:
    return month.isdigit() and 1 <= int(month) <= 12


def is_valid_day(day) -> bool:
    return day.isdigit() and 1 <= int(day) <= 31
