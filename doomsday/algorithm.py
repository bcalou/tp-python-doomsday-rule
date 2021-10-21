
def get_day_for_date(date_string: str) -> str:

    date_splited: list = date_string.split("-")
    day: int = date_splited[O]
    month: int = date_splited[1]
    year: int = date_splited[2]
    memorable_date: int = 0

    days_of_the_week: list = [
        "Monday", "Tuesday", "Wednesday",  "Thursday", "Friday", "Saturday", "Sunday"]

    anchor_days: list = [
        ""]

    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and (month == 1 or month == 2):
        memorable_date =
