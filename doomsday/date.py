
def is_valid_date(date: str) -> bool:
    """Check if a date is valid"""

    if not has_year_month_day(date):
        return False

    year, month, day, *trash = date.split('-')
    # Impossible de typer en restant dans les 10 lignes, cela prendrait 3 à 4
    # lignes rien que pour ça...

    if len(trash) != 0 or not is_digit_date(day, month, year):
        return False
    
    if not is_date_possible(int(day), int(month), int(year)):
        return False
    
    return True


def is_leap_year(year: int) -> bool:
    """Return whether this year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_digit_date(day: str, month: str, year: str) -> bool:
    """Returns wether the date is composed of digits"""
    if day.isdigit() and month.isdigit() and year.isdigit():
        return True
    
    print("DateError : La date doit être composée de chiffres séparés par des tirets.")
    return False

def is_date_possible(day: int, month: int, year: int) -> bool:
    """Returns wether the date is possible"""
    days_per_month: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(is_leap_year(year)):
        days_per_month[1] = 29
    
    if 1 <= month <= 12 and year >= 1583 and 1 <= day <= days_per_month[month - 1]:
        return True

    print("DateError : La date ne peut pas exister.")
    return False

def has_year_month_day(date: str) -> bool:
    """Returns wether the date has a year, a month and a day"""
    if len(date.split('-')) != 3:
        print("DateError : La date doit être au format AAAA-MM-JJ")
        return False
        
    return True