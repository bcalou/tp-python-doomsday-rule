from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date


def ask_for_date():
    date_input: str = input("Veuillez entrer une date au format YYYY-MM-dd\n->")
    while not is_valid_date(date_input):
        date_input: str = input("Veuillez entrer une date au format YYYY-MM-dd\n->")
    print(get_day_for_date(date_input))

ask_for_date()
