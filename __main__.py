from doomsday.algorithm import get_weekday_for_date
from doomsday.date import is_valid_date


def main():
    while True:
        user_input = input(
            "Please enter a date using the format YYYY-MM-dd : ")

        # Check date input
        if not is_valid_date(user_input):
            continue

        break

    print(
        f"{user_input} was a {get_weekday_for_date(user_input)}")


if __name__ == "__main__":
    main()
