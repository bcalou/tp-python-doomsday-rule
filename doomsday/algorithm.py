from doomsday.date import is_leap_year


# Finds the anchor day of a given month
def get_month_anchor_day(month: int, is_leap_year: bool):
    ANCHOR_DAYS_LIST: list[int] = [0, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    if month == 1:
        if is_leap_year:
            return 11
        else:
            return 10
    elif month == 2:
        if is_leap_year:
            return 22
        else:
            return 21
    else:
        return ANCHOR_DAYS_LIST[month-1]


# Finds the century tag
def get_century_tag(year: int) -> int:
    tag_index = year % 400

    if tag_index < 100:
        return 2
    if tag_index < 200:
        return 0
    if tag_index < 300:
        return 5
    return 3


# Many calculations to get a year's anchor
def get_year_anchor(year):
    year_anchor: float = year % 100

    # The odd + 11 method
    if year_anchor % 2 == 1:
        year_anchor = year_anchor + 11

    year_anchor = year_anchor / 2

    if year_anchor % 2 == 1:
        year_anchor = year_anchor + 11

    # Computing the anchor
    year_anchor = 7 * ((year_anchor // 7) + 1) - year_anchor
    return year_anchor


# Finds the day with its month anchor, year anchor and tag
def get_day(target_day, month_anchor_day, year_anchor, tag):
    anchor_day: int = (year_anchor + tag) % 7
    day: int = (target_day - (month_anchor_day - anchor_day)) % 7

    DAYS_LIST: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
    return DAYS_LIST[int(day)]


# Determines what day the given date is referring to
def get_day_for_date(date: str) -> str:
    # We already know that the date is valid so no need to double check,
    # see doomsday.py
    split_date: list[str] = date.split('-')
    received_year: int = int(split_date[0])
    received_month: int = int(split_date[1])
    received_day: int = int(split_date[2])

    month_anchor_day: int = get_month_anchor_day(received_month, is_leap_year(received_year))
    century_tag = get_century_tag(received_year)
    year_anchor: float = get_year_anchor(received_year)
    day_result: str = get_day(received_day, month_anchor_day, year_anchor, century_tag)

    return day_result
