from doomsday.day import DAYS
from doomsday.calculate import calculate_anchor_day
from doomsday.month import month 
from doomsday.leap import is_leap_year
from doomsday.transformate import transform_string_in_date

#Several values to easier dates crawling
DAY: int = 0
MONTH: int = 1
YEAR: int = 2

def get_day_for_date(date_input: str) -> str:
    """Return the day after calculating the current day"""
    doomsday: int
    date: list[int] = transform_string_in_date(date_input)
    if date[MONTH] == month.JANUARY:
        if is_leap_year(date[YEAR]):
            doomsday = 11
        else:
            doomsday = 10
    elif date[MONTH] == month.FEBRUARY:
        if is_leap_year(date[YEAR]):
            doomsday = 22
        else:
            doomsday = 21
    elif date[MONTH] == month.MARCH:
        doomsday = 0
    elif date[MONTH] == month.APRIL:
        doomsday = 4
    elif date[MONTH] == month.MAY:
        doomsday = 9
    elif date[MONTH] == month.JUNE:
        doomsday = 6
    elif date[MONTH] == month.JULY:
        doomsday = 11
    elif date[MONTH] == month.AUGUST:
        doomsday = 8
    elif date[MONTH] == month.SEPTEMBER:
        doomsday = 5
    elif date[MONTH] == month.OCTOBER:
        doomsday = 10
    elif date[MONTH] == month.NOVEMBER:
        doomsday = 7
    elif date[MONTH] == month.DECEMBER:
        doomsday = 12
    else:
        doomsday = -1 #error

    anchor_day: str = calculate_anchor_day(date[YEAR])

    return DAYS[(date[DAY] - doomsday + DAYS.index(anchor_day)) % 7]