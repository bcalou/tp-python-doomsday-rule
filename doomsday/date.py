from doomsday.coherence import are_valids_month_and_day
from doomsday.leap import is_leap_year
from doomsday.transformate import transform_string_in_date
from doomsday.values import DAY, MONTH, YEAR

def is_valid_date(date: str) -> bool:
    """Return True if date is valid and could be calculated"""
    date_to_check:list[int] = transform_string_in_date(date)
    #If array is empty, return false
    if date_to_check == []:
        return False

    if not (date_to_check[YEAR] > 1583):
        print("Error - Year must be after 1583")
        return False
    elif not (date_to_check[MONTH] > 0 and date_to_check[MONTH] <= 12):
        print("Error - Bad month entered")
        return False
    elif (date_to_check[MONTH] == 2) and not is_leap_year(date_to_check[YEAR]) and (date_to_check[DAY] > 28):
        print("Error - Year is not leap")
        return False
    elif (date_to_check[MONTH] == 2) and is_leap_year(date_to_check[YEAR]) and (date_to_check[DAY] > 29):
        print("Error - Year is leap")
        return False
    elif not are_valids_month_and_day(date_to_check[DAY], date_to_check[MONTH]):
        print("Error - Bad day entered")
        return False

    return True