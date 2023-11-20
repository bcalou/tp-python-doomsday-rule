def is_valid_date(date: str):
    try:
        if not date:
            raise ValueError("Empty date string")

        date = date.split("-", 3)
        if len(date) != 3:
            raise ValueError("Invalid date format")

        year = int(date[0]) if date[0] and int(date[0]) >= 1583 else None
        month = int(date[1]) if date[1] and 1 <= int(date[1]) <= 12 else None
        if year is None:
            raise ValueError("Invalid year")
        if month is None:
            raise ValueError("Invalid month")
        if date[2] and month in [1, 3, 5, 7, 8, 10, 12]:
            day = int(date[2]) if 1 <= int(date[2]) <= 31 else None
        elif date[2] and month in [4, 6, 9, 11]:
            day = int(date[2]) if 1 <= int(date[2]) <= 30 else None
        elif date[2] and month == 2:
            day = int(date[2]) if is_leap_year(year) and int(date[2]) > 0 and int(date[2]) < 30 or not is_leap_year(year) and int(date[2]) > 0 and int(date[2]) < 29 else None
        if day is None:
            raise ValueError("Invalid day")
        return True

    except ValueError as e:
        print(e)

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
