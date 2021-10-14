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
    m = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", str(date))
    if m == None:
        return False
    if int(m.group("year")) < 1583 or int(m.group("month")) > 12 or int(m.group("day")) > 31:
        return False
    if int(m.group("day")) > month_max_lenght[int(m.group("month")) - 1]:
        if m.group("month") == "02" and is_leap_year(int(m.group("year"))):
            return m.group(3) == "29"
        return False
    return True