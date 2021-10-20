from doomsday.tools import is_leap_year


index_day_of_the_week: list[str] = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]


"""Return the day for the given date."""
def get_day_for_date(date_input: str) -> str:
    date: list[str] = date_input.split('-')
    year: int = int(date[0])
    month: int = int(date[1])
    day: int = int(date[2])

    century_tag = get_century_tag(year)
    anchor_day = get_anchor_day(year, century_tag)
    doomsday = get_doomsday(year, month)

    day_for_date: str = index_day_of_the_week[(day - doomsday + anchor_day) % 7]
    return day_for_date


"""Return the century tag to add in the formula to get the anchor day"""
def get_century_tag(year: int) -> int:
    century: int = int(int(year)/100)
    return [2, 0, 5, 3][century % 4]


"""Return the anchor date of the given year."""
def get_anchor_day(year: int, century_tag: int) -> int:
    last_numbers_of_year: int = year % 100
    if last_numbers_of_year % 2 != 0:
        last_numbers_of_year += 11
    last_numbers_of_year = int(last_numbers_of_year / 2)
    if last_numbers_of_year % 2 != 0:
        last_numbers_of_year += 11
    difference: int = 7-(last_numbers_of_year%7)
    return (difference + century_tag) % 7


"""Return the doomsday for the given year and month."""
def get_doomsday(year: int, month: int) -> int:
    if month <= 2 and is_leap_year(year):
        return [4, 1][month - 1]
    return [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5][month - 1]
