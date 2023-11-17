DAYS_PER_MONTH = (
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
)

def is_valid_date(date: str) -> bool:
    """Check if a date is valid. Which means beign 3 numbers separated by "-",
    and that the year, month and day given exist in the Gregorian calendar"""

    if is_valid_format_date(date) is False:
        return False

    year, month, day = (int(value) for value in date.split("-"))

    if year < 1583:
        print("Les dates ne sont prises en compte qu'à partir de 1583")
        return False

    if (1 > month) or (month > 12):
        print("Les mois ne vont que de 1 à 12")
        return False

    days_in_this_month: int = days_in_month(year, month)

    if (1 > day) or (day > days_in_this_month):
        print("Pour le mois renseigné, les jours vont de 1 à ",
               days_in_this_month)
        return False

    return True

def is_valid_format_date(date: str) -> bool:
    """Verify if a given date is 3 numbers separated by "-" """

    splited_date: list[str] = date.split("-")

    if len(splited_date) != 3:
        print("La date doit être au format YYYY-MM-dd")
        return False

    for part in splited_date:
        if part.isdigit() is False:
            print("La date ne peut contenir que des nombres")
            return False

    return True


def days_in_month(year: int, month: int) -> int:
    """Return the number of days in a month, depending on year"""

    #Test if a year is a leap year for february
    if month == 2:
        return 29 if year % 4 == 0 and (
            year % 100 != 0 or year % 400 == 0) else 28

    return DAYS_PER_MONTH[month-1]
