from doomsday.algorithm import get_day_for_date
from doomsday.date import is_valid_date


while True:
    date = input("Insert a date in the format 'YYYY-MM-dd' : ")
    if(is_valid_date(date)):
        print("The day for the date " + date + " is " + get_day_for_date(date))
    break
