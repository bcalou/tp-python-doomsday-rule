from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

def ask_date(date: str) -> str:
    
    while(True):
        date = input("Entrer une date au format: YYYY-MM-dd")
        if not is_valid_date(date):
            print("Vous avez commis une erreur de saisie vérifiez bien que le format de la date soit YYYY-MM-dd")
        
        else :
            print("Bien reçu")

        break

    return date

  
