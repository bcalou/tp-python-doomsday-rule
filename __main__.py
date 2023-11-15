from doomsday.algorithm import get_weekday_for_date
from doomsday.date import is_valid_date


def main() -> None:
    user_input = input("Please enter a date in the format YYYY-MM-dd: ")

    if is_valid_date(user_input):
        print(f"The weekday for {user_input} is: {get_weekday_for_date(user_input)}")
    else:
        print("Error: The date is not valid.")


main()
