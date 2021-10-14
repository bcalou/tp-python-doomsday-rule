
date: str = input("Entrez une date au format 'YYYY-MM-dd' ")

def is_valid_date(date: str) -> bool:
    return False

def is_valis_year(date: str) -> bool:
    year: str = ""
    for char in date[:4]:
        if char.isnumeric() == False:
            return False
        else:
            year = year + char
    if int(year) > 1583:
        return True
    return False

def is_valid_month(date: str) -> bool:
    month: str = ""
    for char in date[4:]
    