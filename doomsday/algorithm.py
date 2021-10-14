from doomsday.date import is_leap_year


def get_day_for_date(date: str) -> str:
    date_split = date.split('-')
    year, month, day = date_split[0], date_split[1], date_split[2]
    year, month, day = int(year), int(month), int(day)

    anchor_day = (odd_eleven_method(year) + get_century_index(year)) % 7
    day_for_date = (
        day - (get_doomsday_for_month(month, year) - anchor_day)) % 7

    if day_for_date == 0:
        return "Sunday"

    if day_for_date == 1:
        return "Monday"

    if day_for_date == 2:
        return "Tuesday"

    if day_for_date == 3:
        return "Wednesday"

    if day_for_date == 4:
        return "Thursday"

    if day_for_date == 5:
        return "Friday"

    return "Saturday"


def get_doomsday_for_month(month: int, year: int) -> int:
    if month == 1:
        return 11 if is_leap_year(year) else 10

    if month == 2:
        return 22 if is_leap_year(year) else 21

    if month == 3:
        return 0

    if month == 5:
        return 9

    if month == 7:
        return 11

    if month == 9:
        return 5

    if month == 11:
        return 7

    # for even months other than February, doomsday is when the day
    # is the number of the month : 4/4; 6/6; 8/8; 10/10; 12/12
    return month


def get_century_index(year: int) -> int:
    year_modulo = year % 400
    if year_modulo < 100:
        return 2
    if year_modulo < 200:
        return 0
    if year_modulo < 300:
        return 5
    return 3


def odd_eleven_method(year: int) -> int:
    year_2_last_numbers: int = year % 100
    if year_2_last_numbers % 2 == 1:
        year_2_last_numbers += 11
    year_2_last_numbers = int(year_2_last_numbers / 2)
    if year_2_last_numbers % 2 == 1:
        year_2_last_numbers += 11
    # X is a temporary variable needed for the calculation
    X = year_2_last_numbers % 7
    Multiple = 7 * (X + 1)
    return Multiple - year_2_last_numbers
