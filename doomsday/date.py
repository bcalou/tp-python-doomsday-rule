import re


def is_leap(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_max_month(month: int, year: int) -> int:
        if int(month) in [1, 3, 5, 7, 8, 10, 12]:
            return 31

        elif int(month) == 2:
            return (28, 29)[is_leap(int(year))]

        else:
            return 30


def is_valid_date(date: str) -> bool:
    # verify if the format is the good one
    date_format = re.search(r'(\d+-\d+-\d+)', str(date))
    if date_format is None or date_format.group(0) != date:
        return False

    # Verify if the date is the good one
    year, month, day = date.split("-")

    # look if the year is a standart calendar Gregorian
    if int(year) < 1583:
        return False

    if int(month) not in range(1, 13):
        return False

    if int(day) not in range(1, day_max_month(int(month), int(year)) + 1):
        return False

    return True
