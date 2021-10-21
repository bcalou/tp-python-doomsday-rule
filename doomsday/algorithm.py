from doomsday.date import is_leap_year
from doomsday.date import split_date

def get_day_for_date(date: str) -> str:
    date_split: list[int] | None = split_date(date)
    if date_split:
        
        years_anchor: int = get_anchor_day(date_split[0])
        doomsday: int = get_landmark_day(date_split[1], date_split[0])

        resultat: int = (years_anchor - doomsday + date_split[2]) % 7
        print(resultat)
        return get_day_str(resultat)
    return "Try Again"

def get_century_anchor(year: int) -> int:
    if year % 400 >= 0 and year % 400 < 100:
        return 2
    elif year % 400 >= 100 and year % 400 < 200:
        return 0
    elif year % 400 >= 200 and year % 400 < 300:
        return 5
    elif year % 400 >= 300 and year % 400 < 400:
        return 3
    return 0
    
def get_landmark_day(month: int, year: int) -> int:
    if month == 1:
        if is_leap_year(year):
            return 11
        else: return 10 
    elif month == 2:
        if is_leap_year(year):
            return 22
        else: return 21
    elif month % 2 == 0:
        return month
    elif month == 3:
        return 0
    elif month == 5:
        return 9
    elif month == 7:
        return 11
    elif month == 9:
        return 5
    elif month == 11:
        return 7
    return 0

def get_anchor_day(year: int) -> int:
    century: int = int(year / 100)
    year_in_century: int = year - (century * 100)
    century_anchor: int = get_century_anchor(year)

    return (century_anchor + int(year_in_century / 12) + year_in_century % 12 +
            int((year_in_century % 12) / 4)) % 7

def get_day_str(day: int) -> str:
    return ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"][day]

    
