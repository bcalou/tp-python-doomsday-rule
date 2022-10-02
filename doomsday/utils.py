def init_global_variables():
    global date_list, year, month, day
    date_list = []
    year = 0
    month = 0
    day = 0


def parse_string_date_to_variables(date: str):
    """Parses the string given by the user and stores datas in variables."""

    str_date_list: list[str] = date.split('-')
    global date_list

    for index in range(len(str_date_list)):
        date_list.append(int(str_date_list[index]))
    
    global year, month, day
    year = date_list[0]
    month = date_list[1]
    day = date_list[2]