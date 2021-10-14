from doomsday.date import is_valid_date, is_valid_format

def ask_for_date() :
    date_input : str = input("Veuillez entrer une date au format YYYY-MM-dd\n->")

    while not is_valid_date(date_input) :
        date_input : str = input("Veuillez entrer une date au format YYYY-MM-dd\n->")
