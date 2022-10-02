from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date


def main():
    '''Function gathering the algorithm and date script'''

    date = input("Enter a date with this format YYYY-MM-DD:")
    if not is_valid_date(date):
        return
    print(f"The weekday of this date : {get_day_for_date(date)}")
    return


main()