from doomsday.tools import is_leap_year


#Let's verify if the inputed date is valid
def is_valid_date(date_input: str) -> bool:
    if not isinstance(date_input, str):
        print("Vous n'avez pas entré votre date au format YYYY-MM-dd")
        return False
    date: list[str] = date_input.split('-')

    if not len(date) == 3 or not (date[0].isnumeric() and date[1].isnumeric() and date[2].isnumeric()):
        print("Vous n'avez pas entré votre date au format YYYY-MM-dd")
        return False

    year: int = int(date[0])
    months: int = int(date[1])
    day: int = int(date[2])
    return (is_existing_date(year, months, day))



#Let's verify if the inputed date does exist
def is_existing_date(year: int, month: int, day: int) -> bool:
    if year < 1583:
        print("Seules les dates à partir de l'année 1583 sont prises en charge.")
        return False
    elif month < 1 or month > 12:
        print("Le mois doit être compris entre 01 et 12.")
        return False
    elif day > get_last_day_of_month(year, month):
        print("Le jour n'existe pas dans le mois")
        return False
    return True


#Check how many days there is in the inputed month
def get_last_day_of_month(year, month) -> int:
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
