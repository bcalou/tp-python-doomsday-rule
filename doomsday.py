# -*- coding: utf-8 -*-
"""
Modified on Thu Oct 14 09:19:43 2021

@author: Calixte Suaudeau
"""

import datetime


def get_year(date_string: str) -> int:
    date_list: list = date_string.split('-')
    return int(date_list[0])


def get_month(date_string: str) -> int:
    date_list: list = date_string.split('-')
    return int(date_list[1])


def get_day(date_string: str) -> int:
    date_list: list = date_string.split('-')
    return int(date_list[2])


while True:
    date_string: str = input("Write a date (format: YYYY-MM-dd) \n")

    format = "%Y-%m-d"

    try:
        datetime.datetime.strptime(date_string, format)
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD, not: " + date_string)


while True:

    get_year(date_string)
print("test")
