GREGORIAN_CALENDAR_START: int = 1583
FEBRUARY_NUMBER: int = 2
MIN_LENGTH_DATE_STRING: int = 8
DATE_ELEMENT_NUMBER: int = 3


def is_valid_date(date: str) -> bool:
    """Look if the date does not violate the terms for conway algorithm"""

    date_as_list: list[str] = check_date_string_and_split_it(date)

    if not date_as_list:
        return False

    year, month, day = date_as_list
   

    if not is_valid_year(year):
        return False
    if not is_valid_month_and_day(month, day, find_if_is_bissextile(int(year))):
        return False
    return True


def check_date_string_and_split_it(date: str) -> list[str]:
    """Check date string and make it a list"""

    if len(date) < MIN_LENGTH_DATE_STRING:
        print("Date is not long enough to be valid")
        return []

    date_as_list: list[str] = date.split("-")

    if len(date_as_list) != DATE_ELEMENT_NUMBER:
        print("Too much or too less date elements")
        return []

    return date_as_list


def is_valid_year(year: str) -> bool:
    """Check if year is a number above start of gregorian calendar"""

    if not year.isdecimal():
        print("Year must be a number")
        return False

    if int(year) < GREGORIAN_CALENDAR_START:
        print("Year must be after 1582")
        return False

    return True


def find_if_is_bissextile(year: int) -> bool:
    """Check if a year is multiple of four, and not multiple of 100 but multiple of 400"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_month_and_day(month: str, day: str, is_year_bissextile: bool) -> bool:
    """Check if month and day are coherent"""

    if not (is_a_number(month, "Month") and is_a_number(day, "Day")):
        return False

    int_day: int = int(day)
    int_month: int = int(month)

    if not is_month_valid_and_day_above_1(int_month, int_day):
        return False

    if is_day_valid_in_february(int_month, int_day, is_year_bissextile):
        return True
    elif is_day_valid_in_even_month(int_month, int_day):
        return True
    elif is_day_valid_in_odd_month(int_month, int_day):
        return True

    return False


def is_day_valid_in_february(month: int, day: int, is_year_bissextile: bool) -> bool:
    """Test if the day is not too big for february"""
    return (month == FEBRUARY_NUMBER and
            ((is_year_bissextile and day <= 29) or
             (not is_year_bissextile and day <= 28)))


def is_month_valid_and_day_above_1(month: int, day: int) -> bool:
    """Test if month valid and day above 1"""
    if 1 > month or month > 12:
        print("Month must be between 1 and 12")
        return False

    if 1 > day:
        print("Day must be positive and above 1")
        return False

    return True


def is_day_valid_in_even_month(month: int, day: int) -> bool:
    """Test if the day is not too big for even month except february"""
    return (month % 2 == 0 and month != 2 and
            ((month > 7 and day <= 31)
             or (month < 7 and day <= 30)))


def is_day_valid_in_odd_month(month: int, day: int) -> bool:
    """Test if the day is not too big for odd month """
    return (month % 2 == 1 and
            ((month < 8 and day <= 31) or
             (month > 8 and day <= 30)))


def is_a_number(number_to_test: str, variable_wanted: str) -> bool:
    """Test if a string is a number"""

    if not number_to_test.isdecimal():
        print(f"{variable_wanted} must be a number")
        return False
    return True
