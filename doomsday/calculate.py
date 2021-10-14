from doomsday.day import Day
from doomsday.transformate import transform_string_in_date

DAY: int = 0
MONTH: int = 1
YEAR: int = 2

def is_paired(n: int)->bool:
    if (n % 2) == 0:
        return True
    return False

def multiple_of_7_lower_than(n: int)->int:
    return (n // 7) * 7

def in_function_of_century(century: int)->int:
    if century == 16 or century == 20:
        return 2
    if century == 17 or century == 21:
        return 0
    if century == 18 or century == 22:
        return 5
    if century == 15 or century == 19:
        return 3
    return 0

def calculate_anchor_day(date: list[int])->Day:
    
    date_to_check = date
    print("debug" +str(date_to_check[YEAR])[:2] + " "  + str(date_to_check[YEAR])[2:])

    fist_part_year:int = int(str(date_to_check[YEAR])[:3])
    last_part_year:int = int(str(date_to_check[YEAR])[3:])
    temp:int 

    if not is_paired(last_part_year):
        temp = last_part_year + 11
        temp = temp / 2
        if not is_paired(temp):
            temp = last_part_year + 11
            temp = temp / 2
    else:
        temp = last_part_year
    
    multiple_of_7_lower: int = multiple_of_7_lower_than(temp)

    the_current_day:int = temp - multiple_of_7_lower + in_function_of_century(fist_part_year)

    the_day: Day
    if the_current_day % 7 == 0:
        return Day.SUNDAY
    elif the_current_day % 7 == 1:
        return Day.MONDAY
    elif the_current_day % 7 == 2:
        return Day.TUESDAY
    elif the_current_day % 7 == 3:
        return Day.WEDNESDAY
    elif the_current_day % 7 == 4:
        return Day.THURSDAY
    elif the_current_day % 7 == 5:
        return Day.FRIDAY
    elif the_current_day % 7 == 6:
        return Day.SATURDAY
