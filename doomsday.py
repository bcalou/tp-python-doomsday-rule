from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date


def ask_date() -> str:
    date: str
    while (True):
        date = input("Please write a valid Gregorian calendar date (YYYY-MM-dd) : ")
        if not is_valid_date(date):
            print("This is not a valid date.")
        else:
            break
    return date


if __name__ == "__main__":
    date = ask_date()
    print(date + " is a " + get_day_for_date(date))

