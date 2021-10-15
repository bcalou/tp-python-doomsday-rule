from .date import is_leap
from .utils import get_split_date


def get_day_for_date(date: str) -> str:
    year, month, day = get_split_date(date)

    years_anchor: int = get_years_anchor_day(year)
    doomsday: int = get_doomsday(month, year)

    final_day: int = (years_anchor - doomsday + day) % 7
    return get_day_str(final_day)


def get_years_anchor_day(year: int) -> int:
    # ex: 1923 -> 19
    century: int = int(year / 100)
    # ex: 1923 -> 23
    year_in_century: int = year - (century * 100)

    century_tag: int = get_century_tag(century)

    # years_anchor_day = (century_tag + Z + R + L) % 7
    # Z : year_in_century / 12 because anchor day increases every 12 years
    # R : the rest of that division
    # L : number of leap years between year_in_century and 12
    return (century_tag + int(year_in_century / 12) + year_in_century % 12 +
            int((year_in_century % 12) / 4)) % 7


def get_century_tag(century: int) -> int:
    return [2, 0, 5, 3][century % 4]


def get_doomsday(month: int, year: int) -> int:
    return [(3, 4)[is_leap(year)], (0, 1)[is_leap(year)],
            0, 4, 9, 6, 11, 8, 5, 10, 7, 12][month-1]


def get_day_str(day: int) -> str:
    return ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"][day]

