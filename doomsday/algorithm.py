from doomsday.date import is_leap_year
import doomsday.utils as utils


WEEKDAYS: list[str] = (
    ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
)


def get_day_for_date(date: str) -> str:
    """
    Calculates and returns the weekday for a given date. See 
    https://en.wikipedia.org/wiki/Doomsday_rule to get the different steps of
    the process.
    """

    utils.init_global_variables()
    utils.parse_string_date_to_variables(date)
    anchor_day_index: int =(get_anchor_day_index(utils.year))

    # Doomsdays list for each month. list[0] is unused, list[1,2] for January
    # and February are set afterwards according whether the year is leap or not. 
    months_doomsdays: list[int] = [999, 0, 0, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    if is_leap_year(utils.year):
        months_doomsdays[1] = 11 # January the 11th if year is leap
        months_doomsdays[2] = 22 # February the 22nd if year is leap
    else:
        months_doomsdays[1] = 10 # January the 10th if not
        months_doomsdays[2] = 21 # February the 21st if not
    
    gap_between_day_to_test_and_month_doomsday: int = (
        (utils.day - months_doomsdays[utils.month]) % 7
    )

    return WEEKDAYS[(anchor_day_index + gap_between_day_to_test_and_month_doomsday) % 7]


def get_anchor_day_index(given_year: int) -> int:
    """
    This function calculates the anchor day for the given year and returns
    its index.
    See https://en.wikipedia.org/wiki/Doomsday_rule#The_%22odd_+_11%22_method
    for the calculation process.
    """

    CENTURY_ANCHORS: list[int] = [2, 0, 5, 3]
    century_digits: int = int(str(given_year)[:2])
    year_of_century: int = int(str(given_year)[2:])
    intermediate_result: float = float(year_of_century)

    if not year_of_century % 2 == 0:
        intermediate_result = intermediate_result + 11
    
    intermediate_result = intermediate_result / 2

    if not intermediate_result % 2 == 0:
        intermediate_result = intermediate_result + 11
    
    difference_between_intermediate_result_and_higher_multiple_of_7: int = (
        7 - int(intermediate_result) % 7
    )
    century_anchor: int = CENTURY_ANCHORS[(century_digits) % 4]
    anchor_day_index: int = (
        (difference_between_intermediate_result_and_higher_multiple_of_7
        + century_anchor) % 7
    )
    return anchor_day_index
