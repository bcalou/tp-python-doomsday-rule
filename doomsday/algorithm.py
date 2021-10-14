from .date import *

# Main function to get the day corresponding to any date formatted as YYYY-MM-dd past the 1583-01-01
# Parameter: the formatted date
# Returns: the corresponding day in letters
def get_day_for_date(date: str) -> str:
    if not is_valid_date(date):
        return "Error"
    date_members = str(date).split("-")
    year = int(date_members[0])
    month = int(date_members[1])
    day = int(date_members[2])
    # Which day on the week the key day is
    anchor_day = get_anchor_day(year)
    # Day of the given month which is the day of the week determined earlier
    key_day = get_key_day(month, year)
    # Number of days to add to the anchor day to be at the given date 
    day_shift = day - key_day
    # Knowing which day is the key day, just adding the day difference gives which day of the week is the given day
    return day_labels[(anchor_day + day_shift) % 7]

# Determines the day of reference for a given month of a year given it is a leap year or not
# Parameter: the month and the year as integers
# Returns: a number, corresponding to a day
def get_key_day(month: int, year: int) -> int:
    # January and february change if the year is a leap year
    if month == 1:
        if is_leap_year(year):
            return 11
        else:
            return 10
    elif month == 2:
        if is_leap_year(year):
            return 22
        else:
            return 21
    elif month == 3:
        return 7
    elif month == 5:
        return 9
    elif month == 9:
        return 5
    elif month == 7:
        return 11
    elif month == 11:
        return 7
    # Other months have the same day as their month index
    else:
        return month

# Determines the anchor day of a year
# Parameter: the year as an integer
# Returns: a number, between 0 and 6
def get_anchor_day(year: int) -> int:
    # Gets the last 2 digits of the year
    rest = year % 100
    if rest % 2 != 0:
        rest += 11
    rest = int(rest / 2)
    if rest % 2 != 0:
        rest += 11
    return (-rest % 7 + get_century_anchor_day(year)) % 7

# Determines the anchor day of the century of a year which is used to calculate the anchor day of a year
# Parameter: the year as an integer
# Returns: a number, between 0 and 6
def get_century_anchor_day(year: int) -> int:
    # Gets the century by removing the last 2 digits of the year
    century = int(year / 100)
    rest = century % 4
    if rest == 0:
        return 2
    elif rest == 1:
        return 0
    elif rest == 2:
        return 5
    else:
        return 3