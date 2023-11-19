"""Algo permettant de trouver le doomsday"""
from doomsday.date import is_valid_date, year_is_leap_year


def main(date: str) -> str:
    """Fonction principale du TP"""
    can_launch_algo = is_valid_date(date)

    if can_launch_algo:
        print("Date Valide ! ")

    date_list = date.split("-")

    year_str = date_list[0]
    month_str = date_list[1]
    day_str = date_list[2]

    year = int(year_str)
    month = int(month_str)
    day = int(day_str)


    doomsday = anchor_calc(year, month, day)
    return doomsday



def anchor_calc(year: int, month: int, day: int) -> str:
    """Fonction rassemblant toute les étapes de calcul du doomsday"""
    two_last_numbers_year = str(year)[2] + str(year)[3]
    anchor = int(two_last_numbers_year)
    anchor = first_stage(anchor)
    anchor = seven_multiple(anchor)

    # Donne le jour ancre de l'année
    year_anchor = get_year_anchor(anchor, year)
    if year_anchor >= 7:
        year_anchor -= 7

    # Donne le jour sur lequel tombera le jour ancre en
    # fonction du mois et de l'année
    month_anchor = get_month_anchor(month, year)

    final_day = get_user_requested_day(year_anchor, month_anchor, day)

    return get_day_str(final_day)


def get_user_requested_day(year_anchor: int,
                           month_anchor: int, day: int) -> int:
    """Permet d'obtenir la version finale normalisée du jour entré
    par l'utilisateur"""
    final_day = (day - month_anchor) % 7

    final_day = (year_anchor + final_day) % 7

    return final_day


def first_stage(two_last_numbers: int) -> int:
    """Premère étape de l'algo avec les addition de 11 et division 
    par 2"""
    # si il est impair
    if two_last_numbers % 2 != 0:
        # on ajoute 11 et on divise par 2
        two_last_numbers += 11
        two_last_numbers = two_last_numbers // 2
        if two_last_numbers % 2 != 0:
            # si le nombre est de nouveau impair on réajoute 11
            two_last_numbers += 11
    else:
        two_last_numbers = two_last_numbers // 2
        if two_last_numbers % 2 != 0:
            two_last_numbers += 11

    return two_last_numbers


def seven_multiple(anchor: int) -> int:
    """Permet de trouver le mutiple de 7 supérieur le plus proche"""
    anchor = 7 - anchor % 7
    return anchor


def get_year_anchor(anchor: int, year: int) -> int:
    """Permet de connaitre le jour ancre de l'année en fonction 
    du siecle et de le distance au prochain multiple de 7 
    calculé précedement"""
    if 1600 <= year <= 1699 or 2000 <= year <= 2099:
        return anchor + 2
    if 1700 <= year <= 1799 or 2100 <= year <= 2199:
        return anchor + 0
    if 1800 <= year <= 1899 or 2200 <= year <= 2299:
        return anchor + 5
    else:
        return anchor + 3


def get_month_anchor(month: int, year: int) -> int:
    """Permet savoir sur quel jour va tomber le jour ancre 
    en fonction du mois"""
    is_leap_year = year_is_leap_year(year)
    if month == 1:
        if is_leap_year:
            return 11
        else:
            return 10

    if month == 2:
        if is_leap_year:
            return 22
        else:
            return 21

    if month == 3:
        return 0

    if month == 4:
        return 4

    if month == 5:
        return 9

    if month == 6:
        return 6

    if month == 7:
        return 11

    if month == 8:
        return 8

    if month == 9:
        return 5

    if month == 10:
        return 10

    if month == 11:
        return 7

    else:
        return 12


def get_day_str(day: int) -> str:
    """Permet de convertir notre int en un jour de la semaine"""
    if day == 0:
        return "Sunday"
    if day == 1:
        return "Monday"
    if day == 2:
        return "Tuesday"
    if day == 3:
        return "Wednesday"
    if day == 4:
        return "Thursday"
    if day == 5:
        return "Friday"
    if day == 6:
        return "Saturday"
    return ""


def get_weekday_for_date(date: str) -> str:
    """Fonction à laquelle les test feront appel"""
    return main(date)
