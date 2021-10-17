from doomsday.day import DAYS
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

def calculate_anchor_day(date: list[int])->str:
    
    date_to_check = date

    fist_part_year:int = int(str(date_to_check[YEAR])[:2])
    last_part_year:int = int(str(date_to_check[YEAR])[2:])
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
    # debug
    # print("fist_part_year : " + str(fist_part_year))    
    # print("last_part_year : " + str(last_part_year))    
    # print("temp : " + str(temp))    
    # print("multiple de 7 le plus proche : " + str(multiple_of_7_lower))    
    # print("in_function_of_century : " + str(fist_part_year))

    the_current_day:int = (temp - multiple_of_7_lower) + in_function_of_century(fist_part_year)
    print("the current day " + str(the_current_day))

    # the_day: str
    # if the_current_day % 7 == 0:
    #     return DAYS[0]
    # elif the_current_day % 7 == 1:
    #     return DAYS[1]
    # elif the_current_day % 7 == 2:
    #     return DAYS[2]
    # elif the_current_day % 7 == 3:
    #     return DAYS[3]
    # elif the_current_day % 7 == 4:
    #     return DAYS[4]
    # elif the_current_day % 7 == 5:
    #     return DAYS[5]
    # elif the_current_day % 7 == 6:
    #     return DAYS[6]

    return DAYS[(int)(the_current_day % 7)]
