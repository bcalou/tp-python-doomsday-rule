LAST_DAY_OF_MONTH: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def does_date_exist(date: str) -> bool:
    """Verify if the date exist

    date has to be of valid format (YYYY-MM-DD)"""

    splitted_date: list[int] = split_date(date)

    year:   int = splitted_date[0]
    month:  int = splitted_date[1]
    day:    int = splitted_date[2]

    # We support only dates starting from 1583
    if year < 1583:
        print("L'année saisit n'est pas supportée.")
        print("Veuillez saisir au date à partir de 1583-01-01")
        return False

    if not (0 < month < 13):
        print("Le mois saisit n'est pas valide.")
        return False

    if day <= 0:
        print("Le jour saisit n'est pas valide.")
        return False

    if day > LAST_DAY_OF_MONTH[month-1]:
        # If we are in february during a leap year we have 29 days
        if month == 2 and is_leap_year(year) and day <= 29:
            return True

        print("Le jour saisit n'est pas valide.")
        return False

    return True


def is_leap_year(year: int) -> bool:
    """Returns true if year is bisextile"""
    divisable_by_4 = year % 4 == 0
    divisable_by_100 = year % 100 == 0
    divisable_by_400 = year % 400 == 0
    return divisable_by_4 and (not divisable_by_100 or divisable_by_400)


def split_date(date: str) -> list[int]:
    """Splits a date into a list of ints

    date has to be of valid format (YYYY-MM-DD)"""
    # Split the date in three parts using the '-' character
    splitted_date_str: list[str] = date.split("-")

    # Convert the splitted date to ints
    splitted_date_int: list[int] = list(map(int, splitted_date_str))

    return splitted_date_int
