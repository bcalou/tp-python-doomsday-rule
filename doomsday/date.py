# -*- coding: utf-8 -*-
"""
Modified on Thu Oct 14 2021

@author: Calixte Suaudeau
"""


def get_year(date_string: str) -> int:
    date_list: list = date_string.split('-')
    return int(date_list[0])


def get_month(date_string: str) -> int:
    date_list: list = date_string.split('-')
    return int(date_list[1])


def get_day(date_string: str) -> int:
    date_list: list = date_string.split('-')
    return int(date_list[2])


def is_leap_year(date_string: str) -> bool:
    year: int = get_year(date_string)
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def does_date_exist(date_string: str) -> bool:
    if get_year(date_string) < 1583 or get_month(date_string) > 12:
        return False
    elif get_month(date_string) % 2 == 1 and get_month(date_string) <= 7 or get_month(date_string) % 2 == 0 and get_month(date_string) > 7 and get_day(date_string) > 30:
        return False
    elif get_day(date_string) > 31:
        return False
    elif get_month(date_string) == 2:
        if get_day(date_string) > 28 and not is_leap_year(date_string) or get_day(date_string) > 29 and is_leap_year(date_string):
            return False
    return True


def is_valid_date(date_string: str) -> bool:
    try:
        int(get_day(date_string))
    except ValueError:
        print("Your day is not valid. Format should be YYYY-MM-DD")
        return False
    except IndexError:
        print("Your format is not valid should be YYYY-MM-DD")
        return False

    try:
        int(get_month(date_string))
    except ValueError:
        print("Your month is not valid. Format should be YYYY-MM-DD")
        return False

    try:
        int(get_year(date_string))
    except ValueError:
        print("Your year is not valid. Format should be YYYY-MM-DD")
        return False

    if not does_date_exist(date_string):
        print("This date does not exist or is before 1583")
        return False
    return True


while True:
    date_string: str = input("Write a date (format: YYYY-MM-dd) \n")
    if is_valid_date(date_string):
        break
    continue
