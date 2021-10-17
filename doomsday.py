from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

# date_input: str = input("Enter a date in format YYYY-MM-dd:\n")
# print("Date Valide") if is_valid_date(date_input) else print("Date Invalide")

print(get_day_for_date("2021-02-20"))
if get_day_for_date("2021-02-20") != "Saturday":
    print('\033[91m❌ Date for 2021-02-20 should be Saturday')
