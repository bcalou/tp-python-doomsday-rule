from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

while True:
    date: str = input("Pour quelle date souhaitez vous savoir le jour ? ( Format YYYY-MM-dd ) ")
    if is_valid_date(date):
        break

print(date + " was a " + get_day_for_date(date))
