def is_leap_year(year : int) :
    return ((year%4 == 0 and year%100!=0) or (year%100==0 and year%400==0))

def is_valid_date(date: str) -> bool:
    valid=True
    day=date.split('-')[2]
    month=date.split('-')[1]
    year=date.split('-')[0]
    if ((len(year) > 4) or (len(day) > 2) or (len(month) > 2) ) :
        valid=False
        print("Invalid date format.")
    elif (int(day)<1 ) :
        valid=False
        print("Day number does not exist.")
    elif ((int(month)<1) or (int(month)>12) ) :
        valid=False
        print("Month does not exist.")
    elif ((int(year)<1583)) :
        valid=False
        print("Year should be higher than 1582.")
    elif (int(month) in [1,3,5,7,8,10,12]) :
        if (int(day)>31) :
            valid=False
            print("Day number does not exist in month "+month+".")
    elif (int(month) in [4,6,9,11]) :
        if (int(day)>30) :
            valid=False
            print("Day number does not exist in month "+month+".")
    elif (int(month)==2) :
        if (is_leap_year(int(year))==True) :
            if (int(day)>29) :
                valid=False
                print("Day number does not exist in month "+month+".")
        elif (int(day)>28) :
            valid=False
            print("Day number does not exist in month "+month+".")
    return valid