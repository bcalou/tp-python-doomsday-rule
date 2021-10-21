from doomsday.date import is_leap

Week_days = ["Sunday", "Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday"]


def get_date_anchor_date(year) -> int:
    thursday = 4
    c = int(str(year)[0:2]) + 1
    return int((((5 * c) + ((c - 1) / 4)) % 7) + thursday) % 7


def dooms_year(year) -> int:
    x = int(str(year)[2:])
    if x % 2 == 1:
        x = x + 11
    x = x / 2
    if x % 2 == 1:
        x = x + 11
    x = x % 7
    return int((7 - x) % 7)


def dooms_month(year: int, month: int, day: int) -> int:
    if month == 1:
        return (day - 10, day - 11)[is_leap(year)]
    elif month == 2:
        return (day - 21, day - 22)[is_leap(year)]
    elif month == 3:
        return day - 7
    elif month % 2 == 0:
        return day - month
    # For the remaining months, I use the "9 to 5 at the 7-11 due to Conway"
    elif month == 5:
        return day - 9
    elif month == 9:
        return day - 5
    elif month == 7:
        return day - 11
    # month == 11
    else:
        return day - 7


def get_day_for_date(date: str) -> str:
    year, month, day = date.split("-")
    dom = (get_date_anchor_date(int(year)) 
        + dooms_year(int(year)) 
        + dooms_month(int(year), int(month), int(day))) % 7

    return Week_days[dom]
    

	
	




