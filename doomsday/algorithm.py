from doomsday.date import is_leap_year


DAYS_OF_WEEK = (
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
    )

PIVOT_DAY_LEAP = (4, 1)

PIVOT_DAY = (3, 0, 0, 4, 2, 6, 4, 1, 5, 3, 0, 5)


def get_weekday_for_date(date: str) -> str:
    """
    Détermine le jour du jugement dernier à partir d'une date donnée
    Format attendu : YYYY-MM-dd
    """

    date_in_list: list[str] = date.split("-")

    year: int = int(date_in_list[0])
    month: int = int(date_in_list[1])
    day: int = int(date_in_list[2])

    # 1re partie : déterminer le jour "ancre" de l'année

    anchor_day: int = get_anchor_day(year)

    # 2e partie : déterminer un jour particulier en fonction du jour ancre

    if is_leap_year(year) and (month == 1 or month == 2):
        return DAYS_OF_WEEK[(day - PIVOT_DAY[month - 1] + anchor_day) % 7]
    else:
        return DAYS_OF_WEEK[(day - PIVOT_DAY[month - 1] + anchor_day) % 7]


def get_anchor_day(year: int) -> int:
    """Détermine le jour 'ancre' d'une année"""

    year_end: int = year % 100  # La fin de l'année
    century: int = int(year / 100)  # Le siècle
    century_value: int = 0  # Le décalage lié au siècle

    # Si fin d'année pair /2, sinon +11 et /2 puis si toujours impair +11
    if year_end % 2 != 0:
        year_end += 11
    year_end //= 2
    if year_end % 2 != 0:
        year_end += 11

    # Obtenir le multiple de 7 supérieur ou égal
    multiple_of_7: int = int(year_end)
    if (multiple_of_7 % 7) != 0:
        multiple_of_7 += 7 - multiple_of_7 % 7

    # Obtenir le décalage du siècle
    century_values = [2, 0, 5, 3]

    century_value = century_values[century % 4]

    return multiple_of_7 - int(year_end) + century_value
