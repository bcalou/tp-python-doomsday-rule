def is_valid_date(date: str) -> bool:
    dash_quantity: int = 0

    for character in date:
        if character == "-":
            dash_quantity += 1
    
    if dash_quantity != 2:
        print("Please format date with dashes")
        return False
    
    date_list: list[str] = date.split('-')
    year: str = date_list[0]
    month: str = date_list[1]
    day: str = date_list[2]

    if not year.isdecimal():
        print("Please input a correct year")
        return False
    
    if (not month.isdecimal()) or (not 0 < int(month) <= 12):
        print("Please input a correct month")
        return False
    
    months_with_30_days: list[int] = [4, 6, 9, 11]
    months_with_31_days: list[int] = [1, 3, 5, 7, 8, 10, 12]

    return False


is_valid_date("1952-1-25")