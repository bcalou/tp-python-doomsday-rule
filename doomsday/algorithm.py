from doomsday.date import is_leap_year

WEEKDAYS: list[str] = (
    ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
)

global date_list; date_list: list[int] = []
global year; year: int = 0
global month; month: int = 0
global day; day: int = 0

def get_day_for_date(date: str) -> str:
    reset_global_variables()
    parse_string_date_to_variables(date)
    anchor_day_index: int =(get_anchor_day_index(year))

    months_doomsdays: list[int] = [0, 999, 999, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    if is_leap_year(year):
        months_doomsdays[1] = 11
        months_doomsdays[2] = 22
    else:
        months_doomsdays[1] = 10
        months_doomsdays[2] = 21
    
    gap_between_day_to_test_and_month_doomsday: int = (
        (day - months_doomsdays[month]) % 7
    )

    return WEEKDAYS[(anchor_day_index + gap_between_day_to_test_and_month_doomsday) % 7]


def reset_global_variables():
    global date_list
    global year, month, day
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


def get_anchor_day_index(given_year: int) -> int:
    CENTURY_ANCHORS: list[int] = [2, 0, 5, 3]
    century_digits: int = int(str(given_year)[:2])
    year_of_century: int = int(str(given_year)[2:])
    temp: float = float(year_of_century)

    if not year_of_century % 2 == 0:
        temp = temp + 11
    
    temp = temp / 2

    if not temp % 2 == 0:
        temp = temp + 11
    
    difference_between_temp_and_higher_multiple_of_7: int = (7 - int(temp) % 7)
    century_anchor: int = CENTURY_ANCHORS[(century_digits) % 4]
    anchor_day_index: int = (
        (difference_between_temp_and_higher_multiple_of_7 + century_anchor) % 7
    )
    return anchor_day_index


"""
date_to_test: str = "2022-09-26"
print(f"Weekday for {date_to_test} is", get_day_for_date(date_to_test))
"""







"""
################################################################################
---------
QUESTIONS
---------

Noms des variables "temp" ok dans fonction get_anchor_day_index() ?

Fonction reset_global_variables() et parse_string_date_to_variables()
redondantes avec certaines dans date.py

Variables globales redondantes également entre les fichiers, possible de les partager ?

Import en début de fichier : from doomsday.date import is_leap_year
besoin de préciser doomsdday.date si fonction appelée depuis le fichier doomsday.py,
mais ne fonctionne pas quand fonction appelée depuis ce fichier, besoin de
from date import is_leap_year


-----
TO DO
-----
Commenter tout

Modifs en fonction des réponses aux questions ci-dessus

Clean commentaires en bas de fichier
"""