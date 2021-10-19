from doomsday.day import DAYS

def is_even(n: int)->bool:
    """Return True if n is paired"""
    return ((n % 2) == 0)

def multiple_of_7_greater_than(n: int)->int:
    """Return the multiple of 7 greater than n"""
    return n + (7 - (n % 7))

def get_century_anchor(century: int)->int:
    """Return int in function of century"""
    # A vingt ans, il faisait déjà du 53 a un fonctionnement restreint. 
    # Du coup, on tranche tous les quatres siècles !
    return [2, 0, 5, 3][century%4]

def calculate_anchor_day(current_year: int)->str:
    """Return the anchor day as string"""
    fist_part_year:int = int(str(current_year)[:2])
    last_part_year:int = int(str(current_year)[2:])
    
    if not  is_even(last_part_year):
        last_part_year += 11

    last_part_year = last_part_year/2

    if not  is_even(last_part_year):
        last_part_year += 11
        
    multiple_of_7_lower: int = multiple_of_7_greater_than(last_part_year) 

    the_current_day:int = multiple_of_7_lower - last_part_year + get_century_anchor(fist_part_year)
    
    return DAYS[(int)(the_current_day % 7)]
