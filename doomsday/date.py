from doomsday import algorithm

def is_valid_date(date: str) -> bool:
    dates = str(date).split("-")
    if(not len(dates) == 3):
        print("Il n'y a pas ou manque des '-' dans la date")
        return False
    if(format_validation_input_date(dates) 
    and format_validation_year(int(dates[0])) 
    and format_validation_month(int(dates[1])) 
    and format_validation_day(dates)):
        return True
    return False

def format_validation_input_date(dates:list[str])-> bool:
    is_wrong_date:bool = False
    if(len(dates[0])!= 4):
        is_wrong_date=True
        print("Année invalide, mettez une année postérieur à 1583 et au format YYYY")
    if(len(dates[1])!= 2):
        is_wrong_date=True
        print("Mois invalide, mettez un mois existant au format MM")
    if(len(dates[2])!= 2):
        is_wrong_date=True
        print("Jour invalide, mettez un jour existant au format dd")
    if(is_wrong_date):
        return False
    return True

def format_validation_year(year: int)->bool :
    if(year > 1583):
        return True
    print("Année invalide, mettez une année postérieur à 1583")
    return False

def format_validation_month(month: int)->bool :
    if(month >= 1 and month <=12) :
        return True
    print("Mois invalide, mettez un mois entre 01 et 12")
    return False

def format_validation_day(dates:list[str])->bool :
    MONTHS_DAY: list[int] = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(algorithm.is_leap_year(int(dates[0]))):
        MONTHS_DAY[1] = 29
    return True if int(dates[2]) > 0 and int(dates[2]) <= MONTHS_DAY[int(dates[1])-1] else False