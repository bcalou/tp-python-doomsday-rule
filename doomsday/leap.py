def is_leap_year(a:int)-> bool:
    """Return True if year entered is leap"""
    return ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0)