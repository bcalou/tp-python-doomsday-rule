from doomsday.date import is_valid_date
from doomsday.algorithm import get_weekday_for_date


def main() -> None:
    """Programme principal"""
    print("- Doomsday algorithm -")

    while True:
        date: str = input("Enter a date (expected format : <YYYY-MM-dd>) : ")
        if is_valid_date(date):
            print(get_weekday_for_date(date))
        try_again: str = input("Try another date ? (y/n) : ").lower().strip()
        if try_again != "y":
            break


main()
