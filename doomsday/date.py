def is_valid_date(target_date: str) -> bool:
    return False if type(target_date) != str else is_valid_year(target_date) and is_valid_month(target_date) and is_valid_day(target_date) and has_right_number_of_day(target_date)

def is_valid_year(target_date: str) -> bool:
    year: str = target_date[0:4]
    for char in year:
        if char.isnumeric() == False:
            print("Erreur : Un ou plusieurs caractères ne sont pas des chiffres dans l'année")
            return False
    return int(year) > 1583

def is_valid_month(target_date: str) -> bool:
    month: str = target_date[5:7]
    for char in target_date[5:7]:
        if char.isnumeric() == False:
            print("Erreur : Un ou plusieurs caractères ne sont pas des chiffres dans le mois")
            return False
    return int(month) <= 12
    
def is_valid_day(target_date: str) -> bool:
    day: str = target_date[8:]
    for char in day:
        if char.isnumeric() == False:
            print("Erreur : Un ou plusieurs caractères ne sont pas des chiffres dans le jour")
            return False
    return int(day) <= 31 if day[0] != 0 else True

def is_valid_format(target_date: str) -> bool:
    print("Erreur : La date n'est pas au bon format")
    return target_date[4] == "-" and target_date[7] == "-"

def is_leap_year(year: str) -> bool:
    year_numeric: int = int(year)
    return (year_numeric % 400 == 0) or (year_numeric % 4 == 0 and year_numeric % 100 != 0)

def has_right_number_of_day(target_date: str) -> bool:
    if is_valid_day(target_date) == False or is_valid_month(target_date) == False:
        return False
    day: str = target_date[8:]
    month: str = target_date[5:7]
    year: str = target_date[0:4]
    if month == "02" and is_leap_year(year):
        return int(day) <= 29 if day[0] != 0 else True
    elif month == "02" and is_leap_year(year) == False:
        return int(day) <= 28 if day[0] != 0 else True
    elif month == "04" or month == "06" or month == "09" or month == "11":
        return int(day) <= 30 if day[0] != 0 else True
    else:
        return int(day) <= 31 if day[0] != 0 else True
