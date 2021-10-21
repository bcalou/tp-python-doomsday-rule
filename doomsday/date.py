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
    elif ((get_month(date_string) % 2 == 1 and get_month(date_string) <= 7) or (get_month(date_string) % 2 == 0 and get_month(date_string) > 7)) and get_day(date_string) > 31:
        return False
    elif ((get_month(date_string) % 2 == 0 and get_month(date_string) <= 7) or (get_month(date_string) % 2 == 1 and get_month(date_string) > 7)) and get_day(date_string) > 30:
        return False
    elif get_month(date_string) == 2:
        if get_day(date_string) > 28 and not is_leap_year(date_string):
            return False
        elif get_day(date_string) > 29 and is_leap_year(date_string):
            return False
    return True


def is_valid_date(date_string: str) -> bool:
    if isinstance(date_string, (int, list, dict)):
        print("Your format is not valid should be YYYY-MM-DD")
        return False

    date_splited: list = date_string.split("-")
    if len(date_splited) < 3 and len(date_splited) > 3:
        print("Your format is not valid should be YYYY-MM-DD")
        return False

    if not date_splited[0].isnumeric or not date_splited[1].isnumeric or not date_splited[2].isnumeric:
        print("Your date is not a composed only of number")
        return False

    if not does_date_exist(date_string):
        print("This date does not exist")
        return False

    return True
