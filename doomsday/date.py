from doomsday import algorithm

def is_valid_date(date: str) -> bool:
    dates:list[str] = []
    dates = date.split("-")
    return first_validation_input_date(dates)

def first_validation_input_date(dates:list[str])-> bool:
    is_wrong_date:bool = False
    if(len(dates[0])!= 4):
        is_wrong_date=True
        print("Année invalide, mettez une année postérieur à 1583 et au format YYYY")
    if(len(dates[0])!= 2):
        is_wrong_date=True
        print("Mois invalide, mettez un mois existant au format MM")
    if(len(dates[0])!= 2):
        is_wrong_date=True
        print("Jour invalide, mettez un jour existant au format dd")
    if(is_wrong_date):
        return False
    else :
        return second_validation_year(dates)

def second_validation_year(dates:list[str])->bool :
    if(int(dates[0]) > 1583):
        return third_validation_month(dates)
    print("Année invalide, mettez une année postérieur à 1583")
    return False

def third_validation_month(dates:list[str])->bool :
    if(int(dates[1]) >= 1 and int(dates[1]) <=12) :
        return fourth_validation_day(dates)
    print("Mois invalide, mettez un mois entre 01 et 12")
    return False

def fourth_validation_day(dates:list[str])->bool :
    if(int(dates[1]) != 2 and int(dates[1])%2 == 0 and int(dates[1]) >= 1):
        return pair_months_validation_day(dates)
    elif(int(dates[1]) != 2 and int(dates[1]) >= 1):
        return not_pair_months_validation_day(dates)
    else :
        return leap_year_validation_day(dates)
       

def pair_months_validation_day(dates:list[str]):
        if(int(dates[2])>=1 and int(dates[2])<=31):
            print("Date valide")
            return True
        else:
            print("Date invalide, pour le mois : " 
            + dates[1] 
            + " le jour doit être compris entre 1 et 31 inclus")
            return False

def not_pair_months_validation_day(dates:list[str]):
        if(int(dates[2])>=1 and int(dates[2])<=30):
            print("Date valide")
            return True
        else:
            print("Date invalide, pour le mois : " 
            + dates[1] 
            + " le jour doit être compris entre 1 et 30 inclus")
            return False

def leap_year_validation_day(dates:list[str]):
    if(is_leap_year(int(dates[0]))):
        if(int(dates[2])>=1 and int(dates[2])<=29)
            print("Date valide")
            return True
        else:
            print("Date invalide, pour le mois : " 
            + dates[1] 
            + " le jour doit être compris entre 1 et 29 inclus")
            return False
    else:
        if(int(dates[2])>=1 and int(dates[2])<=28)
            print("Date valide")
            return True
        else:
            print("Date invalide, pour le mois : " 
            + dates[1] 
            + " le jour doit être compris entre 1 et 28 inclus")
            return False