

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
    
    anchor_day(year)
    
    

    
    
    
    
    
def is_valid_date(date :str, year: int, month: int, day: int) -> bool:
    """Permet de savoir si la date ne présente aucune erreur"""
    
    
    
    is_leap_year = year_is_leap_year(year)
    

    if(year < 1583):
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
    
def anchor_day(year: int) -> int:
    two_last_numbers_year = str(year)[2]+str(year)[3]
    print(two_last_numbers_year)
    anchor = int(two_last_numbers_year)
    return anchor

main()
