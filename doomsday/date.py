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

    date_in_list: list[str] = date.split("-")

    # Vérifier que la chaîne en paramètre est de format str-str-str
    if len(date_in_list) != 3:
        print("Please use format YYYY-MM-dd")
        return False

    year: str = date_in_list[0]
    month: str = date_in_list[1]
    day: str = date_in_list[2]

    # Si le l'année, le mois et le jour sont valides, retourne Vrai
    return is_valid_year(year) and is_valid_month(month) and is_valid_day(day, month, year)

def is_valid_year(year: str) -> bool:
    """ Retourne 'vrai' si l'année est valide"""
    # Vérifier que l'année soit composée de chiffres
    if not year.isnumeric():
        print("Year is not numeric format")
        return False

    # Vérifier si le nombre de caractère est bon (voir ci-haut)
    if len(year) < 4:
        print("Year must have 4 or more characters")
        return False

    # Vérifier que l'année soit postérieure à 1583
    if int(year) < 1583:
        print("Year must begin after 1583")
        return False

    return True

def is_valid_month(month: str) -> bool:
    """ Retourne 'vrai' si le mois est valide"""
    # Vérifier que le mois soit composé de chiffres
    if not month.isnumeric():
        print("Year is not numeric format")
        return False

    # Vérifier si le nombre de caractère est bon (voir ci-haut)
    if len(month) < 1 or len(month) > 2:
        print("Month must have 1 or 2 characters")
        return False

    # Vérifier si le mois existe
    if int(month) > 12:
        print("Month must be between 1 (january) and 12 (december)")
        return False

    return True

def is_valid_day(day: str, month: str, year: str) -> bool:
    """ Retourne 'vrai' si le jour est valide"""
    # Vérifier que le jour soit composé de chiffres
    if not day.isnumeric():
        print("Day is not numeric format")
        return False

    # Vérifier si le nombre de caractère est bon (voir ci-haut)
    if len(day) < 1 or len(day) > 2:
        print("Day must have 1 or 2 characters")
        return False

    # Vérifier que le jour existe
    if int(month) == 2 and is_leap_year(int(year)) and int(day) > 29:
        print("Day must be between 1 and 29")
        return False
    if int(month) == 2 and not is_leap_year(int(year)) and int(day) > 28:
        print("Day must be between 1 and 28")
        return False
    if int(month)%2 == 1 and int(day) > 31:
        print("Day must be between 1 and 31")
        return False
    if int(month)%2 == 0 and int(day) > 30:
        print("Day must be between 1 and 30")
        return False

    return True

def is_leap_year(year: int) -> bool:
    """Renvoie 'vrai' si l'année en paramètre est bissextile"""
    return (year%400 == 0) or (year%4 == 0 and year%100 !=0)
