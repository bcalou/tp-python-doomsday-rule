from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

# Commencez ici !

def main():
    """Main functions that asks the user for a date and returns the
    corresponding weekday
    """

    print("Bienvenue sur le programme qui vous dit quel jour de la semaine vous êtes né.e!")
    date = input("Entrez une date au format AAAA-MM-JJ: ")
    if is_valid_date(date):
        print("Vous êtes né.e un", get_day_for_date(date))
    else:
        print("La date est invalide.")

# Lancer uniquement si le fichier est executé directement, pas si il est importé
if __name__ == "__main__":
    main()