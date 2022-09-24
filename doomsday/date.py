def is_valid_date(date: str) -> bool:
    """Checking if entered string format is correct and if the date exists"""

    dash_quantity: int = 0

    for character in date:
        if character == "-":
            dash_quantity += 1
    
    if dash_quantity != 2:
        print("Please format date with dashes")
        return False
    
    date_list: list[str] = date.split('-')
    year: str = date_list[0]
    month: str = date_list[1]
    day: str = date_list[2]

    if not year.isdecimal():
        print("Please enter a correct year")
        return False
    
    if not month.isdecimal():
        print("Please enter a correct month")
        return False
    
    if not int(year) >= 1583:
        print("Please enter a year after 1583")
        return False
    
    if not 0 < int(month) <= 12:
        print("This month doesn't exist")
        return False
    
    months_with_30_days: list[int] = [4, 6, 9, 11]
    months_with_31_days: list[int] = [1, 3, 5, 7, 8, 10, 12]

    if not day.isdecimal():
        print("Please input a correct day")
        return False
    
    if (
        (int(month) in months_with_30_days) and (not 0 < int(day) <= 30) or
        (int(month) in months_with_31_days) and (not 0 < int(day) <= 31)
    ):
        print("This day doesn't exist in this month")
        return False
    
    if (
        int(month) == 2 and
        ((is_leap_year(int(year)) and not 0 < int(day) <= 29) or
        (not is_leap_year(int(year)) and not 0 < int(day) <= 28))
    ):
        print("This day doesn't exist in this month (please check if year is leap)")
        return False

    return True


def is_leap_year(year: int) -> bool:
    """Check is year is leap or not"""
    return (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0)

"""
date_to_test: str = "2021-10-10"
print(f"Is {date_to_test} a valid date ?", is_valid_date(date_to_test))
"""




"""
################################################################################
---------
QUESTIONS
---------

Est-ce que fonction trop longue ? Pertinent de sous-découper en mini fonctions ?
(is_string_format_correct(), does_year_exist(), does_month_exist(), does_day_exist())

Convention respectée pour les if avec des retours à la ligne ?
"""