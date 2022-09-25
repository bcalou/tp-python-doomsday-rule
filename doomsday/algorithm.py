global date_list; date_list: list[int] = []
global year; year: int = 0
global month; month: int = 0
global day; day: int = 0


def get_day_for_date(date: str) -> str:
    reset_global_variables()
    parse_string_date_to_variables(date)
    get_anchor_day(year)
    #store_values_from_date_list_in_variables()
    return "Monday"


def reset_global_variables():
    #global str_date_list
    global date_list
    global year, month, day
    #str_date_list = []
    date_list = []
    year = 0
    month = 0
    day = 0


def parse_string_date_to_variables(date: str):
    global date_list
    global year, month, day
    str_date_list: list[str] = date.split('-')

    for index in range(len(str_date_list)):
        date_list.append(int(str_date_list[index]))
    
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]


"""
def store_values_from_date_list_in_variables():
    global year, month, day
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]
"""


def get_anchor_day(given_year: int) -> int:
    century: int = int(str(given_year)[:2]) + 1
    year_of_century: int = int(str(given_year)[2:])
    temp: float = float(year_of_century)

    if not year_of_century % 2 == 0:
        temp = temp + 11
    
    temp = temp / 2

    if not temp % 2 == 0:
        temp = temp + 11
    
    difference_between_temp_and_higher_multiple_of_7: int = (7 - int(temp) % 7)
    century_anchors: list[int] = [2, 0, 5, 3]
    century_anchor: int = century_anchors[(century - 1) % 4]
    anchor_day: int = (difference_between_temp_and_higher_multiple_of_7 + century_anchor) % 7
    # WEEKDAYS: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # anchor_weekday: str = WEEKDAYS[anchor_day]
    # print(anchor_weekday)
    return anchor_day



date_to_test: str = "2023-03-25"
print(f"Weekday for {date_to_test} is", get_day_for_date(date_to_test))








"""
################################################################################
---------
QUESTIONS
---------

Noms des variables "temp" ok dans fonction get_anchor_day() ?

Fonction reset_global_variables() et parse_string_date_to_variables()
redondantes avec certaines dans date.py

Variables globales redondantes également entre les fichiers, possible de les partager ?


-----
TO DO
-----
Modifs en fonction des réponses aux questions ci-dessus

Clean commentaires en bas de fichier
"""