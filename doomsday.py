from doomsday import date

input_date:str = ""
is_valid_date:bool = False
while(not is_valid_date):
    is_a_wrong_date=True
    input_date = input("Rentrer une date au format YYYY-MM-dd (mettre les '-' sans espace entre les champs) : \n")
    if(date.is_valid_date(input_date) and input_date.isdigit()):
        is_valide_date = True
