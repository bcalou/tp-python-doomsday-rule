

def is_valid_date(date: str) -> bool:
    # Check input length
    splited_date: list[str] = date.split("-")

    if not (len(date) <= 10 or len(date) >= 8) or len(splited_date) != 3:
        return error_message("Format non valide veuillez utiliser le format YYYY-MM-dd ou YYYY-M-d et séparez les jours des mois des année par le caractère `-`")

    # Check if the year input is a number that fits in the gregorian calendar
    if not splited_date[0].isdigit() or is_year_valid(splited_date[0]):
        return error_message("Année non valide veuillez utiliser le format YYYY et verifiez que l'année est valide (superieur a 1582, 1583 est le début du calendrier grégorien).")

    # Check if the month input is a number that is between 1 and 12
    if not (splited_date[1].isdigit() and (is_month_valid(splited_date[1]))):
        return error_message("Mois non valide veuillez utiliser le format MM ou M et verifiez que le mois est valide (1 à 12 si vous ne savez pas).")

    # Check the validity off the
    if is_day_valid(splited_date[2], int(splited_date[1]), int(splited_date[0])):
        return error_message("Jour non valide veuillez utiliser le format dd ou d et verifiez que le jour existe dans le mois choisi.")
    return True


def error_message(message: str) -> bool:
    print("\033[91m❌ " + message + "\033[00m\n")
    return False


def is_year_valid(year: str):
    return int(year) < 1583


def is_month_valid(month: str):
    return int(month) <= 12 and int(month) >= 1


def is_day_valid(day_text: str, month: int, year: int) -> bool:

    USUSAL_DAYS_PER_MONTH: list[int] = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if day is in a valid format
    if not day_text.isdigit():
        return False

    # Check for february and leap year case
    day = int(day_text)

    if is_leap_year(year) and month == 2 and (day <= 29 or day >= 1):
        return True

    # Check for casual cases
    return day <= USUSAL_DAYS_PER_MONTH[month - 1] and day > 1


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0
