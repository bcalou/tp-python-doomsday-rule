from doomsday.date import is_leap_year


#
def get_day_for_date(date: str) -> str:
    DAY_NAMES: list[str] = ["Sunday", "Monday", "Tuesday",
                            "Wednesday", "Thursday", "Friday", "Saturday"]

    splited_date: list[str] = date.split("-")

    day: int = int(splited_date[2])
    month: int = int(splited_date[1])
    year: int = int(splited_date[0])

    return DAY_NAMES[get_day_for_date_index(day, month, year)]


# Calculate which day of the week is the date
def get_day_for_date_index(day: int, month: int, year: int) -> int:
    COMMON_DOOMDAYS: list[int] = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    day_for_date: int = get_pivot_day(
        year) + (day - COMMON_DOOMDAYS[month - 1])

    # During january and february of leap years the common doomsday are one day after so since we remove the dooms day we need to remove on to the index
    if is_leap_year(year) and month <= 2:
        day_for_date -= 1

    # Clamp the returned value to week indexes
    return day_for_date % 7


# Calculate the pivot day
def get_pivot_day(year: int) -> int:

    year_last_digits = year % 100

    ancor_day = get_ancor_day(year_last_digits)

    next_multiple = get_next_multiple_of(ancor_day, 7)

    return (next_multiple - ancor_day + get_century_offset(year)) % 7


# Get the ancor day using the "odd + 11" method by by Chamberlain Fong and Michael K. Walters
def get_ancor_day(year_last_digits: int) -> int:
    if year_last_digits % 2 == 1:
        year_last_digits += 11

    year_last_digits //= 2

    if year_last_digits % 2 == 1:
        year_last_digits += 11

    return year_last_digits


# Computes the next configurable multiple greater than a configurable number
def get_next_multiple_of(number: int, multiple: int) -> int:
    next_multiple: int = multiple
    while next_multiple < number:
        next_multiple += multiple
    return next_multiple


# Get the offset off the pivot day based on a 400 year cycle
def get_century_offset(year: int) -> int:
    offsets: list[int] = [2, 0, 5, 3]
    year = year % 400

    for i in range(4):
        if year < (i + 1) * 100:
            return offsets[i]

    # Should never happend
    return -1
