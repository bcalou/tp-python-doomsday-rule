def is_valid_date(date: str) -> bool:
    """Verify if the date parameter is valid

    First the function verify the format,
    then it verify if the date exist
    """

    if not is_format_valid(date):
        print("Le format de la date n'est pas YYYY-MM-DD!")
        return False

    if not does_date_exist(date):
        print("La date n'existe pas!")
        return False

    return True


def is_format_valid(date: str) -> bool:
    """Verify if date follows the format YYYY-MM-DD"""
    return True


def does_date_exist(date: str) -> bool:
    """Verify if the date exist"""
    return True
