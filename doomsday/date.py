from typing import Match


def is_valid_date(date) -> bool:
    date = str(date)

    if len(date) != 10:
        print("YYYY-MM-dd format must contain 10 characters")
        return False

    date = date.split('-')

    if len(date) != 3:
        print("YYYY, MM & dd must be separated by hymens")
        return False

    year, month, day = date[0], date[1], date[2]

    if not (year + month + day).isnumeric():
        print("YYYY, MM & dd must be numerics")
        return False

    year, month, day = int(year), int(month), int(day)

    return is_coherent_date(year, month, day)


def is_coherent_date(year: int, month: int, day: int) -> bool:
    if year < 1583:
        print("Year must be earlier than 1583")

    elif month <= 0 or month > 12:
        print("Month must be between 1 and 12")

    elif day < 0:
        print("Day must be positive")

    elif day > day_count_in_month(month, year):
        print("Day too high")

    else:
        return True

    return False


def is_leap_year(year: int) -> bool:
    if(year % 400 != 0):
        return year % 4 == 0 if year % 100 != 0 else False
    return True


def day_count_in_month(month: int, year: int) -> int:
    month_31_list = [1, 3, 5, 7, 8, 10, 12]
    for month_31 in month_31_list:
        if month == month_31:
            return 31

    month_30_list = [4, 6, 9, 11]
    for month_30 in month_30_list:
        if month == month_30:
            return 30

    return 29 if is_leap_year(year) else 28
