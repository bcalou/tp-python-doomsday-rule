from doomsday.algorithm import get_day_for_date
from doomsday.date import is_valid_date

user_date = input("Tape une date : YYYY-MM-DD\n")

while not is_valid_date(user_date):
    print("Date invalide\n")
    user_date = input("Tape une date : YYYY-MM-DD\n")
else:  print("Le jour de la semaine correspondant est: " + get_day_for_date(user_date) + "\n")