

def is_valid_date(user_date: str) -> bool:
    if not isinstance(user_date, str):
        return False
        
    date_split: list[int] | None = split_date(user_date)
    if date_split:
        if not is_valid_year(date_split[0]):
            return False
        if not is_valid_month(date_split[1]):
            return False
        if not is_valid_day(date_split[2], date_split[1], date_split[0]):
            return False
        else: 
            return True
    return False

def split_date(date: str) -> list[int] | None:
    split_date: list[str] = date.split("-")
    year_str: str = split_date[0]
    month_str: str = split_date[1]
    day_str: str = split_date[2]
    if not is_numeric_date(day_str, month_str, year_str):
        return None
    year_int: int = int(year_str)
    month_int: int = int(month_str)
    day_int: int = int(day_str)
    date_split: list[int] = [year_int, month_int, day_int]
    return date_split

def is_numeric_date(day: str, month: str, year: str) -> bool:
    return day.isnumeric() and month.isnumeric() and year.isnumeric()

def is_valid_year(year: int) -> bool:
    return year >= 1583

def is_valid_month(month: int) -> bool:
    return month > 0 and month <= 12

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





