from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

date_input: str = input("Enter a date in format YYYY-MM-dd:\n")

while not is_valid_date(date_input):
    print("Bad format.. ")
    date_input: str = input("Enter a date in format YYYY-MM-dd:\n")

print("This will be a " + get_day_for_date(date_input))