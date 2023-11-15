def get_weekday_for_date(date: str) -> str:
    """get_weekday_for_date need the anchor date 
    and then find the day of the date"""

    list_date: list[str] = date.split('-')

    anchor_day_week: str = get_anchor_day(int(list_date[0]))

    anchor_day_in_date_month=find_anchor_day_in_date_month(int(list_date[1]))

    distance_in_day=get_anchor_day(int(list_date[2]),anchor_day_in_date_month):

    return get_day_in_week(anchor_day_week,distance_in_day)


def get_anchor_day(year: int) -> str :

    number_for_day: int = year % 100 
    number_for_day = add_eleven_if_is_odd(number_for_day) 
    number_for_day //= 2
    number_for_day = add_eleven_if_is_odd(number_for_day)
    number_for_day = get_difference_near_multiple_of_seven(number_for_day)
    number_for_day.add_century_step(year//100*100)
    number_for_day %= 7
    return change_into_str[number_for_day]


def add_eleven_if_is_odd(number: int) -> int :
    return number if number % 2 == 0 else number + 11


def get_difference_near_multiple_of_seven(number: int) -> int :
    return get_multiple_of_seven()

def add_century_step(century: int) -> int :
    return tab_change_for_century[(century/100)%4]