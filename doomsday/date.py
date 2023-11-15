def is_valid_date(date: str) -> bool:
    """
    Retourne 'vrai' si la date est valide
        Format attendu : "YYYY-MM-dd"
        Exeptions : - jour : 1 caractère accepté
                    - mois : 1 caractère accepté
                    - année : 4+ caractères acceptés
        Date minimale : 1583-01-01
    Affiche une explication si erreur
    """
    print("Tested date : " + date)

    date_in_list: list[str] = date.split("- ")

    print("test" + date_in_list[0])

    # Vérifier que la chaîne en paramètre est de format str-str-str
    if not len(date_in_list) == 3:
        print("Please use format YYYY-MM-dd")
        return False
    # Vérifier si la date est composée de chiffres (0-9)
    
    if not date_in_list[0].isnumeric():
        print("Year is not numeric format")
        return False
    if not date_in_list[1].isnumeric():
        print("Month is not numeric format")
        return False
    if not date_in_list[2].isnumeric():
        print("Day is not numeric format")
        return False
    
    year: int =  int(date_in_list[0])
    month: int =  int(date_in_list[1])
    day: int =  int(date_in_list[2])
    
    # Vérifier si le nombre de caractère est bon (voir ci-haut)
    if len(date_in_list[0]) < 4:
        print("Year must have 4 or more characters")
        return False
    if 0 > len(date_in_list[1]) > 2:
        print("Month must have 1 or 2 characters")
        return False
    if 0 > len(date_in_list[2]) > 2:
        print("Day must have 4 or more characters")
        return False
    
    # Vérifier que la date est postérieure à 1583
    if year < 1583:
        print("Year must begin after 1583")
        return False
    
    # Vérifier si le mois existe
    if 0 > month > 13:
        print("Month must be between 1 (january) and 12 (december)")
        return False

    # Vérifier si le jour existe
    if month == 2 and is_leap_year(year) and 0 > day > 29:
        print("Day must be between 1 and 29")
        return False
    if month == 2 and not is_leap_year(year) and 0 > day > 30:
        print("Day must be between 1 and 28")
        return False
    if month%2 == 1 and 0 > day > 32:
        print("Day must be between 1 and 32")
        return False
    if month%2 == 0 and 0 > day > 31:
        print("Day must be between 1 and 31")
        return False

    return True
    
def is_valid_year(date: int) -> bool:
    """ Retourne 'vrai' si l'année est valide"""
    return True

def is_valid_month(date: int) -> bool:
    """ Retourne 'vrai' si le mois est valide"""
    return True

def is_valid_day(date: int) -> bool:
    """ Retourne 'vrai' si le jour est valide"""
    return True

def is_leap_year(year: int) -> bool:
    """Renvoie 'vrai' si l'année en paramètre est bissextile"""

    return True if (year%400 == 0) or (year%4 == 0 and year%100 !=0) else False