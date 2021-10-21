import re


def is_leap_year(y: int) -> bool:
    """Return True if the year passed in argument is a leap year"""
    return(y % 4 == 0 and y % 100 != 0) or y % 400 == 0


def is_valid_date(date: str) -> bool:
    """Return True if date is at format -> YYYY-MM-dd"""
    month_max_lenght = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", str(date))
    if m is None:
        return False
    if int(m.group("year")) < 1583 or int(m.group("month")) > 12 \
            or int(m.group("day")) > 31:
        return False
    if int(m.group("day")) > month_max_lenght[int(m.group("month")) - 1]:
        return (m.group("month") == "02" and
                is_leap_year(int(m.group("year")))) and m.group(3) == "29"
    return True


def convert_date(date: str) -> list[int]:
    """ Convert date from one chain to 3 ints
    return List[int] as [year, month, day]"""
    splited_date: list[str] = date.split('-')
    return [int(splited_date[0]), int(splited_date[1]), int(splited_date[2])]
