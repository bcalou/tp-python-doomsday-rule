from doomsday.coherence import are_valids_month_and_day
from doomsday.leap import is_leap_year
from doomsday.transformate import transform_string_in_date

DAY: int = 0
MONTH: int = 1
YEAR: int = 2

def is_valid_date(date: str) -> bool:
    date_to_check:list[int] = transform_string_in_date(date)

    if date_to_check == []:
        return False

    if not (date_to_check[YEAR] > 1583):
        print("Error - Year must be after 1583")
        return False
    elif not (date_to_check[DAY] > 0 and date_to_check[DAY] <= 31):
        print("Error - Bad day entered")
        return False
    elif not (date_to_check[MONTH] > 0 and date_to_check[MONTH] <= 12):
        print("Error - Bad month entered")
        return False
    elif (date_to_check[YEAR] > 2148):
        print("Error - Year must exist")
        return False
    elif (date_to_check[MONTH] == 2) and not is_leap_year(date_to_check[YEAR]) and (date_to_check[DAY] > 28):
        print("Error - Year is not leap")
        return False
    elif (date_to_check[MONTH] == 2) and is_leap_year(date_to_check[YEAR]) and (date_to_check[DAY] > 29):
        print("Error - Year is leap")
        return False
    elif not are_valids_month_and_day(date_to_check[DAY], date_to_check[MONTH]):
        return False

    return True