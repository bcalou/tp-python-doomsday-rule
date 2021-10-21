def is_leap_year(year: int) -> bool:
    """
    check if the year is leap year
    Args:
        year (int): year input
    Returns:
        bool: return True if the year is leap
    """
    isLeapYear = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
        isLeapYear = True
    return isLeapYear

def get_year(date: str) -> int:
    """
    get the year from the input date with the format int
    Args:
        date (str): date input by user
    Returns:
        int: year of the input date
    """    
    return int(date[0:4])

def get_month(date: str) -> int:
    """
    get the month from the input date with the format int
    Args:
        date (str): date input by user
    Returns:
        int: month of the input date
    """   
    return int(date[5:7])

def get_day(date: str) -> int:
    """
    get the day from the input date with the format int
    Args:
        date (str): date input by user
    Returns:
        int: day of the input date
    """   
    return int(date[8:])