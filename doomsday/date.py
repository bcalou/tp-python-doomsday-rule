#Determines if the year is a leap year or not
def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#Determines if the day exists for a specified date
def does_day_exist(year:int, month: int, day: int) -> bool:
    MONTHS_WITH_31_DAYS: list[int] = [1, 3, 5, 7, 8, 10, 12]
    if month in MONTHS_WITH_31_DAYS:
        if day >= 1 and day <= 31:
            return True
        else:
            return False
    elif month == 2:
        if is_leap_year(year) == True:
            if day >= 1 and day <= 29:
                return True
            else:
                return False
        else:
            if day >= 1 and day <= 28:
                return True
            else:
                return False
    else:
        if day >= 1 and day <= 30:
            return True
        else:
            return False

#Determines if a date is valid
def is_valid_date(date: str) -> bool:
    #Checks for type, length, and length of each part
    if type(date) is str:
        if len(date) == 10:
            split_date: list[str] = date.split('-')
            if len(split_date) == 3:
                year = split_date[0]
                day = split_date[2]
                month = split_date[1]

                valid_year: bool = False
                valid_month: bool = False
                valid_day: bool = False

                if len(year) == 4 and year.isnumeric() and year.isdigit():
                    year = int(year)
                    if year < 1583:
                        return False
                    else:
                        valid_year: bool = True
                if len(month) == 2 and month.isnumeric() and month.isdigit():
                    month = int(month)
                    if month > 12 or month < 1:
                        return False
                    else:
                        valid_month: bool = True
                if len(day) == 2 and day.isnumeric() and day.isdigit():
                    day = int(day)
                    if does_day_exist(year, month, day) == False:
                        return False
                    else:
                        valid_day: bool = True
                #If everything is valid, return True
                if valid_year and valid_month and valid_day:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False