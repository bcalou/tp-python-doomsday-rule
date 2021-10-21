import math


EASY_CENTURY_TAG : list[int] = [2, 0, 5, 3]
DAYS : list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DAYS_ANCHOR : list[int] = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    

def get_day_for_date(date_input: str) :
    date : list[str] = date_input.split("-")
    day_anchor : int = get_day_anchor(date)
    day_of_the_year: int = get_day_of_the_year(int(date[0]))
    result = (int(date[2]) - day_anchor + day_of_the_year)%7
    return DAYS[result]

def is_leap_year(year : int) :
    return year%4 == 0 and year%400 == 0


def get_century_tag(year : int ) -> int :
    century : float = math.floor(year/100)
    return EASY_CENTURY_TAG[century%4]

def get_day_anchor(date : list[str]) -> int :
    month : int = int(date[1])
    year : int = int(date[0])
    if is_leap_year(year):
        if month == 1 : return 11
        elif month == 2 : return 22
        else : return DAYS_ANCHOR[month -1]
    else:
        return DAYS_ANCHOR[month -1]

def get_day_of_the_year(year : int) :
    century_tag = get_century_tag(year)
    day_of_year = year%100
    if (day_of_year%2!=0):
        day_of_year+=11
    day_of_year //= 2
    if (day_of_year%2 !=0):
        day_of_year+=11
    compt = 7 - day_of_year%7
    day_of_year  = (compt + century_tag)%7
    return day_of_year