from doomsday.date import is_valid_date
from doomsday.algorithm import get_weekday_for_date

def main() -> None:
    date: str = ask_for_valid_date()
    get_weekday_for_date(date)


def ask_for_valid_date() -> str:
    """Ask for a date until a valid one is given"""

    given_date: str = ""

    while True:
        print("De quelle date souhaitez vous connaître le jour ? (YYYY-MM-dd)")
        given_date = input()
        if is_valid_date(given_date) is True:
            return given_date

main()
