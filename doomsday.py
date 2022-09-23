from doomsday.date import is_valid_date
from doomsday.algorithm import get_day_for_date

# Commencez ici !

# Greeting text
print("Hello Doomsday !")
print("Bienvenue sur ’algorithme du jour du jugement dernier !\n")


is_input_date_valid: bool = False
date_input: str = ""

# Re ask date input until a valid date is given 
while not is_input_date_valid:

    # Instructions
    date_input = input("Veuillez indiquer la date au format YYYY-MM-dd :\n\n")
    is_input_date_valid = is_valid_date(date_input)
