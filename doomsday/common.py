def is_leap_year(year: int) -> bool:
    """ Returns true if it is a leap year """
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
