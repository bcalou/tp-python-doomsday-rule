def main() -> None:
    """Fonction Main"""
    date_input_by_user = str(input("Saisir une date au format YYYY-MM-DD:"))
    input_is_date(date_input_by_user)

def input_is_date(date_result: str) -> bool:
    
    if len(date_result) != 10:
        print("Input date is not valid")
        return False
    
    years = int(date_result[:4])
    month = int(date_result[5:7])
    days = int(date_result[8:])
    
    try:
        if years <= 1583 or month > 12 or days > 31:
            print("Valeur fausse")
            return False
        
        return True
    except ValueError:
        print("Error car le format de la date n'est pas bon " + date_result)
        return False

main()
