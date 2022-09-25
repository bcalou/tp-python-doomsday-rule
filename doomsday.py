from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

while True:
    date: str = input("Enter a date to get the corresponding weekday (YYYY-MM-dd) : ")

    if is_valid_date(date):
        print(int_date_list)
        print("Youpi")