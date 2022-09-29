SEMAINE: tuple = ("Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi")

def get_day_for_date(date: str) -> str:
    """Return the day of the week for the given date (format = YYYY-MM-DD)"""

    jour: int = int(date[ :2])
    mois: int = int(date[3:5])
    siecle: int = int(date[6:8])
    annee: int = int(date[8: ])

    anchor_weekday: int = get_anchor_weekday(get_year_anchor(siecle), annee)
    ancre_mois: int = get_month_anchor(mois, is_leap_year(annee))

    jour_calcule: int = (jour - ancre_mois + anchor_weekday) % 7

    return SEMAINE[jour_calcule]

def get_anchor_weekday(year_anchor: int, year: int) -> int:
    """Calculates the anchor day for the given year"""
    if year % 2 == 1:
        year += 11
    year = year // 2
    if year % 2 == 1:
        year += 11

    jour_ancre: int = 7 - (year % 7) + year_anchor
    return jour_ancre % 7

def get_month_anchor(mois: int,is_leap_year: bool) -> int:
    """Return the month anchor for the given month"""
    if mois <= 3:
        return special_month_cases(mois, is_leap_year)
    if mois == 5 or mois == 9:
        return 14 - mois # On inverse mai et septembre
    if mois == 7 or mois == 11:
        return 18 - mois # On inverse juillet et novembre
    return mois # Les autres mois correspondent à leur jour ancre

def special_month_cases(mois: int, is_leap_year: bool) -> int:
    """Completes get_month_anchor for special cases (the first 3 months)"""
    if mois == 1:
        return 10 if is_leap_year else 11
    if mois == 2:
        return 21 if is_leap_year else 22
    return 0

def is_leap_year(year: int) -> bool:
    """Return whether this year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_year_anchor(siecle: int) -> int:
    """Return the year anchor for the given century"""
    if siecle % 4 == 0:
        return 2
    if siecle % 4 == 1:
        return 0
    if siecle % 4 == 2:
        return 5
    return 3

if __name__ == "__main__":
    print("Ce fichier n'est pas le script principal. Lancez 'doomsday.py'.")