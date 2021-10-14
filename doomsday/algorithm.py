
days = ["Sunday", "Monday", "Thuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
pivots_commun = [3, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
century_marker = [2, 0, 5, 3]

def get_century_marker(year : int) -> int:
    y: int = (year % 400) // 100
    return century_marker[y]

def get_day_for_date(date: str) -> str:
    return "Monday"
