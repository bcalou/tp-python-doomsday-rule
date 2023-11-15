DAYS_PER_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def get_days_per_month(month: int, year: int) -> int:
    """Returns the number of day of the given month,
    accounting for leap years"""

    if (month == 2 and is_leap_year(year)):
        return DAYS_PER_MONTH[month - 1] + 1
    else:
        return DAYS_PER_MONTH[month - 1]


def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year.
    Leap years are every year that are multiples of 4 but not multiples of 100
    or years that are multiple of 400."""

    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def is_valid_date(date: str) -> bool:

    split_date: list[str] = date.split("-")

    # Check for valid number of date components
    if (len(split_date) != 3 or "" in split_date):
        print("Date must be formatted as YYYY-MM-DD")
        return False

    year: int = int(split_date[0])
    month: int = int(split_date[1])
    day: int = int(split_date[2])

    # Years below 1583 are not supported.
    if (year < 1583):
        print("For simplicity, years before 1583 are not supported.")
        return False

    # Check for valid month
    if (month < 1 or month > 12):
        print("Invalid month")
        return False

    # Check for valid day, accounting for leap years.
    if (day < 1 or day > get_days_per_month(month, year)):
        print("Invalid day number for the given date.")
        return False

    return True
