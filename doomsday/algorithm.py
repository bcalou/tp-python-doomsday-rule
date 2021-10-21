
from doomsday.date import is_leap

Week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
Month_doomsday = [3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]
Month_doomsday_LEAP = list(Month_doomsday)
Month_doomsday_LEAP[:2] = [4, 29]
CDOOMSDAY = [2, 0, 5, 3]



def get_date_anchor_date(year):
    thursday = 4
    c = int(str(year)[0:2]) + 1
    return int((((5 * c) + ((c - 1) / 4)) % 7) + thursday) % 7

def dooms_year(year):
    x = int(str(year)[2:])
    if x % 2 == 1:
        x = x + 11
    x = x / 2
    if x % 2 == 1:
        x = x + 11
    x = x % 7
    return int((7 - x) % 7)

def dooms_month(year: int, month:int, day: int) -> int:
    # In January and February, the doomsday used depends
    # on whether or not the year of the date is a is_leap.
    if month == 1:
        if is_leap(year):
            return day - 11
        else:
            return day - 10
    elif month == 2:
        if is_leap(year):
            return day - 22
        else:
            return day - 21
    # In March we use the 7th as our reference Doomsday.
    elif month == 3:
        return day - 7
    # Even months after March use the day of the month
    # equal to the month of the year
    elif month % 2 == 0:
        return day - month
    # For the remaining months, we use the "9 to 5 at the 7-11"
    # mnemonic due to Conway
    elif month == 5:
        return day - 9
    elif month == 9:
        return day - 5
    elif month == 7:
        return day - 11
    else: # month == 11
        return day - 7


# if __name__ == '__main__':
#     tests = [
#         (2305, 7, 13, 'Thursday'),
#         (1776, 7, 4, 'Thursday'),
#         (1969, 7, 20, 'Sunday'),
#         (1984, 1, 6, 'Friday'),
#         (1902, 10, 19, 'Sunday'),
#    ]
    # for test in tests:
    #     if getDoomsday(*test[:3]) != test[-1]:
    #         print('Broken for', test)


def get_day_for_date(date: str) -> str:
    year, month, day = date.split("-")
    dom = (get_date_anchor_date(int(year)) + dooms_year(int(year)) + dooms_month(int(year), int(month), int(day))) % 7
    name : bool = True
    if name:
        return Week_days[dom]
    else:
        return dom
    

	
	




