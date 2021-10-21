from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date


def main():
    while True:
        date = input("please input a date of format YYYY-MM-DD: ")
        if is_valid_date(date):
            print("It's {}".format(get_day_for_date(date)))
            break
        else:
            print("Please try again")

main()
