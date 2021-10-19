days: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def get_day_for_date(date: str) -> str:
    return "Monday"

def anchor_day(date: str) -> str:
    year: str = date[:4]
    two_last_numbers_of_year: float = int(year[2:])
    number_of_the_day: float = 0
    difference: int = 0
    day_anchor: str = ""
    for i in range(2):
        if is_odd_number(two_last_numbers_of_year) and i == 0:
            number_of_the_day = (two_last_numbers_of_year + 11) / 2
        elif is_odd_number(number_of_the_day) and i == 1:
            number_of_the_day += 11
        else:
            break
    difference = int(first_multiple_of_7_above_number(number_of_the_day) - number_of_the_day)
    day_anchor = days[(difference + number_of_century(year)) % 7]

    return day_anchor

def is_odd_number(number: float) -> bool:
    if (number % 2 != 0):
        return True
    return False

def first_multiple_of_7_above_number(number: float) -> float:
    response: bool = False
    multiple_of_seven = 0
    count = 1
    while response == False:
        multiple_of_seven = 7 * count
        if multiple_of_seven >= number:
            response = True
            return multiple_of_seven
        else:
            count += 1
    return multiple_of_seven

def number_of_century(year: str) -> int:
    two_first_number_of_year = int(year[:2])
    control_number: int = 15
    list_possible_numbers: list[int] = [3, 2, 0, 5]

    #il y a 4 possibilité, elle change tous les siècles mais toujours dans le même ordre donc en partant de 15
    #(on commence au 15ème siècle) si je fais le modulo de la différence entre le siècle donné et 15 je retombe sur la bonne catégorie
    #à condition de les avoir mis dans le même ordre dans la liste
    #exemple : pour 1580 on prend 15 - 15 ça fait 0, 0 % 4 = 0 donc première catégorie on ajoute 3
    #2100 on prend 21 - 15 = 6 % 4 = 2 on tombe sur la troisième catégorie donc on ajoute 0
    return list_possible_numbers[(two_first_number_of_year-control_number) % 4]
