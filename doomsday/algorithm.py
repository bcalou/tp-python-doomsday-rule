from doomsday.toolbox import is_leap_year
from doomsday.toolbox import parse_date_to_ints

from doomsday.const import DAYS

def get_weekday_for_date(date: str) -> str:
    '''
        Returns the right day asked from the date (it's magic)
    '''
    split_date: list[int] = parse_date_to_ints(date)

    year: int = split_date[0]
    month: int = split_date[1]
    day: int = split_date[2]

    doomsday: int = get_doomsday(month, year)
    anchor_day: int = get_anchor_day(year)

    out_day = int((anchor_day + ((day - doomsday) % 7)) % 7)

    return DAYS()[out_day]


def get_anchor_day(year: int) -> int:
    '''
        Get the anchor day of the year
    '''

    anchor = year - ((year // 100) * 100)

    if anchor % 2 != 0 :
        anchor += 11
        anchor /= 2
    

    if anchor % 2 != 0 :
        anchor += 11

    anchor = 7 - (anchor % 7)
    century_anchor: int = get_century_anchor(year)

    return anchor + century_anchor


def get_century_anchor(year: int) -> int:
    '''
        Subshit from get_anchor_day() getting the century anchor
    '''

    century_basis = year // 100

    if century_basis % 4 == 15 % 4 :
        return 3
    elif century_basis % 4 == 16 % 4 :
        return 2
    elif century_basis % 4 == 17 % 4 :
        return 0
    else :
        return 5


def get_doomsday(month: int, year: int) -> int:
    '''
        Get the doomsday of the date
    '''
    # april, june, august, october, december
    if month in [4, 6, 8, 10, 12] :
        return month
    
    # march
    if month == 3 :
        return 0
    
    # january, february
    if (month == 1) :
        if(is_leap_year(year)) :
            return 11
        else :
            return 10
    
    #february
    if (month == 2) :
        if(is_leap_year(year)) :
            return 22
        else :
            return 21

    # may, july, september, november
    for tuple in [[5, 9], [7, 11]] :
        if month in tuple :
            if tuple.index(month) == 1 :
                return tuple[0]
            else :
                return tuple[1]

