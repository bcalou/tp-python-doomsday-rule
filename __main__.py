from doomsday.date import *
from doomsday.algorithm import *


def main() -> None:
    date = input("Veuillez saisir une date au format YYYY-MM-DD: ")

    if is_valid_date(date):
        print(f"Le {date} est un {get_weekday_for_date(date)}.")
    else:
        print("Erreur")


main()
