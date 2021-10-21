from doomsday.date import is_leap_year, is_valid_date

START_DAYS: list[int] = [10, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
DAYS: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def get_day_for_date(date: str) -> str:
    if is_valid_date(date):
        year: str = date.split('-')[0]
        month: str = date.split('-')[1]
        day: str = date.split('-')[2]
        start_day = get_start_day(year, month)
        anchor_day = get_anchor_day(year)

        #si on enlève à l'index du jour ancre, la différence modulo 7 entre le jour de départ et le jour donnée 
        #on obtient le jour de la liste correspondant au décalage
        #exemple si le jour ancre est un mercredi et que le jour de départ est le 4 (pour avril) et le jour donnée le 5
        #l'index du jour est 3, la différence = 4 - 5 = -1, -1 % 7 = 6, 3 - 6 = -3, en partant de la fin de la liste
        #on tombe sur Thursday donc le jour juste après Wednesday
        return DAYS[(DAYS.index(anchor_day) - (start_day - int(day)) % 7)] 
    else:
        print("Date non valide")
        return ""

def get_anchor_day(year: str) -> str:
    two_last_numbers_of_year: float = int(year[2:])
    number_of_the_day: float = 0

    if is_odd_number(two_last_numbers_of_year):
        number_of_the_day = two_last_numbers_of_year + 11

    number_of_the_day = number_of_the_day / 2 

    if is_odd_number(number_of_the_day):
        number_of_the_day += 11
  
    difference = int(first_multiple_of_7_above_number(number_of_the_day) - number_of_the_day)
    anchor_day = DAYS[(difference + anchor_of_century(year)) % 7]

    return anchor_day

def is_odd_number(number: float) -> bool:
    return number % 2 != 0

def first_multiple_of_7_above_number(number: float) -> float:
    #si le nombre est un multiple de 7 on le renvoie tel quel
    #si non on lui ajoute ce qu'il lui manque pour atteindre le multiple suivant
    return number if number % 7 == 0 else number + 7 - (number % 7)

def anchor_of_century(year: str) -> int:
    two_first_number_of_year = int(year[:2])
    control_number: int = 15
    list_possible_numbers: list[int] = [3, 2, 0, 5]

    #il y a 4 possibilité, elle change tous les siècles mais toujours dans le même ordre donc en partant de 15
    #(on commence au 15ème siècle) si je fais le modulo de la différence entre le siècle donné et 15 je retombe sur la bonne catégorie
    #à condition de les avoir mis dans le même ordre dans la liste
    #exemple : pour 1580 on prend 15 - 15 ça fait 0, 0 % 4 = 0 donc première catégorie on ajoute 3
    #2100 on prend 21 - 15 = 6 % 4 = 2 on tombe sur la troisième catégorie donc on ajoute 0
    return list_possible_numbers[(two_first_number_of_year-control_number) % 4]

def get_start_day(year: str, month: str) -> int:
    if is_leap_year(year) and (int(month) == 1 or int(month) == 2):
        return START_DAYS[int(month) - 1] + 1
    else:
        return START_DAYS[int(month) - 1]
