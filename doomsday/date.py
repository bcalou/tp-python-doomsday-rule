from re import match
from doomsday.functions import is_leap_year, get_year, get_month, get_day

def is_valid_date(date: str) -> bool:
    year_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not isinstance(date, str):
        return False
    if not match(r"(\d{4}-\d{1,2}-\d{1,2})", date):
        return False
    else:
        year = get_year(date)
        month = get_month(date)
        day = get_day(date)
        if year < 1583:
            return False
        if month < 1 or month > 12:  
            return False
        if is_leap_year(year):
            year_month[1] = 29
            if day < 1 or day > year_month[month-1]:
                return False
        else:
            if day < 1 or day > year_month[month-1]:
                return False
        return True
    
