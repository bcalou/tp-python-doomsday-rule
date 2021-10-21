

def is_valid_date(user_date: str) -> bool:
    if not isinstance(user_date, str):
        return False
        
    split_date: list[str] = user_date.split("-")
    year_str: str = split_date[0]
    month_str: str = split_date[1]
    day_str: str = split_date[2]
    
    if not is_numeric_date(day_str, month_str, year_str):
        return False
    if len(month_str) != 2 or len(day_str) != 2:
        return False

    year_int: int = int(year_str)
    month_int: int = int(month_str)
    day_int: int = int(day_str)

    if not is_valid_year(year_int):
        return False
    if not is_valid_month(month_int):
        return False
    if not is_valid_day(day_int, month_int, year_int):
        return False
    return True

def is_numeric_date(day: str, month: str, year: str) -> bool:
    if day.isnumeric and month.isnumeric and year.isnumeric:
        return True
    else:
        return False

def is_valid_year(year: int) -> bool:
    if year >= 1583:
        return True
    else:
        return False

def is_valid_month(month: int) -> bool:
    if month > 0 and month <= 12:
        return True
    else:
        return False
    
def is_valid_day(day: int, month: int, year: int) -> bool:
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 0 and day < 32:
        return True
    elif month in [4, 6, 9, 11] and day > 0 and day < 31:
        return True
    elif month == 2:
        if is_leap_year(year) and day > 0 and day < 30:
            return True
        elif not is_leap_year(year) and day > 0 and day < 29:
            return True
        else:
            return False
    else:
        return False

def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)





