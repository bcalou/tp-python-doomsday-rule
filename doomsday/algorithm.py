from doomsday.day import DAYS
from doomsday.calculate import calculate_anchor_day
from doomsday.month import month 
from doomsday.leap import is_leap_year
from doomsday.transformate import transform_string_in_date
from doomsday.values import DAY, MONTH, YEAR


def get_doomsday_from_month(current_month: month, current_year: int):
    if current_month == month.JANUARY:
        return 11 if is_leap_year(current_year) else 10
    elif current_month == month.FEBRUARY:
        return 22 if is_leap_year(current_year) else 21
    else:
        return [0, 4, 9, 6, 11, 8, 5, 10, 7, 12][current_month - 2 -1]# - 2 for JANUARY and FEBRUARY and -1 because month start at 1

def get_day_for_date(date_input: str) -> str:
    """Return the day after calculating the current day"""
    
    date: list[int] = transform_string_in_date(date_input)

    doomsday: int = get_doomsday_from_month(date[MONTH], date[YEAR])

    anchor_day: str = calculate_anchor_day(date[YEAR])

    return DAYS[(date[DAY] - doomsday + DAYS.index(anchor_day)) % 7]