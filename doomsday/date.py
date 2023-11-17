import re
from doomsday.does_date_exist import *


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
    format_match = re.fullmatch(r"\d{4}[-]\d{1,2}[-]\d{1,2}", date)

    return format_match is not None
