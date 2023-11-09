from doomsday.algorithm import get_weekday_for_date
from doomsday.date import is_valid_date


def main() -> None:
    """Ask the user for a date and print the corresponding weekday"""
    while True:
        date = input("Please enter a YYYY-MM-DD date\n-> ")

        if is_valid_date(date):
            break

    print(get_weekday_for_date(date))


main()
