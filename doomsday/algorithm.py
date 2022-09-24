DAYS_TABLE: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

MONTH_KEY_DAYS_POSITION: list[int] = [0,0,0,4,9,6,11,8,5,10,7,12]
CENTURY_CORRECTOR_EQUIVALENCE: list[int] = [2,0,5,3]

from calendar import weekday
from operator import is_
from doomsday.date import is_year_bissextile


def get_day_for_date(date: str) -> str:
    return "Monday"

def get_weekday_for_date(date: str) -> str:
    """Return the week day of a date"""
    
    date_as_list: list[str] = date.split("-")
    key_day: int = get_key_day(year = date_as_list[0])
    month_key_day_position: int = get_position_key_day_in_month(month = date_as_list[1], year = date_as_list[0])

    position_difference_with_key_day: int = (int(date_as_list[2]) - month_key_day_position) % 7
    weekday: int = (key_day + position_difference_with_key_day) % 7

    return DAYS_TABLE[weekday]


def get_century_balise(century: str) -> int :
    """Find the century balise, based on century % 4"""

    int_century: int = int(century)
    type: int = int_century % 4
    return CENTURY_CORRECTOR_EQUIVALENCE[type]
    
def get_operations_on_end_year(years: str) -> int:
    """Do the preliminary operations on the 2 last digits of year"""
    int_years: int = int(years)

    int_years = add_11_if_number_is_odd(int_years)
    int_years //= 2
    int_years = add_11_if_number_is_odd(int_years)

    superior_multiple_of_7: int = get_superior_multiple_of_seven(int_years)
    
    return (superior_multiple_of_7 * 7) - int_years

def add_11_if_number_is_odd(number: int) -> int:

    if number % 2 != 0:
        number += 11
    return number

def get_superior_multiple_of_seven(number: int) -> int:

    superior_multiple_of_7: int =  (number // 7)
    if superior_multiple_of_7 != 0:
        superior_multiple_of_7 += 1

    return superior_multiple_of_7


def get_key_day(year: str) -> int:
    """Get the key day of a given year, odd 11 method"""

    year_length: int = len(year)
    transformed_year: int = get_operations_on_end_year(year[year_length - 2:])

    century_balise: int = get_century_balise(year[:year_length - 2])

    return (transformed_year + century_balise) % 7
    
def get_position_key_day_in_month( month: str, year: str) -> int :
    """Get position of key day in given month"""

    int_month:int = int(month)

    if int_month < 3 :
        if is_year_bissextile(int(year)) :
            return 11 if (int_month == 1) else 22
        else :
            return 10 if (int_month == 1) else 21
    else:
        return MONTH_KEY_DAYS_POSITION[int_month - 1]
           
        

