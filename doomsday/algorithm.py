from doomsday.date import is_leap_year

def get_weekday_for_date(date: str) -> str:
    """
    Détermine le jour du jugement dernier à partir d'une date donnée
    Format attendu : YYYY-MM-dd
    """

    days_of_week = (
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
        )

    date_in_list: list[str] = date.split("-")

    year: int =  int(date_in_list[0])
    month: int =  int(date_in_list[1])
    day: int =  int(date_in_list[2])

    # 1re partie : déterminer le jour "ancre" de l'année

    anchor_day: int = get_anchor_day(year)

    # 2e partie : déterminer un jour particulier en fonction du jour ancre

    if is_leap_year(year):
        match month:
            case 1:
                return days_of_week[(day - 4 + anchor_day) % 7]
            case 2:
                return days_of_week[(day - 1 + anchor_day) % 7]

    match month:
        case 1:
            return days_of_week[(day - 3 + anchor_day) % 7]
        case 2:
            return days_of_week[(day + anchor_day) % 7]
        case 3:
            return days_of_week[(day + anchor_day) % 7]
        case 4:
            return days_of_week[(day - 4 + anchor_day) % 7]
        case 5:
            return days_of_week[(day - 2 + anchor_day) % 7]
        case 6:
            return days_of_week[(day - 6 + anchor_day) % 7]
        case 7:
            return days_of_week[(day - 4 + anchor_day) % 7]
        case 8:
            return days_of_week[(day - 1 + anchor_day) % 7]
        case 9:
            return days_of_week[(day - 5 + anchor_day) % 7]
        case 10:
            return days_of_week[(day - 3 + anchor_day) % 7]
        case 11:
            return days_of_week[(day + anchor_day) % 7]
        case 12:
            return days_of_week[(day - 5 + anchor_day) % 7]
        case _:
            return ""

def get_anchor_day(year: int) -> int:
    """Détermine le jour 'ancre' d'une année"""

    year_end: float = year % 100 # La fin de l'année
    century: int = int(year / 100) # Le siècle
    century_value: int = 0 # Le décalage lié au siècle

    # Si fin d'année pair /2, sinon +11 et /2 puis si toujours impair +11
    if year_end % 2 != 0:
        year_end += 11
    year_end /= 2
    if year_end % 2 != 0:
        year_end += 11

    # Obtenir le multiple de 7 supérieur ou égal
    multiple_of_7: int = int(year_end)
    while multiple_of_7 % 7 != 0:
        multiple_of_7 += 1

    # Obtenir le décalage du siècle
    match (century % 4):
        case 0: # Dates 1600, 2000, etc.
            century_value = 2
        case 1: # Dates 1700, 2100, etc.
            century_value = 0
        case 2: # Dates 1800, 2200, etc.
            century_value = 5
        case 3: # Dates 1500, 1900, etc.
            century_value = 3

    return multiple_of_7 - int(year_end) + century_value
