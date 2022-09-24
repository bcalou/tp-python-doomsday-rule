from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

def guess_week_day(date : str) -> str:

    days = 
    months =
    years = 

    anchor = anchor_day(years)
    


# Commencez ici !



def anchor_day(year:int) -> int:
    '''
    Anchor day
    '''
    century = year // 100
    c = century % 4
    anchor_day = (2 + 5 * c) % 7
    return anchor_day



#..........................................................................#
'''Year'''
y = year % 10
if y % 2 == 0:
    '''Si c'est pair'''
    y = y / 2
else:
    y = (y + 11) / 2

if y % 2 != 0:
    y += 11

#return (anchor_day - y) % 7


print(doomsday(1973))

