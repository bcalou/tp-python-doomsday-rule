from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

def main():
    """Main functions that asks the user for a date and returns the
    corresponding weekday
    """

    print("Welcome to the app that tells you the weekday of a date!")
    input_date = input("Please enter a date at the format YYYY-MM-DD: ")
    if not is_valid_date(input_date):
        return

    print("It's a", get_day_for_date(input_date))

# Start only if the file is directly executed
if __name__ == "__main__":
    main()