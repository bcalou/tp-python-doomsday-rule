from doomsday.date import is_leap_year

# This function return the anchor day for a month given in input 
def month_finder(mois,year) -> int:
    months_figure_board = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    number = months_figure_board[mois-1]
    if((mois == 1 or mois == 2) and is_leap_year(year)):
        return number+1
    else:
        return number


# This function do the main calcul of doomsday algorithm:
# it returns a figure which corespond to the day without the figure of the year
def calcul(year) -> int:
    year_list = str(year)
    days = year_list[2]+year_list[3]
    days = int(days)

    if(days % 2 == 0):
        number = days/2
        if(number % 2 == 0):
            return -number%7
        else:
            return -(number+11)%7
    else:
        number = (days + 11)/2
        if(number % 2 == 0):
            return -number%7
        else:
            return -(number+11)%7


# This function returns a figure which is needed to be add to the calcul to have the day 
def find_year_figure(year_figure) -> int:
    modulo = year_figure % 400
    if(modulo >= 0 and modulo < 100):
        return 2
    elif(modulo >=100 and modulo<200):
        return 0
    elif(modulo >=200 and modulo<300):
        return 5
    return 3


# This function is the final function of the algorithm, it returns the day in format string
def get_day_for_date(date: str) -> str:
    split_date = date.split('-')
    year = int(split_date[0])
    month = int(split_date[1])
    days = int(split_date[2])

    days_board = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    day_key = int((calcul(year)+find_year_figure(year)))
    day_pivot = (month_finder(month,year))
    diff_day = (day_pivot - days)

    return days_board[(day_key-diff_day)%7]
