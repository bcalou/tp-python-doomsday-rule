from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date


def ask_for_date():
    date_input : str = input("Veuillez entrer une date au format YYYY-MM-dd\n->")
    if is_valid_date(date_input) :
        return get_day_for_date(date_input)
    else: 
        return False

while True : 
    date_input = ask_for_date()
    if date_input: 
        print(date_input)
        break
