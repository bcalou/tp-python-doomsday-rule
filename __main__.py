from doomsday.date import is_valid_date
from doomsday.algorithm import get_weekday_for_date


def main() -> None:
    """Main function asking for a date and displaying its day"""

    date: str = ask_for_valid_date()

    display_weekday_for_date(date, get_weekday_for_date(date))


def ask_for_valid_date() -> str:
    """Ask for a date until a valid one is given"""

    given_date: str = ""

    while True:
        given_date = input("Your date (YYYY-MM-dd):\n")
        if is_valid_date(given_date):
            return given_date


def display_weekday_for_date(date: str, day: str) -> None:
    """Display a sentence saying a date and its day"""

    print(f"{date} is a {day}")


main()
