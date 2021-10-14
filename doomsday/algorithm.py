from doomsday.date import *

# Main function to get the day corresponding to any date formatted as YYYY-MM-dd past the 1583-01-01
# Parameter: the formatted date
# Returns: the corresponding day in letters
def get_day_for_date(date: str) -> str:
    return "Monday"

# Determines the number which is used to calculate the key date of a year
# Parameter: the year as an integer
# Returns: a number, either 2, 0, 5 or 3
def get_century_beacon(year: int) -> int:
    # Gets the 
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