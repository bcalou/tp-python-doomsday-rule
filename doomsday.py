from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

date_input: str = input("Inserez une date de format YYYY-MM-dd:")

while not is_valid_date(date_input):
    date_input: str = input("Inserez une date de format YYYY-MM-dd:")

day_of_date: str = get_day_for_date(date_input)
print("The day of the date ",date_input," is ", day_of_date )

# Commencez ici !