from doomsday.date import is_valid_date
from doomsday.algorithm import get_weekday_for_date


# Commencez ici !
def get_date_and_return_day() -> None:
    date: str = input("Give a date in format YYYY-MM-dd, we will give you its day")
    day: str = find_day_of_date(date)
    print(day)


def find_day_of_date(date: str) -> str:
    """Return day of date, if date is valid"""

    day: str = "There is no day corresponding"
    if is_valid_date(date):
        day = get_weekday_for_date(date)

    return day


get_date_and_return_day()
