
days = ["Sunday", "Monday", "Thuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
pivots_commun = [3, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

# The century marker is an empirical value base on the hundred digit over a 4 century loop
def get_century_marker(year : int) -> int:
    y: int = (year % 400) // 100
    return [2, 0, 5, 3][y]

# "Odd + 11" methode 
def compute(year: int) -> int:
    y_last_digit: int = year % 100
    y_last_digit = y_last_digit if y_last_digit % 2 == 0 else y_last_digit + 11
    y_last_digit //= 2
    y_last_digit = y_last_digit if y_last_digit % 2 == 0 else y_last_digit + 11
    y_last_digit = 7 - (y_last_digit%7)
    return (y_last_digit + get_century_marker(year))% 7

# return the anchor day based on the year
def get_day_for_date(date: str) -> str:
    d, m, y = convert_date(myDate)
    v : int = compute(y)
    return days[v]

if __name__ == "__main__":
    from date import *
    myDate = "17-08-1965"
    print(get_day_for_date(myDate))
    
