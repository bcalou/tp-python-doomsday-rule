from tools import is_leap_year

def get_day_for_date(date_input: str) -> str:
    date : list[str] = date_input.split('-')
    year : str = date[0]
    month : int = int(date[1])
    day : int = int(date[2])

    index_day_of_the_week : list[str] = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]
    
    century_tag = get_century_tag(year)
    anchor_day = get_anchor_day(year, century_tag)
    doomsday = get_doomsday(int(year), month)
    

    day_for_date : str = index_day_of_the_week[(day - doomsday + anchor_day)%7]
    return day_for_date

def get_century_tag(year : str) -> int:
    century : int = int(int(year)/100)
    return [2,0,5,3][century%4]

def get_anchor_day(year : str, century_tag : int) -> int:
    last_numbers_of_year : int = int(year[-2:])
    if last_numbers_of_year%2 != 0 :
        last_numbers_of_year += 11
    last_numbers_of_year = int(last_numbers_of_year/ 2)
    if last_numbers_of_year%2 !=0 :
        last_numbers_of_year += 11
    multiple_sup : int = 0
    while multiple_sup < last_numbers_of_year :
        multiple_sup += 7
    difference : int = multiple_sup - last_numbers_of_year
    return (difference + century_tag)%7

def get_doomsday(year : int, month : int) -> int :
    if month <= 2 and is_leap_year(year):
        return [4, 1][month - 1]
    return [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5][month - 1]

print(get_day_for_date("2259-01-10"))
