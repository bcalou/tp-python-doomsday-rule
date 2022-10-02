# According to:
# https://arxiv.org/ftp/arxiv/papers/1006/1006.3913.pdf

WEEKDAYS = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ]
def get_day_for_date(date) -> str:
    y = int(date.split('-')[0])
    m = int(date.split('-')[1])
    d = int(date.split('-')[2])

    dow = (doomscentury(y) + doomsyear(y) + doomsmonth(y, m, d)) % 7

    return WEEKDAYS[dow]

def doomscentury(year: int) -> int:
    thursday = 4
    c = year / 100 + 1
    return int((((5 * c) + ((c - 1) / 4)) % 7) + thursday) % 7

def doomsmonth(year: int, month: int, day: int) -> int:
    # on whether or not the year of the date is a leap year.
    if month == 1:
        if is_leap_year(year):
            return day - 11
        else:
            return day - 10
    elif month == 2:
        if is_leap_year(year):
            return day - 22
        else:
            return day - 21

    # In March we use the 7th as our reference Doomsday.
    elif month == 3:
        return day - 7

    # Even months after March use the day of the month
    # equal to the month of the year
    elif month % 2 == 0:
        return day - month

    # For the remaining months: "9 to 5 at the 7-11"
    elif month == 5:
        return day - 9
    elif month == 9:
        return day - 5
    elif month == 7:
        return day - 11
    else: # month == 11
        return day - 7

def doomsyear(year):
    x = int(str(year)[2:])
    if x % 2 == 1:
        x = x + 11
    x = x / 2
    if x % 2 == 1:
        x = x + 11
    x = x % 7
    return int((7 - x) % 7)

def is_leap_year(year: int):
    """Returns True if year is a leap year"""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

