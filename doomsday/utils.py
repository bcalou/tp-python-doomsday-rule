def is_leap_year(year: int) -> bool:
    """Return true if the given year is a leap year (29 days in february)"""
    # There is a leap year each 4 years, except if at the start of the century
    # BUT every 400 years, the first year of the century is a leap year anyway
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def get_date_parts(date: str) -> list[int]:
    """Separate date parts and return them as an array of ints"""
    # "1990-02-15".split('-') -> ["1990", "02", "15"]
    date_parts: list[str] = date.split('-')

    year: int = int(date_parts[0])
    month: int = int(date_parts[1])
    day: int = int(date_parts[2])

    return [year, month, day]
