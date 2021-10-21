def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


def months_finder(month: int, year: int):
    tab_months = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    number = tab_months[month-1]
    return number+1 if((month == 1 or month == 2) and leap_year(year)) else number


def calculation_anchor_day(year: int) -> int:
    list_year = str(year)
    day = list_year[2]+list_year[3]
    day = int(day)
    if(not day % 2 == 0):
        day += 11
    day = day/2
    if(not day % 2 == 0):
        day += 11
    return int(-day % 7)


def year_century(year_century: int) -> int:
    modulo = int(year_century / 100 % 4)
    if(modulo == 0):
        return 2
    elif(modulo == 1):
        return 0
    elif(modulo == 2):
        return 5
    return 3


def get_day_for_date(date: str) -> str:
    list_date = date.split('-')
    year = int(list_date[0])
    month = int(list_date[1])
    day = int(list_date[2])
    days = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    day_key = int((calculation_anchor_day(year)+year_century(year)))
    day_pivot = (months_finder(month, year))
    diff_day = (day_pivot - day)
    return days[(day_key-diff_day) % 7]
