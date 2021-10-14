import doomsday


def init():
    """ Initialize the Doomsday sequence """
    date: str = input("What is the date? (format YYYY-MM-dd)\n")

    # Reask the question each time the input is invalid
    while True:
        if doomsday.is_valid_date(date):
            break
        else:
            date = input("Please enter a valide date:\n")

    print(doomsday.get_day_for_date(date))


init()
