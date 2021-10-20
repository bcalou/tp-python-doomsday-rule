# Determines if the year is a leap year or not
def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0


# Determines if the day exists for a specified date
def does_day_exist(year: int, month: int, day: int) -> bool:
    MONTHS_WITH_31_DAYS: list[int] = [1, 3, 5, 7, 8, 10, 12]

    if not day >= 1:
        return False

    if month in MONTHS_WITH_31_DAYS:
        return day <= 31
    elif month == 2:
        if is_leap_year(year):
            return day <= 29
        else:
            return day <= 28
    else:
        return day <= 30


# Determines if a date is valid
def is_valid_date(date: str) -> bool:
    # Checks for type, length, and length of each part
    if not type(date) is str:
        return False

    split_date: list[str] = date.split('-')

    if not len(split_date) == 3:
        return False

    year = split_date[0]
    month = split_date[1]
    day = split_date[2]

    if year.isdigit():
        year = int(year)
        if year < 1583:
            return False

    if len(month) == 2 and month.isdigit():
        month = int(month)
        if month > 12 or month < 1:
            return False

    if len(day) == 2 and day.isdigit():
        day = int(day)
        if does_day_exist(year, month, day) is False:
            return False

    # If everything is valid,
    return True
