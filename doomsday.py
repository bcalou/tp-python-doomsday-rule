from doomsday.date import is_valid_date
import doomsday.algorithm as algo

print("Entrez une date au format YYYY-MM-dd")

while True :
    selected_date : str = input()
    if is_valid_date(selected_date):
        break
    print(selected_date + " n'est pas valide")

print(algo.get_century_marker(int(selected_date[:4])))
