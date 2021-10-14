from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

date: str = input("Pour quelle date souhaitez vous savoir le jour ? ( Format YYYY-MM-dd ) ")

if (is_valid_date(date)):
    print(get_day_for_date(date))