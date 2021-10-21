from doomsday import algorithm

def is_valid_date(date: str) -> bool:
    
    if(str(date).count("-") <2):
        print("Il n'y a pas ou manque des '-' dans la date")
        return False
    dates = date.split("-")
    return format_validation_input_date(dates)

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
    return format_validation_year(dates)

def format_validation_year(dates:list[str])->bool :
    if(int(dates[0]) > 1583):
        return format_validation_month(dates)
    print("Année invalide, mettez une année postérieur à 1583")
    return False

def format_validation_month(dates:list[str])->bool :
    if(int(dates[1]) >= 1 and int(dates[1]) <=12) :
        return format_validation_day(dates)
    print("Mois invalide, mettez un mois entre 01 et 12")
    return False

def format_validation_day(dates:list[str])->bool :
    MONTHS: list[list[int]] = [[1,3,5,7,8,10,12],[4,5,9,11]]
    if(MONTHS[0].count(int(dates[1])) == 1):
        return long_months_validation_day(dates)
    elif(MONTHS[1].count(int(dates[1])) == 1):
        return not_long_months_validation_day(dates)
    else :
        return leap_year_validation_day(dates)
       

def long_months_validation_day(dates:list[str]):
    if(int(dates[2])>=1 and int(dates[2])<=31):
        print("Date valide")
        return True
    else:
        print("Date invalide, pour le mois : " 
        + dates[1] 
        + " le jour doit être compris entre 1 et 31 inclus")
        return False

def not_long_months_validation_day(dates:list[str]):
    if(int(dates[2])>=1 and int(dates[2])<=30):
        print("Date valide")
        return True
    else:
        print("Date invalide, pour le mois : " 
        + dates[1] 
        + " le jour doit être compris entre 1 et 30 inclus")
        return False

def leap_year_validation_day(dates:list[str]):
    if(algorithm.is_leap_year(int(dates[0]))):
        if(int(dates[2])>=1 and int(dates[2])<=29):
            print("Date valide")
            return True
        else:
            print("Date invalide, pour le mois : " 
            + dates[1] 
            + " le jour doit être compris entre 1 et 29 inclus")
            return False
    else:
        if(int(dates[2])>=1 and int(dates[2])<=28):
            print("Date valide")
            return True
        else:
            print("Date invalide, pour le mois : " 
            + dates[1] 
            + " le jour doit être compris entre 1 et 28 inclus")
            return False