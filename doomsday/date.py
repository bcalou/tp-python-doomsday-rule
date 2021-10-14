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


def is_valid_date(date: str) -> bool:
    if(not(isinstance(date, str))):
        print("Error Format String Request")
        return False
    count_dash = 0
    for char in date:
        if(char == "-"):
            count_dash = count_dash + 1
    if(count_dash != 2):
        print("Error Format Missing Dash")
        return False
    list_date = date.split('-')
    if(len(list_date) != 3):
        return False
    year = int(list_date[0])
    month = int(list_date[1])
    day = int(list_date[2])
    day_february = 28
    if(bixestil(year)):
        day_february = day_february+1
    if (month < 0 or month > 12) or (day < 1 or day > 31) or year < 1583:
        if(month < 0 or month > 12):
            print("Error Date Month")
        elif((day < 1 or day > 31)):
            print("Error Date Day")
        else:
            print("Error Date year < 1583")
        return False
    elif((month == 4 or month == 6 or month == 8 or month == 10 or month == 12) and day > 30):
        print("Error Date Day for Peer Months")
        return False
    elif(month == 2 and day > day_february):
        print("Error Date Day for February")
        return False
    else:
        return True
