def bixestil(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def months_finder(month, year):
    switcher = {
        1: 10,
        2: 21,
        3: 0,
        4: 4,
        5: 9,
        6: 6,
        7: 11,
        8: 8,
        9: 5,
        10: 10,
        11: 7,
        12: 12
    }
    number = int(switcher.get(month, "Invalid months"))
    if((month == 1 or month == 2) and bixestil(year)):
        return number+1
    else:
        return number


def calculation_year(year):
    list_year = str(year)
    day = list_year[2]+list_year[3]
    day = int(day)
    if(day % 2 == 0):
        number = day/2
        if(number % 2 == 0):
            return -number % 7
        else:
            return -(number+11) % 7
    else:
        number = (day + 11)/2
        if(number % 2 == 0):
            return -number % 7
        else:
            return -(number+11) % 7


def year_century(year_century):
    modulo = year_century % 400
    if(modulo >= 0 and modulo < 100):
        return 2
    elif(modulo >= 100 and modulo < 200):
        return 0
    elif(modulo >= 200 and modulo < 300):
        return 5
    return 3


def get_day_for_date(date: str):
    list_date = date.split('-')
    year = int(list_date[0])
    month = int(list_date[1])
    day = int(list_date[2])
    days = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    day_key = int((calculation_year(year)+year_century(year)))
    day_pivot = (months_finder(month, year))
    diff_day = (day_pivot - day)

    return days[(day_key-diff_day) % 7]
