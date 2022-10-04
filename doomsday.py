from doomsday.date import is_valid_date
from doomsday.algorithm import get_weekday_for_date

# Ask the user for a date until the input is valid
while True:
    date: str = input("Please enter a YYYY-MM-DD date\n-> ")

    if is_valid_date(date):
        break

print(get_weekday_for_date(date))
