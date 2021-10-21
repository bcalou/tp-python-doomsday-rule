import math
from doomsday.functions import is_leap_year, get_year, get_month, get_day

def get_day_for_date(date: str) -> str:
    DAYS_OF_WEEK = [
                    "Sunday", "Monday", "Tuesday", 
                    "Wednesday", "Thursday", "Friday", "Saturday"
    ]
    DOOMSDAY_LEAP_YEAR = [4, 1, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
    DOOMSDAY_NORMAL_YEAR = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
    year = get_year(date)
    month = get_month(date)
    day = get_day(date)
    dooms_day = get_dooms_day(year)
    if is_leap_year(year):
        ancre_date = DOOMSDAY_LEAP_YEAR[month - 1]
    else:
        ancre_date = DOOMSDAY_NORMAL_YEAR[month - 1]
    week_day = (dooms_day + day - ancre_date) % 7
    return DAYS_OF_WEEK[week_day]

def get_dooms_day(year: int) -> int:
    """
    return the doomsday of the input year
    Args:
        year (int): year of the input date
    Returns:
        int: doomsday of the input year
    """    
    century = math.floor(year / 100)
    ancre_date_of_century = (5 * (century % 4) + 2) % 7
    century_rest = year % 100
    century_rest_m = century_rest % 12
    dooms_day = (
        ((math.floor(century_rest / 12)) + (math.floor(century_rest_m / 4) + 
         century_rest_m) + ancre_date_of_century) % 7)
    return dooms_day