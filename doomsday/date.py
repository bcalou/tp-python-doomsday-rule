def is_valid_date(target_date: str) -> bool:
    if type(target_date) == str:
        year: str = target_date[0:4]
        month: str = target_date[5:7]
        day: str = target_date[8:]
        return is_valid_year(year) and is_valid_month(month) and is_valid_day(day) and has_right_number_of_day(year, month, day) and is_valid_format(target_date)
    else:
        return False

def is_valid_year(year: str) -> bool:
    if year.isnumeric() == False:
        print("Erreur : Un ou plusieurs caractères ne sont pas des chiffres dans l'année")
        return False
    return int(year) > 1583

def is_valid_month(month: str) -> bool:
    if month.isnumeric() == False:
        print("Erreur : Un ou plusieurs caractères ne sont pas des chiffres dans le mois")
        return False
    return int(month) <= 12
    
def is_valid_day(day: str) -> bool:
    if day.isnumeric() == False:
        print("Erreur : Un ou plusieurs caractères ne sont pas des chiffres dans le jour")
        return False
    return int(day) <= 31 and int(day) > 0

def is_valid_format(target_date: str) -> bool:
    if target_date[4] != "-" or target_date[7] != "-":
        print("Erreur : La date n'est pas au bon format")
        return False
    else:
        return target_date[4] == "-" and target_date[7] == "-"

def is_leap_year(year: str) -> bool:
    year_numeric: int = int(year)
    return (year_numeric % 400 == 0) or (year_numeric % 4 == 0 and year_numeric % 100 != 0)

def has_right_number_of_day(year: str, month: str, day: str) -> bool:
    if not is_valid_day(day) or not is_valid_month(month):
        return False
    if month == "02" and is_leap_year(year):
        return int(day) <= 29 if day[0] != 0 else True
    elif month == "02" and is_leap_year(year) == False:
        return int(day) <= 28 if day[0] != 0 else True
    elif month == "04" or month == "06" or month == "09" or month == "11":
        return int(day) <= 30 if day[0] != 0 else True
    else:
        return int(day) <= 31 if day[0] != 0 else True
