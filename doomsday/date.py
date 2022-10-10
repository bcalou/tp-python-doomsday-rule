"""Multiple functions that allows for date validity testing
"""

def is_valid_date(date: str) -> bool:
    """Check if a date is valid"""

    if not has_year_month_day(date):
        return False

    year: str
    month: str
    day: str

    year, month, day, *trash = date.split('-')

    return (
        len(trash) == 0
        and is_digit_date(day, month, year)
        and is_date_possible(int(day), int(month), int(year))
    )


def is_leap_year(year: int) -> bool:
    """Return whether this year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_digit_date(day: str, month: str, year: str) -> bool:
    """Returns wether the date is composed of digits"""
    if day.isdigit() and month.isdigit() and year.isdigit():
        return True

    print("DateError : The date should be composed of digits separated by dashes.")
    return False

def is_date_possible(day: int, month: int, year: int) -> bool:
    """Returns wether the date can exist"""
    days_per_month: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_per_month[1] = 29

    if 1 <= month <= 12 and year >= 1583 and 1 <= day <= days_per_month[month - 1]:
        return True

    print("DateError : This date can't exist, or is before 1583.")
    return False

def has_year_month_day(date: str) -> bool:
    """Returns wether the date has a year, a month and a day"""
    if len(date.split('-')) != 3:
        print("DateError : The date should respect the format YYYY-MM-DD.")
        return False

    return True

if __name__ == "__main__":
    print("This file isn't executable. Prefer starting 'doomsday.py'.")
