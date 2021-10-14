import math

EASY_CENTURY_TAG : list[list[int]] = [[19,20,21,22],[5,3,2,0]]
    

def get_day_for_date(date: str) -> str:
    return "Monday"


def is_leap_year(year : int) :

    if(year%4 == 0):
        if (year%100 == 0 ) :
            if (year%400 ==0) :
                return True
            else :
                return False
        else :
            return True
    else : 
        return False


#def get_century_tag(year : int ) -> int :
#    century : float = math.trunc(year/100) + 1
#    for centuries in EASY_CENTURY_TAG :
#        if century == EASY_CENTURY_TAG[0][centuries]:
            
        


#    return 0


def get_day_anchor(date : list[str]) -> str :
    month : int = int(date[2])
    if month%2 == 0 and month > 3 :
        return str(month)
    elif month%2 != 0 and month > 2 :
        if month == 3 : return "0"
        elif month == 5 : return "9"
        elif month == 9 : return "5"
        elif month == 7 : return "11"
        elif month == 11 : return "7"
    else:
        if is_leap_year(int(date[1])) :
            if month == 1 : return "11"
            elif month == 2 : return "22"
        else :
            if month == 1 : return "10"
            elif month == 2 : return "21"
            

    return "null"

#def get_the_day_of_year() :
