from doomsday.date import is_leap_year

def get_day_for_date(date: str) -> str:
    split_date: list[str] = date.split('-')
    year:str = split_date[0]
    mounth:int = int(split_date[1])
    day:int = int(split_date[2])
    pivot:int = find_pivot(int(year),mounth)
    pivot_day:float = day_for_year(int(year[2:]),int(year[:2]))
    result:float = day - pivot
    result = (pivot_day + (result % 7)) % 7
    if result == 0 :
        return "Sunday"
    if result == 1 :
        return "Monday"
    if result == 2 :
        return "Tuesday"
    if result == 3 :
        return "Wednesday"
    if result == 4 :
        return "Thursday"
    if result == 5 :
        return "Friday"
    else:
        return "Saturday"
    



def find_pivot(year:int, mounth:int) -> int:
    if mounth == 1 and is_leap_year(str(year)):
        return 11
    elif mounth == 1 and not is_leap_year(str(year)):
        return 10
    elif mounth == 2 and is_leap_year(str(year)):
        return 22
    elif mounth == 2 and not is_leap_year(str(year)):
        return 21
    else:
        if mounth%2 == 0:
            return mounth
        elif mounth == 3:
            return 0
        elif mounth == 5:
            return 9
        elif mounth == 9:
            return 5
        elif mounth == 7:
            return 11
        else:
            return 7
    
def century_tag(split_centuary:int) -> int:
    if split_centuary % 4 == 0:
        return 2
    if split_centuary % 4 == 1:
        return 0
    if split_centuary % 4 == 2:
        return 5
    else:
        return 3

def day_for_year(split_year:float,split_centuary:int) -> float :
    if not split_year % 2 == 0:
        split_year += 11
    split_year = split_year/2
    if not split_year % 2 == 0:
        split_year += 11
    split_year = ((split_year % 7) - 7) * -1 
    if split_year == 7:
        split_year = 0
    return ((split_year + century_tag(split_centuary))%7)
