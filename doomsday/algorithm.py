import doomsday.date as date

WEEK_DAY_STR = ("Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday")

TAB_CHANGE_FOR_CENTURY = (2, 0, 5, 3)
TAB_ANCHOR_DAY_IN_MONTH = (10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12)

NUMBER_ADD_IF_ODD = 11
WEEK_SIZE = 7
CENTURY = 100

YEAR = 0
MONTH = 1
DAY = 2


def get_weekday_for_date(date: str) -> str:
    """get_weekday_for_date need the anchor date
    and then find the day of the date"""

    # We split again the date
    list_date: list[str] = date.split('-')

    # We find the anchor day
    anchor_day_week: int = get_anchor_day(int(list_date[YEAR]))

    # With the month we find the anchor day in the month
    anchor_day_in_date_month = find_anchor_day_in_date_month(
        int(list_date[MONTH]), int(list_date[YEAR]))

    # We return the str day in week
    return get_day_in_week(anchor_day_week,
                           anchor_day_in_date_month, list_date)


def get_anchor_day(year: int) -> int:
    """get_anchor_day find the anchor day with different operation"""

    # We keep only the two last number of the year
    number_for_day: int = year % CENTURY

    # We transform this number
    number_for_day = add_eleven_if_is_odd(number_for_day)
    number_for_day //= 2
    number_for_day = add_eleven_if_is_odd(number_for_day)
    number_for_day = get_difference_near_multiple_of_seven(number_for_day)
    number_for_day = add_century_step(
        number_for_day, year // CENTURY * CENTURY) % WEEK_SIZE

    # We find the day in a tab
    return number_for_day


def add_eleven_if_is_odd(number: int) -> int:
    """We add eleven if number is odd"""
    return number if number % 2 == 0 else number + NUMBER_ADD_IF_ODD


def get_difference_near_multiple_of_seven(number: int) -> int:
    """We take difference between number and multiple of seven above"""
    return get_multiple_of_seven_above(number)-number


def get_multiple_of_seven_above(number: int) -> int:
    """We find the multiple of seven above the number"""
    number = number // WEEK_SIZE * WEEK_SIZE
    if number % WEEK_SIZE != 0:
        number += WEEK_SIZE
    return number


def add_century_step(number: int, century: int) -> int:
    """we add a number different with the century"""
    return number+TAB_CHANGE_FOR_CENTURY[(century // CENTURY) %
                                         len(TAB_CHANGE_FOR_CENTURY)]


def find_anchor_day_in_date_month(month: int, year: int) -> int:
    """anchor day in month who is in a tab"""
    if (month < 3 and date.get_leap(year)):
        return TAB_ANCHOR_DAY_IN_MONTH[month-1] + 1
    return TAB_ANCHOR_DAY_IN_MONTH[month-1]


def get_difference_in_day(current_day: int, anchor_day: int) -> int:
    """get difference between anchor day and current day"""
    return current_day - anchor_day


def get_day_in_week(anchor_day: int, anchor_day_in_date_month: int,
                    list_date: list[str]) -> str:
    """get_day_in_week translate anchor to day we search with distance"""
    distance_in_day = get_difference_in_day(int(list_date[DAY]),
                                            anchor_day_in_date_month)
    return WEEK_DAY_STR[(anchor_day+distance_in_day) % WEEK_SIZE]
