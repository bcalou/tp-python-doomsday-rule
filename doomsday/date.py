def is_valid_date(date: str) -> bool:
    '''Check the input date validity'''

    input_date: list[str] = date.split('-')
    if len(input_date) != 3:
        return False

    year: str
    month: str
    day: str

    # Get Each elements
    year, month, day = input_date

    if not check_date(day, month, year):
        return False

    return True


def is_numeric(day: str, month: str, year: str) -> bool:
    '''Check if the input date is composed with numeric characters'''
    return day.isnumeric() and month.isnumeric() and year.isnumeric()


def is_leap_year(year: int) -> bool:
    '''Returns True if the input year is a leap year, else it returns False'''
    return (not year % 100 == 0 and year % 4 == 0) or year % 400 == 0


def check_date(day: str, month: str, year: str) -> bool:
    '''
    Check each elements of the date (day, month, year)
    and check if characters are numeric
    '''
    if not is_numeric(day, month, year):
        print("The date should be composed of numeric characters separated by \
            dashes.")
        return False

    if not check_day(int(day)):
        return False

    if not check_month(int(year), int(month), int(day)):
        return False

    if not check_year(int(year)):
        return False

    return True


def check_day(day: int) -> bool:
    '''Check the validity of the input day'''
    if day <= 0:
        print("The input day don't be negative or null")
        return False
    return True


def check_year(year: int) -> bool:
    '''Check the validity of the input year'''
    if year <= 1583:
        print("This algorithm operates only in gregorian calender wich start\
             in 1583. Please enter a date greater than 1583")
        return False
    return True


def check_month(year: int, month: int, day: int) -> bool:
    '''Check the validity of the input month'''

    if 0 >= month or month > 12:
        print("The input month must be included between 0 and 12")
        return False

    # Months with 31 days
    big_months: list[int] = [1, 3, 5, 7, 8, 10, 12]
    for big_month in big_months:
        if month == big_month and day > 31:
            print("The input day is not possible with this input month")
            return False

    # Months with 30 days
    small_months: list[int] = [2, 4, 6, 9, 11]
    for small_month in small_months:
        if month == small_month and day > 30:
            print("The input day is not possible with this input month")
            return False

    # Check day in febuary during leap year
    if is_leap_year(year) and month == 2 and day > 29:
        print("The input day is not possible with this input month/years")
        return False

    # Check day in febuary during simple year
    if not is_leap_year(year) and month == 2 and day > 28:
        print("The input day is not possible with this input month/years")
        return False

    return True
