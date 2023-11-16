

def main() -> None: 
    """fonction principale du projet"""
    date = str(input("Donner un date au format YYYY-MM-DD \n"))
    
    if (len(date) != 10):
        print("ERREUR : Le format n'a pas été respecté")
        return None
    yearStr = str(date[0]+date[1]+date[2]+date[3])
    monthStr = str(date[5]+date[6])
    dayStr = str(date[8]+date[9])
    
    try:
        year = int(yearStr)
        month = int(monthStr)
        day = int(dayStr)
    except ValueError:
        print("ERREUR : Nous attendons des chiffres")
        return None

    is_valid_date(date, year, month, day)
    print("Date Valide ! ")
    
    anchor_calc(year, month, day)
    
    

    
    
    
    
    
def is_valid_date(date :str, year: int, month: int, day: int) -> bool:
    """Permet de savoir si la date ne présente aucune erreur"""
    
    
    
    is_leap_year = year_is_leap_year(year)
    

    if(year < 1583 or year < 2200):
        print("ERREUR : l'année est invalide")
        return False
        
    if(month < 0 or month > 12):
        print("ERREUR : Le mois est invalides")
        return False
        
    if(day < 0 or (day > 31 and (month == 1 or month == 3 or month == 5 or 
        month == 7 or month == 8 or month == 10 or month == 12)) or 
       day > 30 and (month == 4 or month == 6 or month == 9 or month == 11) or 
       (day > 28 and not is_leap_year) or (day > 29 and is_leap_year)):
        print("ERREUR : Le jour est invalide")
        return False
    
    return True
    
def year_is_leap_year(year: int) -> bool:
    """Permet de savoir si une année est bisextille"""
    if(year % 4 != 0):
        return False
    elif(year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True
    
def anchor_calc(year: int, month: int, day: int) -> int:
    two_last_numbers_year = str(year)[2]+str(year)[3]
    print(two_last_numbers_year)
    anchor = int(two_last_numbers_year)
    anchor = first_stage(anchor)
    anchor = seven_multiple(anchor)
    year_anchor = get_year_anchor(anchor, year)
    month_anchor = get_month_anchor(year_anchor, month, year)
    final_day = last_stage(year_anchor,month_anchor, day)
            
    return anchor

def first_stage(two_last_numbers: int) -> int:
    if(two_last_numbers % 2 != 0):
            two_last_numbers += 11
            two_last_numbers = two_last_numbers // 2
            if(two_last_numbers % 2 != 0):
                two_last_numbers += 11
                two_last_numbers = two_last_numbers // 2
                
    return two_last_numbers

def seven_multiple(anchor: int) -> int:
    test_number = anchor
    counter = 0 
    while(True):
        anchor -= 7
        if(anchor < 0 ):
            break
        counter += 1
    test_number = test_number - 7 * counter
    return test_number

def get_year_anchor(anchor: int, year: int) -> int:
    if(1600 <= year <= 1699 or 2000 <= year <= 2099):
        return anchor + 2
    if(1700 <= year <= 1799 or 2100 <= year <= 2199):
        return anchor + 0
    if(1800 <= year <= 1899 or 2200 <= year <= 2299):
        return anchor + 5
    else:
        return anchor + 3
    
def get_month_anchor(anchor: int, month: int, year: int) -> int:
    is_leap_year = year_is_leap_year(year)
    if (month == 1):
        if (is_leap_year):
            return 11
        else : return 10
        
    if (month == 2):
        if(is_leap_year):
            return 22
        else : return 21
        
    if (month == 3):
        return 0
        
    if (month == 4):
        return 4
        
    if (month == 5):
        return 9
        
    if (month == 6):
        return 6
        
    if (month == 7):
        return 11
        
    if (month == 8):
        return 8

    if (month == 9):
        return 5
        
    if (month == 10):
        return 10
        
    if (month == 11):
        return 7
        
    else:
        return 12
   
   
#à finir faut rajouter le else bonne chance mon reuf 
def last_stage(year_anchor: int, month_anchor: int, day) -> int:
    if(month_anchor - year_anchor >= 0):
        if(month_anchor - year_anchor <= 7):
            return month_anchor - year_anchor
        else:
            while(month_anchor - year_anchor >= 7):
                month_anchor = month_anchor - 7
                if ( month_anchor - year_anchor <= 7 ):
                    return month_anchor - year_anchor
    
    return 0
main()
