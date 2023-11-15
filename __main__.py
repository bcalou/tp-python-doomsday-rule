def main() -> None:
    date: str = ask_for_valid_date()


def ask_for_valid_date() -> str:
    """Ask for a date until a valid one is given"""

    given_date: str = ""

    while True:
        print("De quelle date souhaitez vous connaître le jour ?")
        given_date = input()
        if is_valid_date(given_date) is True:
            return given_date
        else: 
            print("La date doit être donnée au format YYYY-MM-dd "
                "à compter de 1583")


def is_valid_date(date: str) -> bool:
    """Check if a date is valid"""

    splited_date: list[str] = date.split("-")
    
    #Verify if there is 3 parts on the date
    if len(splited_date) != 3:
        return False
    
    #Verify they are numbers
    for part in splited_date:
        if part.isdigit() is False:
            return False
    
    #Verify if year and month exist in our calendar
    if int(splited_date[0]) >= 1583 is False:
        return False
    
    if 1 > int(splited_date[1]) > 12:
        return False
    
    if (1 > int(splited_date[2]) > days_in_month(int(splited_date[0]), int(splited_date[1]))):
        return False



def days_in_month(year: int, month: int) -> int:
    return 28

main()
