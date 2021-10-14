import math


def pair(number):
    """Returns True if the number is pair"""
    return number % 2 == 0


def get_year_day(year: int) -> int:
    """ Returns the anchor day name for a year (0 for sunday, 1 for monday, etc...) """
    century_tag: int = get_century_tag(year)
    res: int = year % 100
    if not pair(res):
        res += 11
    res //= 2
    if not pair(res):
        res += 11
    cpt: int = 0
    while (cpt + res) % 7 != 0:
        cpt += 1
    res = cpt + century_tag
    res = res % 7
    return res


def get_anchoring_day(year: int, month: int) -> int:
    """ Returns the anchor day for a month and a year (10 or 11 for january, 21 for february, etc...) """
    anchoring_days: list = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    if is_leap_year(year):
        anchoring_days[0] = 11
        anchoring_days[1] = 22
    return anchoring_days[month - 1]


def get_century_tag(year):
    """ Returns the century tag """
    tags: list = [2, 0, 5, 3]
    index: int = math.floor(year/100) % 4
    return tags[index]


def is_leap_year(annee):
    """ Returns true if it is a leap year """
    return annee % 4 == 0 and ((annee % 100 + annee % 400 == 0) or annee % 100 != 0)


def get_day_name(day: int) -> str:
    """ Returns a day name for an index (sunday for 0) """
    return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][day]


def get_day_for_date(date: str) -> str:
    """ Returns the day name for a date in "YYYY-MM-dd" format """
    date_list: list = date.split("-")
    day: int = int(date_list[2])
    month: int = int(date_list[1])
    year: int = int(date_list[0])

    year_day: int = get_year_day(year)
    anchoring_day: int = get_anchoring_day(year, month)

    if (day > anchoring_day):
        while (day > anchoring_day):
            day -= 7
    elif (day < anchoring_day):
        while (day < anchoring_day):
            day += 7

    return get_day_name(((day - anchoring_day + year_day) % 7))
