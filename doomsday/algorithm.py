from doomsday.date import get_split_date
from doomsday.date import is_leap_year
from doomsday.constants import DAYS
from doomsday.constants import BALISES
from doomsday.constants import BENCHMARK_DAY


def get_day_for_date(date: str) -> str:
    """
    Return string.
    Get the day for the date.
    Keyword arguments:
    date -- Date input by the user
    """

    year, month, day = get_split_date(date)
    anchor_day: int = get_anchor_day_range(year)
    has_leap_year: bool = is_leap_year(year)
    benchmark_day: int = get_benchmark_day(month, has_leap_year)
    day_range: int = (anchor_day + ((day - benchmark_day))) % 7

    return DAYS[day_range]


def get_anchor_day_range(target) -> int:
    """
    Return integer.
    Get the range of the anchor day in the constant list.
    Keyword arguments:
    target -- Year of the date input by the user
    """

    anchor_day_range: int = 0
    end_of_year: int = int(str(target)[-2] + str(target)[-1])

    if end_of_year % 2 == 1:
        anchor_day_range = end_of_year + 11
    anchor_day_range = anchor_day_range // 2
    if anchor_day_range % 2 == 1:
        anchor_day_range = anchor_day_range + 11

    higher_multiple = get_higher_multiple_of_seven(anchor_day_range)
    anchor_day_range = higher_multiple - anchor_day_range

    add_for_century = get_balise(target)

    anchor_day_range = (anchor_day_range + add_for_century) % 7

    return anchor_day_range


def get_higher_multiple_of_seven(target) -> int:
    """
    Return integer.
    Get multiple of seven higher than target
    Keyword arguments:
    target -- anchor day range
    """

    higher_multiple_of_seven = 7
    while True:
        higher_multiple_of_seven += 7
        if(higher_multiple_of_seven > target):
            return higher_multiple_of_seven


def get_balise(target) -> int:
    """
    Return int.
    Get the number in the contant list of balise.
    Keyword arguments:
    target -- year of the date input bu the user
    """
    century: int = int(str(target)[0] + str(target)[1]) % 4
    return BALISES[century % 4]


def get_benchmark_day(month, has_leap_year) -> int:
    """
    Return integer.
    Get the benchmark day of the month
    Keyword arguments:
    month -- Month of the date input bu the user
    has_leap_year -- Boolean is a leap year
    """
    if month <= 2 and has_leap_year:
        return BENCHMARK_DAY[str(month) + "bis"]

    return BENCHMARK_DAY[str(month)]
