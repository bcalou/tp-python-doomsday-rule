from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date
from doomsday.algorithm import doomsday

day=" "
date=""
print("For wich date would you like to have the day? \nVWrite it in format 'AAAA-MM-dd'")
date=input()
if (is_valid_date(date)) :
    day=doomsday(date)
    print("The "+ date + " was a " + day)
else :
    print("Date is not valid.")