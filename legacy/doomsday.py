semaine: list[str] = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

# Fonction qui prend une date au format JJ/MM/AAAA
# et qui en déduit le jour de la semaine correspondant
def main():
    date: str = input("Entrez une date au format JJ/MM/AAAA : ")
    print("C'est un",doomsday(date))

def doomsday(date : str) -> str:
    """Calculates the day of the week for a given date (format = JJ/MM/AAAA)"""
    # Gestion d'erreur
    if(
        len(date.split("/")) != 3
        or len(date)!=10
        or not date.split("/")[0].isdigit()
        or not date.split("/")[1].isdigit()
        or not date.split("/")[2].isdigit()
    ):
        raise ValueError("Format invalide. La date doit être au format JJ/MM/AAAA")

    # Contenu de la fonction
    
    jour: int = int(date[ :2])
    mois: int = int(date[3:5])
    siecle: int = int(date[6:8])
    annee: int = int(date[8: ])

    ancre_jour: int = get_anchor_day_of_the_week(get_year_anchor(siecle), annee)
    ancre_mois: int = get_month_anchor(mois, is_leap_year(annee))

    jour_calcule: int = (jour - ancre_mois + ancre_jour)%7

    return semaine[jour_calcule]

def get_anchor_day_of_the_week(year_anchor: int, year: int) -> int:
    """Calculates the anchor day for the given year"""
    if year % 2 == 1 :
        year += 11
    year = year // 2
    if year % 2 == 1 :
        year += 11

    jour_ancre: int = 7 - (year % 7) + year_anchor
    return jour_ancre % 7

def get_month_anchor(mois: int,is_leap_year: bool) -> int:
    """Return the month anchor for the given month"""
    if mois == 1:
        return 10 if is_leap_year else 11
    if mois == 2:
        return 21 if is_leap_year else 22
    if mois == 3:
        return 0
    if mois == 5:
        return 9
    if mois == 7:
        return 11
    if mois == 9:
        return 5
    if mois == 11:
        return 7
    return mois


def is_leap_year(year: int) -> bool:
    """Return whether this year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_year_anchor(siecle: int) -> int:
    """Return the year anchor for the given century"""
    if siecle % 4 == 0 :
        return 2
    if siecle % 4 == 1 :
        return 0
    if siecle % 4 == 2 :
        return 5
    return 3


if __name__ == "__main__":
    main()