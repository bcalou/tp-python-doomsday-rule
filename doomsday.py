from doomsday.date import is_valid_date

print("Entrez une date au format YYYY-MM-dd")

while True :
    selected_date : str = input()
    if is_valid_date(selected_date):
        break
    print(selected_date + " n'est pas valide")

print(selected_date + " est valide")


