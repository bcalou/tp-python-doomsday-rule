from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date


date = ""
while (not is_valid_date(date)):
    date = input("Enter a date (YYYY-MM-dd):\n")
print(date + " is a " + get_day_for_date(date))
