def are_valids_month_and_day(day:int, month:int)->bool:
    if not is_31_month(month) and day <= 30:
        return True
    elif is_31_month(month) and day <= 31:
        return True
    print("Error - Month and day are not compatible")
    return False

def is_31_month(month)->bool:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return True
    return False