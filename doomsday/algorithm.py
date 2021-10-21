from doomsday.date import is_leap_year


def get_day_for_date(date: str) -> str:
    # returns the day of the week corresponding to the given date
    year, month, day = date.split('-')
    year, month, day = int(year), int(month), int(day)

    anchor_day = (odd_eleven_method(year) + get_century_index(year)) % 7
    day_for_date = (
        day - (get_doomsday_for_month(month, year) - anchor_day)) % 7

    days_names = ["Sunday", "Monday", "Tuesday",
                  "Wednesday", "Thursday", "Friday", "Saturday"]

    return days_names[day_for_date]


def get_doomsday_for_month(month: int, year: int) -> int:
    # returns the doomsday for the given month and year
    doomsdays = [
        10 + is_leap_year(year), 21 + is_leap_year(year), 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    return doomsdays[month - 1]


def get_century_index(year: int) -> int:
    # returns the century index of the given year
    year_modulo = year % 400

    if year_modulo < 100:
        return 2

    if year_modulo < 200:
        return 0

    if year_modulo < 300:
        return 5

    return 3


def odd_eleven_method(year: int) -> int:
    # computes the value needed for the calculation of the anchor day
    year_2_last_numbers: int = year % 100
    if year_2_last_numbers % 2 == 1:
        year_2_last_numbers += 11

    year_2_last_numbers = int(year_2_last_numbers / 2)
    if year_2_last_numbers % 2 == 1:
        year_2_last_numbers += 11

    # X is a temporary variable needed for the calculation
    x = year_2_last_numbers % 7
    multiple = 7 * (x + 1)
    return multiple - year_2_last_numbers
