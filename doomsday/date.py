import re

month_max_lenght = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def is_leap_year(y : int) -> bool :
    if y%4 == 0 and y%100 != 0:
        return True
    elif  y%400 == 0:
        return True
    return False

# check if date is at format -> YYYY-MM-dd
def is_valid_date(date: str) -> bool:
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date)
    if m == None:
        return False
    # TODO ne gére pas le nombre de jour en fonction du mois
    if int(m.group(1)) < 1583 or int(m.group(2)) > 12 or int(m.group(3)) > 31:
        return False
    if int(m.group(3)) > month_max_lenght[int(m.group(2))]:
        if m.group(2) == "02":
            pass
    return True