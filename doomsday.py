from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date
from doomsday.constants import *


while True:
    date: str = input("Enter a date in the YYYY-MM-DD format")

    date_checker = is_valid_date(date)

    if date_checker == OK:
        break
    elif date_checker == WRONG_FORMAT:
        print("Wrong format, please repeat")
    elif date_checker == NAN:
        print("Wrong digits are be entered, please repeat")
    else:
        print("Unknown error, please repeat")

print(f"The day of this date is {get_day_for_date(date)}")