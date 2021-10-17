from doomsday.day import DAYS

def is_paired(n: int)->bool:
    if (n % 2) == 0:
        return True
    return False

def multiple_of_7_lower_than(n: int)->int:
    return n + (7 - (n % 7))
    # return (n // 7) * 7

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

def calculate_anchor_day(current_year: int)->str:
    
    fist_part_year:int = int(str(current_year)[:2])
    last_part_year:int = int(str(current_year)[2:])

    if not is_paired(last_part_year):
        last_part_year = last_part_year + 11
        last_part_year = last_part_year / 2
        if not is_paired(last_part_year):
            last_part_year = last_part_year + 11
    
    multiple_of_7_lower: int = multiple_of_7_lower_than(last_part_year)
    # debug
    # print("last_part_year : " + str(last_part_year))    
    # print("multiple de 7 le plus proche : " + str(multiple_of_7_lower))    

    the_current_day:int = multiple_of_7_lower - last_part_year + in_function_of_century(fist_part_year)
    
    return DAYS[(int)(the_current_day % 7)]
