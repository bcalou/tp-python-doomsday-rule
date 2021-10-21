from doomsday.algorithm import leap_year


def is_valide_input(date: str) -> bool:
    if(not(isinstance(date, str))):
        print("Error Format String Request")
        return False
    list_date = date.split('-')
    if(len(list_date) != 3):
        print("Error Format Date YYYY-MM-dd")
        return False
    return True


def is_valid_date(date: str) -> bool:
    if(is_valide_input(date)):
        list_date = date.split('-')
        year = int(list_date[0])
        month = int(list_date[1])
        day = int(list_date[2])
        day_february = 28
        if(leap_year(year)):
            day_february = day_february+1
        if(month < 0 or month > 12):
            print("Error Date Month")
            return False
        elif((day < 1 or day > 31)):
            print("Error Date Day")
            return False
        elif(year < 1583):
            print("Error Date year < 1583")
            return False
        elif((month == 4 or month == 6 or month == 8 or month == 10 or month == 12) and day > 30):
            print("Error Date Day for Even Months")
            return False
        elif(month == 2 and day > day_february):
            print("Error Date Day for February")
            return False
        else:
            return True
    return False
