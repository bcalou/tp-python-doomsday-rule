"""Verification de la validité de la date"""
def is_valid_date(date: str) -> bool:
    """Permet de savoir si la date ne présente aucune erreur"""

    date_list = date.split("-")

    if len(date_list) != 3 :
        return False

    year_str = date_list[0]
    month_str = date_list[1]
    day_str = date_list[2]

    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        print("ERREUR : Nous attendons des chiffres")
        return False


    is_leap_year = year_is_leap_year(year)

    if year < 1583 or year > 2400:
        print("ERREUR : l'année est invalide")
        return False

    if month < 0 or month > 12:
        print("ERREUR : Le mois est invalide")
        return False

    if (
        day < 0
        or (
            day > 31
            and (
                month == 1
                or month == 3
                or month == 5
                or month == 7
                or month == 8
                or month == 10
                or month == 12
            )
        )
        or (
            day > 30
            and (
                month == 4 or month == 6 or month == 9 or month == 11
            )
        )
        or (
            (
                (day > 28 and not is_leap_year)
                or (day > 29 and is_leap_year)
            )
            and month == 2
        )
    ):
        print("ERREUR : Le jour est invalide")
        return False

    return True

def year_is_leap_year(year: int) -> bool:
    """Permet de savoir si une année est bissextile"""
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True
