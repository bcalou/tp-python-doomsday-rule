def get_day_for_date(date: str) -> str:
    return "Monday"

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def is_leap_year(year : int) :
    return ((year%4 == 0 and year%100!=0) or (year%100==0 and year%400==0))

def pivot_day(year : int, month : int) :
    pivot_day=0
    if (is_leap_year(year) and month==1 or month==2) :
        if (month==1) :
            pivot_day=11
        elif (month==2) :
            pivot_day=22
    else :
        if (month>2 and month%2==0) :
            pivot_day=month
        elif (month==1) :
            pivot_day=10
        elif (month==2) :
            pivot_day=21
        elif (month==3) :
            pivot_day=0
        elif (month==5) :
            pivot_day=9
        elif (month==7) :
            pivot_day=11
        elif (month==9) :
            pivot_day=5
        elif (month==11) :
            pivot_day=7
    return pivot_day

def century(year) :
    y=int(year[:-2])
    century=0
    if (y>=20) :
        t=y-20
    else :
        t=20-y
    if (t%4==0) :
        century=2
    elif(t%4==3) :
        century=0
    elif(t%4==2) :
        century=5
    elif(t%4==1) :
        century=3
    return century

def anchor_day(year) :
    y=int(year[-2:])
    anchor_day=0
    if (y%2 !=0) :
        y=y+11
        y=y/2
    else :
        y=y/2
    if (y%2!=0) :
            y=y+11
    day_number=0
    for i in range(0, 10) :
        if((7*i)>=y) :
            day_number=int(7*i-y+century(year))
            break
    if (day_number>6) :
        day_number=day_number-7
    for index, j in enumerate(DAYS) :
        if(day_number==index) :
            anchor_day=index
            break
    return anchor_day

def doomsday(date) :
    my_day=[] 
    day=date.split('-')[2]
    month=date.split('-')[1]
    year=date.split('-')[0]
    closest_anchor_day=pivot_day(int(year), int(month))
    my_anchor_day=anchor_day(year)
    day_index=0
    if (closest_anchor_day>int(day)) :
        day_index=closest_anchor_day-int(day)+my_anchor_day
    elif (closest_anchor_day<int(day)) :
        day_index=int(day)-closest_anchor_day+my_anchor_day
    while (day_index>6) :
        day_index=day_index-7
    for index, j in enumerate(DAYS) :
        if(day_index==index) :
            my_day=j
            break
    return my_day