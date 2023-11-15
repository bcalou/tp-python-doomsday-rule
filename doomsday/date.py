def is_valid_date(date: str) -> bool:
    """Check if a date is valid"""

    splited_date: list[str] = date.split("-")
    
    #Verify there is 3 parts on the date
    if len(splited_date) != 3:
        print("La date doit être au format YYYY-MM-dd")
        return False
    
    #Verify they are numbers
    for part in splited_date:
        if part.isdigit() is False:
            print("La date ne peut contenir que des nombres")
            return False
    
    #Verify if year and month exist in our calendar
    if int(splited_date[0]) < 1583:
        print("Les dates ne sont prises en compte qu'à partir de 1583")
        return False
    
    if (1 > int(splited_date[1])) or (int(splited_date[1]) > 12):
        print("Les mois ne vont que de 1 à 12")
        return False
    
    #Verify if the day is correct
    days_in_this_month: int = days_in_month(
        int(splited_date[0]), int(splited_date[1]))
    
    if (1 > int(splited_date[2])) or (
        int(splited_date[2]) > days_in_this_month):
        print("Pour le mois renseigné, les jours vont de 1 à ",
               days_in_this_month)
        return False
    
    return True


def days_in_month(year: int, month: int) -> int:
    """gives the number of days in february, depending on year"""

    if month == 2:
        return 29 if year % 4 == 0 and (
            year % 100 != 0 or year % 400 == 0) else 28
        
    days_per_month: list[int] = [
        31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]

    return days_per_month[month-1]
    
