from doomsday.date import is_valid_date
import doomsday.algorithm as algo

print("Please enter a date under format YYYY-MM-dd")

while True:
    selected_date: str = input()
    if is_valid_date(selected_date):
        break
    print("invalide format")

print("This day was a " + algo.get_day_for_date(selected_date))
