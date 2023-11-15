from doomsday.date import is_valid_date


def main() -> None:
    user_input = input("Please enter a date in the format YYYY-MM-dd: ")

    if is_valid_date(user_input):
        print("The date is valid.")
    else:
        print("Error: The date is not valid.")


main()
