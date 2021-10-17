from doomsday.day import DAYS
from doomsday.calculate import calculate_anchor_day
from doomsday.month import month 
from doomsday.leap import is_leap_year
from doomsday.transformate import transform_string_in_date

DAY: int = 0
MONTH: int = 1
YEAR: int = 2

def get_day_for_date(date_input: str) -> str:
    current_month: int 
    doomsday: int
    date: list[int] = transform_string_in_date(date_input)
    if date[MONTH] == month.JANUARY - 1:
        current_month = month.JANUARY
        if is_leap_year(date[YEAR]):
            doomsday = 11
        else:
            doomsday = 10
    elif date[MONTH] == month.FEBRUARY - 1:
        current_month = month.FEBRUARY
        if is_leap_year(date[YEAR]):
            doomsday = 22
        else:
            doomsday = 21
    elif date[MONTH] == month.MARCH - 1:
        current_month = month.MARCH
        doomsday = 0
    elif date[MONTH] == month.APRIL - 1:
        current_month = month.APRIL
        doomsday = 4
    elif date[MONTH] == month.MAY - 1:
        current_month = month.MAY
        doomsday = 9
    elif date[MONTH] == month.JUNE - 1:
        current_month = month.JUNE
        doomsday = 6
    elif date[MONTH] == month.JULY - 1:
        current_month = month.JULY
        doomsday = 11
    elif date[MONTH] == month.AUGUST - 1:
        current_month = month.AUGUST
        doomsday = 8
    elif date[MONTH] == month.SEPTEMBER - 1:
        current_month = month.SEPTEMBER
        doomsday = 5
    elif date[MONTH] == month.OCTOBER - 1:
        current_month = month.OCTOBER
        doomsday = 10
    elif date[MONTH] == month.NOVEMBER - 1:
        current_month = month.NOVEMBER
        doomsday = 7
    elif date[MONTH] == month.DECEMBER - 1:
        current_month = month.DECEMBER
        doomsday = 12
    else:
        doomsday = -1 #error

    anchor_day: str = calculate_anchor_day(date[YEAR])

    print("anchor_day" + str(anchor_day))
    print("doomsday" + str(doomsday))
    print("day" + str(date[DAY]))

    return DAYS[(date[DAY] - doomsday + DAYS.index(anchor_day)) % 7]