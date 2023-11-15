from doomsday.algorithm_helper_function import *
from doomsday.does_date_exist import split_date


def get_weekday_for_date(date: str) -> str:
    """Return the weekday from a date

    date has to be of valid format and exist"""

    splitted_date: list[int] = split_date(date)

    year:   int = splitted_date[0]
    month:  int = splitted_date[1]
    day:    int = splitted_date[2]

    doomsday: int = get_year_doomsday(year)

    return "Sunday"
