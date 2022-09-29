from doomsday.date import is_leap_year


def get_day_for_date(date: str) -> str:
    DAY_NAMES: list[str] = ["Sunday", "Monday", "Tuesday",
                            "Wednesday", "Thursday", "Friday", "Saturday"]
    splited_date: list[str] = date.split("-")

    day: int = int(splited_date[2])
    month: int = int(splited_date[1])
    year: int = int(splited_date[0])

    return DAY_NAMES[find_week_day_index(day, month, year)]


def find_week_day_index(day: int, month: int, year: int) -> int:
    COMMON_DOOMDAYS: list[int] = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    week_day_index: int = get_doomdays_week_index(
        year) + (day - COMMON_DOOMDAYS[month - 1])

    if is_leap_year(year) and month <= 2:
        week_day_index -= 1

    return week_day_index % 7


def get_doomdays_week_index(year: int) -> int:

    year_end = year % 100

    ancor_day = get_ancor_day(year_end)

    next_multiple = get_next_multiple_of(ancor_day, 7)

    return (next_multiple - ancor_day + get_century_offset(year)) % 7


# Filter the last 2 digit of the year where
def get_ancor_day(year_end: int) -> int:
    if year_end % 2 == 1:
        year_end += 11

    year_end //= 2

    if year_end % 2 == 1:
        year_end += 11

    return year_end


def get_next_multiple_of(number: int, multiple: int) -> int:
    next_multiple: int = multiple
    while next_multiple < number:
        next_multiple += multiple
    return next_multiple


def get_century_offset(year: int) -> int:
    offsets: list[int] = [2, 0, 5, 3]
    year = year % 400

    for i in range(4):
        if year < (i + 1) * 100:
            return offsets[i]

    return 0
