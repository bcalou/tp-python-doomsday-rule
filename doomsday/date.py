# -*- coding: utf-8 -*-
"""
Modified on Thu Oct 14 2021

@author: Calixte Suaudeau
"""


def is_leap_year(date_string: str) -> bool:
    date_list: list = date_string.split('-')
    year: int = date_list[0]
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def does_date_exist(date_string: str) -> bool:
    date_list: list = date_string.split('-')
    if date_list[0] < 1583 or date_list[1] > 12:
        return False
    elif date_list[2] > 31:
        if date_list[1] % 2 == 1 and date_list[1] <= 7:
            return False
        elif date_list[1] % 2 == 0 and date_list[1] > 7:
            return False
    elif date_list[2] > 30:
        if date_list[1] % 2 == 0 and date_list[1] <= 7:
            return False
        elif date_list[1] % 2 == 1 and date_list[1] > 7:
            return False
    elif date_list[1] == 2:
        if date_list[2] > 28 and not is_leap_year(date_string):
            return False
        elif date_list[2] > 29 and is_leap_year(date_string):
            return False
    return True


def is_valid_date(date_string: str) -> bool:
    if isinstance(date_string, (int, list, dict)):
        print("Your format is not valid should be YYYY-MM-DD")
        return False

    date_splited: list = date_string.split("-")
    if len(date_splited) != 3:
        print("Your format is not valid should be YYYY-MM-DD")
        return False

    if not date_splited[0].isnumeric or not date_splited[1].isnumeric or not date_splited[2].isnumeric:
        print("Your date is not a composed only of number")
        return False

    if not does_date_exist(date_string):
        print("This date does not exist")
        return False

    return True
