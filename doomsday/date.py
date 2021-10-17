from re import match
def is_valid_date(date: str) -> bool:
    normal_year_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
    if not isinstance(date, str):
        return False
    if not match(r"(\d{4}-\d{1,2}-\d{1,2})", date):
        return False
    else:
        year = int(date[0:4])  
        month = int(date[5:7])  
        day = int(date[8:])  

        isLeapYear = False
        if (year % 4 == 0 and year % 100 != 0 ) or (year % 400) == 0:
            isLeapYear = True
        if year < 1583:
            return False
        if month < 1 or month > 12:  
            return False
        if isLeapYear:
            if day < 1 or day > leap_year_month[month]:
                return False
        else:
            if day < 1 or day > normal_year_month[month]:
                return False
        return True
