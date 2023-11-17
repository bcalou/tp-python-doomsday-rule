from doomsday.date import is_leap_year

DAYS = (
     "Sunday",
     "Monday",
     "Tuesday",
     "Wednesday",
     "Thursday",
     "Friday",
     "Saturday"
)

CENTURY_ANCHOR = (
    3, 2, 0, 5
)


def get_weekday_for_date(date: str) -> str:
    """Return the name of the day corresponding to the given date"""

    year, month, day = (value for value in date.split("-"))
    anchor_day: int = get_anchor_day(year)

    return get_weekday_by_anchor_day(
        int(year), int(month), int(day), anchor_day)


def get_anchor_day(year: str) -> int:
    """Return the anchor day for the given year"""

    # Get the last two numbers in the year
    anchor_day: int = int(year[-2:len(year)])
    century: int = int(year[0:-2]) + 1

    if anchor_day % 2 != 0:
        anchor_day += 11

    anchor_day //= 2

    if anchor_day % 2 != 0:
        anchor_day += 11

    # Find the lowest multiple of seven greater than the value we have,
    # and keep the difference between this multiple and our value
    anchor_day %= 7
    anchor_day -= 7
    anchor_day = -anchor_day

    anchor_day += CENTURY_ANCHOR[(century % 4)]

    return anchor_day % 7


def get_weekday_by_anchor_day(
          year: int, month: int, day: int, anchor_day: int) -> str:
    """Return the weekday of the given MM-dd
    with the anchor day for the year"""

    is_leap_year_value : bool = is_leap_year(year)

    doomsdays = [
        3 if not is_leap_year_value else 4,
        28 if not is_leap_year_value else 29,
        14, 4, 9, 6, 11, 8, 5, 10, 7, 12
    ]

    doomsday: int = doomsdays[month - 1]

    if doomsday == day:
        return DAYS[anchor_day]

    if day > doomsday:
        return DAYS[(anchor_day + (day - doomsday)) % 7]

    return DAYS[(anchor_day - (doomsday - day)) % 7]
