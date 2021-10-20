from doomsday.algorithm import get_day_for_date
from doomsday.date import is_valid_date

while True:
    print("\nEnter a date (Format: YYYY-MM-dd):")
    date_received: str = input()

    if is_valid_date(date_received):
        print("\nThat was a " + get_day_for_date(date_received) + " ! Want to try with another date ? (y/n)")

        if input() == "n":
            print("\nGoodbye !")
            break
    else:
        print("This date does not exist in the gregorian calendar, try again.")
