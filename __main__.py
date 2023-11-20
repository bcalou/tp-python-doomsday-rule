from doomsday.date import is_valid_date
from doomsday.algorithm import get_weekday_for_date

def input_date() -> None:
    """Asks for a date and check if its valid"""
    time_str = str(input("Enter date in this format yyyy-mm-dd \n >>"))
    if is_valid_date(time_str):
        result = get_weekday_for_date(time_str)
        print(f"The day of the week is: {result}")
    else:
        return False

input_date()