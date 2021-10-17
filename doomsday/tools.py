#OUTILS
def is_leap_year(year: int) -> bool:
    leap_year = ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))
    return leap_year
