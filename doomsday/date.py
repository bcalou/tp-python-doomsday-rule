def is_valid_date(date_input: str) -> bool:
    
    #Je vérifie que la date ne soit pas trop courte
    if not 8<=len(date_input) :
        print("Erreur: La date ne correspond pas au format demandé.")
        return False
    #Je sépare la date pour pouvoir l'exploiter
    split_date: list[str] = date_input.split('-')

    #Je vérifie que la date est bien sous forme décimale
    for part_date in split_date:
        if not part_date.isdecimal():
            print("Erreur: la date n'est pas écrite en décimale.")
            return False

    #Je vérifie que l'année est bien supérieure ou égale à 1583.
    if not (1583 <= int(split_date[0])) :
        print("Erreur: l'année ne peut pas être inférieur à 1583.")
        return False
    else:

    #Je vérifie que le mois est bien compris entre 1 et 2
        if not (1 <= int(split_date[1]) <= 12) :
            print("Erreur: le mois n'existe pas.")
            return False
        else:

    #Je vérifie le nombre de jour dans le mois et si celui proposé par l'utilisateur est donc valide.
            if is_31_days_mounth(split_date[1]):
                if not ( 1 <= int(split_date[2]) <= 31):
                    print("Erreur: le jour n'existe pas.")
                    return False
            elif int(split_date[1]) == 2 :
                if not (1 <= int(split_date[2]) <= 29) and is_leap_year(split_date[0]) :
                    print("Erreur: le jour n'existe pas.")
                    return False
                elif not (1 <= int(split_date[2]) <= 28) and not is_leap_year(split_date[0]):
                    print("Erreur: le jour n'existe pas.")
                    return False
            else:
                if not ( 1 <= int(split_date[2]) <= 30):
                    print("Erreur: le jour n'existe pas.")
                    return False
    return True
        
            
def is_31_days_mounth(mounth_tested:str)-> bool:
    #Fonction de vérification du nombre total de jour dans un mois
    if (int(mounth_tested) == 1 or int(mounth_tested) == 3
        or int(mounth_tested) == 5 or int(mounth_tested) == 7
        or int(mounth_tested) == 8 or int(mounth_tested) == 10
        or int(mounth_tested) == 12) :
        return True
    else :
        return False


def is_leap_year(year_tested:str) -> bool:
    #Fonction de vérification d'une année bisextile
    if (int(year_tested)%400==0):
        return True
    elif not (int(year_tested)%100==0) and (int(year_tested)%4==0):
        return True
    else :
        return False