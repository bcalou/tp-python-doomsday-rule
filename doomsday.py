from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

from doomsday.calculate import calculate_anchor_day

# date_input: str = input("Enter a date in format YYYY-MM-dd:\n")
# print("Date Valide") if is_valid_date(date_input) else print("Date Invalide")

# print(get_day_for_date("2021-02-20"))
# if get_day_for_date("2021-02-20") != "Saturday":
#     print('\033[91m❌ Date for 2021-02-20 should be Saturday')


print(calculate_anchor_day(2021)+"------------------")#dimanche
print(calculate_anchor_day(2020)+"------------------")#samedi!
print(calculate_anchor_day(2002)+"------------------")#jeudi!
print(calculate_anchor_day(2001)+"------------------")#merdredi
print(calculate_anchor_day(2000)+"------------------")#mardi
print(calculate_anchor_day(1999)+"------------------")#dimanche
print(calculate_anchor_day(1998)+"------------------")#samedi!

