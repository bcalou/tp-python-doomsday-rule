def get_century_anchor(year: int) -> int:
    if year % 400 < 100:
        return 2
    if year % 400 < 200:
        return 0
    if year % 400 < 300:
        return 5
    else:
        return 3


def get_day_anchor(year: int) -> int:
    decade: int = year % 100
    is_looped_once: bool = False
    while True:
        if decade % 2 == 0 and is_looped_once == True:
            break
        elif decade % 2 == 1:
            decade += 11
        else:
            decade /= 2
            is_looped_once = True
    if decade % 7 == 0:
        return 0
    return int(7 - (decade % 7))


def get_start_day(day: int, month: int, year: int) -> int:
    start_days: list = [10, 21, 0, 4, 9, 6, 11, 8, 5, 7, 12]
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and (month == 1 or month == 2):
        if month == 1:
            return 11
        elif month == 2:
            return 22
    else:
        return start_days[month - 1]


def get_day_for_date(date_string: str) -> str:

    date_splited: list = date_string.split("-")
    day: int = int(date_splited[2])
    month: int = int(date_splited[1])
    year: int = int(date_splited[0])

    days_of_the_week: list = [
        "Monday", "Tuesday", "Wednesday",  "Thursday", "Friday", "Saturday", "Sunday"]

    anchor_day: int = int(get_day_anchor(year) + get_century_anchor(year)) % 7
    doomsday_date: int = int(
        (day - get_start_day(day, month, year) - anchor_day) % 7)
    print(day - get_start_day(day, month, year))
    return days_of_the_week[doomsday_date]
