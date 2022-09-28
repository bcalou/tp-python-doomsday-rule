

def is_valid_date(date: str) -> bool:
    # Check input length
    if not (len(date) <= 10 or len(date) >= 8):
        return False

    # Split date and check if the list contain 3 elements : YYYY/MM/DD
    splited_date: list[str] = date.split("-")
    if len(splited_date) != 3:
        return False
    # Check if the year input is a number that fits in the gregorian calendar
    if not splited_date[0].isdigit() or int(splited_date[0]) < 1583:
        return False

    # Check if the month input is a number that is between 1 and 12
    if not (splited_date[1].isdigit() and (int(splited_date[1]) <= 12 and int(splited_date[1]) >= 1)):
        return False

    return is_day_valid(splited_date[2], int(splited_date[1]), int(splited_date[0]))


def is_day_valid(day_text: str, month: int, year: int) -> bool:

    USUSAL_DAYS_PER_MONTH: list[int] = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if day is in a valid format
    if not day_text.isdigit():
        return False

    # Check for february and leap year case
    day = int(day_text)

    if is_leap_year(year) and month == 2 and (day <= 29 or day >= 1):
        return True

    # Check for casual cases
    return day <= USUSAL_DAYS_PER_MONTH[month - 1] and day > 1


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0
