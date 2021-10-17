import math


def get_day_for_date(date: str) -> str:
    DAYS_OF_WEEK = [
                    "Sunday", "Monday", "Tuesday", 
                    "Wednesday", "Thursday", "Friday", "Saturday"
    ]
    DOOMSDAY_LEAP_YEAR = [4, 1, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
    DOOMSDAY_NORMAL_YEAR = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:])
    century = math.floor(year / 100)
    ancre_date_of_century = (5 * (century % 4) + 2) % 7
    century_rest = year % 100
    century_rest_m = century_rest % 12
    dooms_day = (
        ((math.floor(century_rest / 12)) + (math.floor(century_rest_m / 4) + 
         century_rest_m) + ancre_date_of_century) % 7)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400) == 0:
        ancre_date = DOOMSDAY_LEAP_YEAR[month - 1]
    else:
        ancre_date = DOOMSDAY_NORMAL_YEAR[month - 1]
    week_day = (dooms_day + day - ancre_date) % 7
    return DAYS_OF_WEEK[week_day]
