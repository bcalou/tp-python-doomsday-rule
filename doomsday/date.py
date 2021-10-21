from doomsday.utils import is_leap_year

def is_valid_date(date: str) -> bool:
    day=date.split('-')[2]
    month=date.split('-')[1]
    year=date.split('-')[0]
    if ((len(year) < 4) or (len(day) != 2) or (len(month) != 2) ) :
        return False
    elif (int(day)<1 ) :
        return False
    elif ((int(month)<1) or (int(month)>12) ) :
        return False
    elif ((int(year)<1583)) :
        return False
    elif (int(month) in [1,3,5,7,8,10,12]) :
        if (int(day)>31) :
            return False
    elif (int(month) in [4,6,9,11]) :
        if (int(day)>30) :
            return False
    elif (int(month)==2) :
        if (is_leap_year(int(year))==True) :
            if (int(day)>29) :
                return False
        elif (int(day)>28) :
            return False
    return True

print(is_valid_date('1996-02-29'))