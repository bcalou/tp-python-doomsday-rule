import doomsday
from doomsday import date

input_date:str = ""
has_error:bool = False
is_valide_date:bool = False
while(not input_date.isdigit() and not is_valide_date):
    if(has_error):
        print("Ce n'est pas une date valide")
    is_a_wrong_date=True
    input_date = input("Rentrer une date au format YYYY-MM-dd (mettre les '-' sans espace entre les champs) : \n")
    if(date.is_valid_date(input_date)):
        is_valide_date = True
