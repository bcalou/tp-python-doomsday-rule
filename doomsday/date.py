DAYS_PER_MONTH = (
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
)


def is_valid_date(date: str) -> bool:
    """Check if a date is valid. Which means beign 3 numbers separated by "-",
    and that the year, month and day given exist in the Gregorian calendar"""

    if not is_valid_format_date(date):
        return False

    year, month, day = (int(value) for value in date.split("-"))

    if year < 1583:
        print("Years begin from 1583")
        return False

    if (1 > month) or (month > 12):
        print("Month goes from 1 to 12")
        return False

    days_in_this_month: int = get_days_in_month(year, month)

    if (1 > day) or (day > days_in_this_month):
        print("For this month, day goes from 1 to ",
              days_in_this_month)
        return False

    return True


def is_valid_format_date(date: str) -> bool:
    """Verify if a given date is 3 numbers separated by "-" """

    splited_date: list[str] = date.split("-")

    if len(splited_date) != 3:
        print("Date format should be YYYY-MM-dd")
        return False

    for part in splited_date:
        if not part.isdigit():
            print("A date must be composed with numbers")
            return False

    return True


def get_days_in_month(year: int, month: int) -> int:
    """Return the number of days in a month, depending on year"""

    if month == 2:
        return 28 if not is_leap_year(year) else 29

    return DAYS_PER_MONTH[month-1]

def is_leap_year(year: int) -> bool:
    """Verify if a year is a leap year or not"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
