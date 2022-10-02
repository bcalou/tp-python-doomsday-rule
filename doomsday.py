from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date
import doomsday.utils as utils

utils.init_global_variables()

print("-----------------------------------------------------------------------")
print("          Welcome to the most ass kickin' doomsday calculator")
print("-----------------------------------------------------------------------")

while True:
    print("")
    date: str = input("Enter a date to get the corresponding weekday (YYYY-MM-dd) : ")

    if is_valid_date(date):
        print(f"Weekday for {date} is", get_day_for_date(date))
