import doomsday


def init():
    """ Initialize the Doomsday sequence """
    message: str = "What is the date? (format YYYY-MM-dd)\n"

    # Reask the question each time the input is invalid
    while True:
        date: str = input(message)
        if doomsday.is_valid_date(date):
            break
        else:
            message = "Please enter a valide date (format YYYY-MM-dd):\n"

    print(doomsday.get_day_for_date(date))


init()
