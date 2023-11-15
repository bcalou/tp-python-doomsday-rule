from doomsday.date import *


def main() -> None:
    date = input("Veuillez saisir une date au format YYYY-MM-DD: ")

    if is_valid_date(date):
        print("Date valide!")
        # Exécuter l'algorithme
    else:
        print("Erreur")


main()
