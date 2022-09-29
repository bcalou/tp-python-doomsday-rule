WEEK: tuple = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def get_day_for_date(date: str) -> str:
    """Return the day of the week for the given date (format = YYYY-MM-DD)"""

    year, month, day = date.split("-")
    
    siecle: int = int(year) // 100
    annee: int = int(year) % 100
    mois: int = int(month)
    jour: int = int(day)


    anchor_weekday: int = get_anchor_weekday(get_year_bonus(siecle), annee)
    month_anchor: int = get_month_anchor(mois, is_leap_year(siecle*100 + annee))

    jour_calcule: int = (anchor_weekday + (jour - month_anchor)) % 7
    return WEEK[jour_calcule]

def get_anchor_weekday(year_bonus: int, year: int) -> int:
    """Calculates the anchor day for the given year"""
    if year % 2 == 1:
        year += 11
    year = year // 2
    if year % 2 == 1:
        year += 11

    jour_ancre: int = (7 - (year % 7)) + year_bonus
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
        return 11 if is_leap_year else 10
    if mois == 2:
        return 22 if is_leap_year else 21
    return 0

def is_leap_year(year: int) -> bool:
    """Return whether this year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_year_bonus(siecle: int) -> int:
    """Return the number to add for the given century"""
    if siecle % 4 == 0:
        return 2
    if siecle % 4 == 1:
        return 0
    if siecle % 4 == 2:
        return 5
    return 3

if __name__ == "__main__":
    print("Ce fichier n'est pas le script principal. Lancez 'doomsday.py'.")