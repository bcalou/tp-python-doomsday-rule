# This function return if the year given is bisextil or not
def is_leap_year(year) -> int:
    return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


# This function check if the month given is valid
def is_odd(a_month) -> bool:
    return a_month == 4 or a_month == 6 or a_month == 9 or a_month == 11


# This function check if the year given is valid
def year_verification(a_year)-> bool:
    if a_year > 1583:
        return True
    
    print("The year enter is not valid")
    return False


# This function check if the date give by the user is valid
def month_verification(a_month) -> bool:
    if(a_month > 0 and a_month <= 12):
        return True
    
    print("The month enter is not valid")
    return False


# This function check if the day of a date is valid, but we have to know if the year is bisextil so we need the month 
# the year.
def day_verification(a_year, a_month, a_day) -> bool:
    is_year_bisextil = is_leap_year(a_year)
    is_month_odd = is_odd(a_month)

    if(month_verification(a_month)):
        if(a_month == 2):
            if is_year_bisextil:
                if(a_day > 0 and a_day <= 29):
                    return True
            else:
                if(a_day > 0 and a_day <= 28):
                    return True

        elif(is_month_odd and a_month != 2 and a_day <= 30 and a_day>0):
            return True

        elif(not is_month_odd and a_month != 2 and a_day>0 and a_day <= 31):
            return True

    print("The day enter is not valid")
    return False
    
    
# This function check if the date give by the user is valid
def is_valid_date(date: str) -> bool:

    if(not isinstance(date, str)):
        return False

    split_date = date.split("-")
    if(len(split_date) == 3):
        if(str.isnumeric(split_date[0]) and str.isnumeric(split_date[1]) and str.isnumeric(split_date[2])):
            year = int(split_date[0])
            month = int(split_date[1])
            day = int(split_date[2])
        else:
            print("This is not a date in format YYYY-MM-dd")
            return False
    else:
        print("This is not a date in format YYYY-MM-dd")
        return False

    return year_verification(year) and month_verification(month) and day_verification(year, month, day)


