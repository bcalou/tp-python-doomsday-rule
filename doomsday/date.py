global str_date_list; str_date_list: list[str] = []
global int_date_list; int_date_list: list[int] = []
global year; year: int = 0
global month; month: int = 0
global day; day: int = 0


def is_valid_date(date: str) -> bool:
    """Checking if entered string format is correct and if the date exists"""
    reset_global_variables()

    if not is_string_format_correct(date):
        return False
    else:
        parse_string_date_to_variables()
        #store_values_from_date_list_in_variables()
    
    if not does_year_exists(year):
        return False
    
    if not does_month_exists(month):
        return False
    
    if not does_day_exists(day):
        return False
    
    #reset_global_variables()
    return True



def is_string_format_correct(input: str) -> bool:
    dash_quantity_in_input_string: int = 0

    for character in input:
        if character == "-":
            dash_quantity_in_input_string += 1
    
    if dash_quantity_in_input_string != 2:
        print("Please input a correct date format (YYYY-MM-dd) with dashes")
        return False
    
    global str_date_list
    str_date_list = input.split('-')
    local_year: str = str_date_list[0]
    local_month: str = str_date_list[1]
    local_day: str = str_date_list[2]

    if not local_year.isdecimal():
        print("Please enter a correct year")
        return False
    
    if not local_month.isdecimal():
        print("Please enter a correct month")
        return False
    
    if not local_day.isdecimal():
        print("Please input a correct day")
        return False
    
    return True



def parse_string_date_to_variables():
    global int_date_list
    global year, month, day

    for index in range(len(str_date_list)):
        int_date_list.append(int(str_date_list[index]))
        
    year = int_date_list[0]
    month = int_date_list[1]
    day = int_date_list[2]



"""
def store_values_from_date_list_in_variables():
    global year, month, day
    year = int_date_list[0]
    month = int_date_list[1]
    day = int_date_list[2]
"""



def does_year_exists(given_year: int) -> bool:
    if given_year >= 1583:
        return True
    else:
        print("Please enter a year after 1583")
        return False



def does_month_exists(given_month: int) -> bool:
    if 0 < given_month <= 12:
        return True
    else:
        print("This month doesn't exist")
        return False



def does_day_exists(given_day: int) -> bool:
    MONTHS_WITH_30_DAYS: list[int] = [4, 6, 9, 11]
    MONTHS_WITH_31_DAYS: list[int] = [1, 3, 5, 7, 8, 10, 12]
    
    if (
        (month in MONTHS_WITH_30_DAYS) and (not 0 < given_day <= 30) or
        (month in MONTHS_WITH_31_DAYS) and (not 0 < given_day <= 31)
    ):
        print("This day doesn't exist in this month")
        return False
    
    if (
        month == 2 and
        ((is_leap_year(year) and not 0 < given_day <= 29) or
        (not is_leap_year(year) and not 0 < given_day <= 28))
    ):
        print("This day doesn't exist in this month (please check if year is leap)")
        return False
    
    return True



def is_leap_year(given_year: int) -> bool:
    """Check is year is leap or not.
    See https://www.mathsisfun.com/leap-years.html for calculation rules.
    """
    return (given_year % 4 == 0 and not given_year % 100 == 0) or (given_year % 400 == 0)



def reset_global_variables():
    global str_date_list, int_date_list
    global year, month, day
    str_date_list = []
    int_date_list = []
    year = 0
    month = 0
    day = 0





"""
date_to_test: str = "2021-10-10"
print(f"Is {date_to_test} a valid date ?", is_valid_date(date_to_test))
"""



"""
################################################################################
---------
QUESTIONS
---------

Noms des variables ok avec préfixe local_ dans is_string_format_correct() ?

Convention respectée pour les if avec des retours à la ligne ?

2 lignes vides entre chaque def de fonction ? Actuellement 3


-----
TO DO
-----
Modifs en fonction des réponses aux questions ci-dessus

Clean commentaires en bas de fichier
"""