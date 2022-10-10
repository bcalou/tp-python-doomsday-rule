"""Multiple functions that implements the doomsday algorithm
"""

WEEK: tuple = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def get_day_for_date(date: str) -> str:
    """Return the day of the week for the given date (format = YYYY-MM-DD)"""

    input_year, input_month, input_day = date.split("-")

    converted_century: int = int(input_year) // 100
    converted_year: int = int(input_year) % 100
    converted_month: int = int(input_month)
    converted_day: int = int(input_day)
    is_leap: bool = is_leap_year(converted_century*100 + converted_year)

    anchor_weekday: int = get_anchor_weekday(get_year_bonus(converted_century), converted_year)
    month_anchor: int = get_month_anchor(converted_month, is_leap)

    computed_day: int = (anchor_weekday + (converted_day - month_anchor)) % 7
    return WEEK[computed_day]

def get_anchor_weekday(year_bonus: int, year: int) -> int:
    """Calculates the anchor day for the given year"""
    if year % 2 == 1:
        year += 11
    year = year // 2
    if year % 2 == 1:
        year += 11

    anchor_weekday: int = (7 - (year % 7)) + year_bonus
    return anchor_weekday % 7

def get_month_anchor(month: int, is_leap: bool) -> int:
    """Return the month anchor for the given month"""
    if month <= 3:
        return special_month_cases(month, is_leap)
    if month == 5 or month == 9:
        return 14 - month # We invert may and september
    if month == 7 or month == 11:
        return 18 - month # We invert july and november
    return month # The other months correspond to their anchor day

def special_month_cases(month: int, is_leap: bool) -> int:
    """Completes get_month_anchor for special cases (the first 3 months)"""
    # Month anchor for January and February change if it's a leap year
    if month == 1:
        return 11 if is_leap else 10
    if month == 2:
        return 22 if is_leap else 21
    return 0 # March's anchor day is 0

def is_leap_year(year: int) -> bool:
    """Return whether this year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_year_bonus(century: int) -> int:
    """Return the number to add for the given century"""
    if century % 4 == 0:
        return 2
    if century % 4 == 1:
        return 0
    if century % 4 == 2:
        return 5
    return 3

if __name__ == "__main__":
    print("This file isn't executable. Prefer starting 'doomsday.py'.")
