def is_leap_year(year: int) -> bool:
    """Return true if the given year is a leap year (29 days in february)

    There is a leap year every 4 years, except at the start of the century
    EXCEPT every 400 years: the first year of the century is a leap year too
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def get_date_parts(date: str) -> tuple[int, int, int]:
    """Separate date parts and return them as a tuple of 3 ints

    Input exemple : "1990-02-15"
    Output : (1990, 2, 15)
    """
    date_parts = tuple(date.split('-'))

    return (int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
