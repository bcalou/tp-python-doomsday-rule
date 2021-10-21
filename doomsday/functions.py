def is_leap_year(year: int) -> bool:
    isLeapYear = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
        isLeapYear = True
    return isLeapYear

def get_year(date: str) -> int:
    return int(date[0:4])

def get_month(date: str) -> int:
    return int(date[5:7])

def get_day(date: str) -> int:
    return int(date[8:])