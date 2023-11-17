

def main() -> None: 
    """fonction principale du TP"""
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

    can_launch_algo = is_valid_date(date, year, month, day)
    
    if(can_launch_algo):
    
        print("Date Valide ! ")
        anchor_calc(year, month, day)
    
    else:
        
        print("Date invalide, veuillez recommencer")
        return 
    

    
    
    
    
    
def is_valid_date(date :str, year: int, month: int, day: int) -> bool:
    """Permet de savoir si la date ne présente aucune erreur"""
    
    
    
    is_leap_year = year_is_leap_year(year)
    

    if(year < 1583 or year > 2200):
        print("ERREUR : l'année est invalide")
        return False
        
    if(month < 0 or month > 12):
        print("ERREUR : Le mois est invalide")
        return False
        
    if(day < 0 or (day > 31 and (month == 1 or month == 3 or month == 5 or 
        month == 7 or month == 8 or month == 10 or month == 12)) or 
       day > 30 and (month == 4 or month == 6 or month == 9 or month == 11) or 
       ((day > 28 and not is_leap_year) or 
        (day > 29 and is_leap_year))) and month == 2:
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
    print("2 derniers chiffre de l'année : "+two_last_numbers_year)
    anchor = int(two_last_numbers_year)
    anchor = first_stage(anchor)
    print("premier calcul impair pair : "+str(anchor))
    anchor = seven_multiple(anchor)    
    print("distance avec le plus grand multipe de 7 : " + str(anchor))
    # donne le jour ancre de l'année
    year_anchor = get_year_anchor(anchor, year)
    if ( year_anchor >= 7 ):
        year_anchor -= 7
    print("jour ancre de l'année : " + str(year_anchor))
    # donne le jour sur lequel tombera le jour ancre en focntion du mois et de l'année 
    month_anchor = get_month_anchor(year_anchor, month, year)
    print("jour ancre du mois : "+ str(month_anchor))
    final_day = last_stage(year_anchor,month_anchor, day)
    print("écart entre le jour de l'utilisateur et le jour ancre : " + str(final_day))
    final_day = abs(final_day) + year_anchor
    if (final_day >= 7):
        final_day = final_day - 7
    print("le jour final est : " +str(final_day))
    print_result(year, month, day, (final_day))
            
    return anchor

def first_stage(two_last_numbers: int) -> int:
    # si il est impair
    if(two_last_numbers % 2 != 0): 
        # on ajoute 11 et on divise par 2
        two_last_numbers += 11
        two_last_numbers = two_last_numbers // 2 
        if(two_last_numbers % 2 != 0):
            # si le nombre est de nouveau impaire on réajoute 11
            two_last_numbers += 11
    else:
        two_last_numbers = two_last_numbers // 2
        if (two_last_numbers % 2 != 0):
            two_last_numbers += 11
             
    return two_last_numbers

def seven_multiple(anchor: int) -> int: 
    anchor = 7 - anchor % 7
    return anchor

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
   
def last_stage(year_anchor: int, month_anchor: int, day) -> int:
    """year = jour ancre de l'année month = jour sur lequel tombera le jour
    ancre en fonction de l'année day = jour demandé par l'utilisateur"""
    
    
    final_day = month_anchor - day # 0 - 18 = -18
    print("test :")
    print(final_day)
    
    if (0 <= final_day <= 7):
        return final_day
    elif ( -7 <= final_day < 0 ):
        return final_day * -1
    elif (final_day < 0):
        while ( final_day <= -7 ):
            final_day += 7
            print(final_day)
        return final_day * -1
    else:
        while ( final_day > 0 ):
            final_day -= 7
        return final_day
    
    #if(month_anchor - day >= 0): # m = 12 d = 16
    #     if(month_anchor - day <= 7):
    #         return month_anchor - day
    #     else:
    #         while(month_anchor - day >= 7):
    #             month_anchor = month_anchor - 7
    #             if ( month_anchor - day <= 7 ):
    #                 return month_anchor - day
    # else: # m = 0 d = 2
    #     if(month_anchor + day <= 7):
    #         return month_anchor + day
    #     else:
    #         while(month_anchor + day >= 7):
    #             month_anchor = month_anchor + 7
    #             if ( month_anchor + day <= 7 ):
    #                 return month_anchor + day
    
    
    return 0 

def print_result(year: int, month: int, day: int, final_day: int):
    print("Le "+ str(day) + " " + get_month_str(month) + " " + str(year) + 
          " est un " + get_day_str(final_day))
    
    
def get_month_str(month: int) -> str:
    if (month == 1):
        return "Janvier"
    if (month == 2):
        return "Fevrier"
    if (month == 3):
        return "Mars"
    if (month == 4):
        return "Avril"
    if (month == 5):
        return "Mai"
    if (month == 6):
        return "Juin"
    if (month == 7):
        return "Juillet"
    if (month == 8):
        return "Aout"
    if (month == 9):
        return "Septembre"
    if (month == 10):
        return "Octobre"
    if (month == 11):
        return "Novembre"
    if (month == 12):
        return "Decembre"
    
    return ""

def get_day_str(day: int) -> str: 
    if (day == 0):
        return "Dimanche"
    if (day == 1):
        return "Lundi"
    if (day == 2):
        return "Mardi"
    if (day == 3):
        return "Mercredi"
    if (day == 4):
        return "Jeudi"
    if (day == 5):
        return "Vendredi"
    if (day == 6):
        return "Samedi"
    return ""
     
main()
