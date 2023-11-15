def input_date() -> None:
    """Asks for a date and check if its valid"""
    time_str = str(input("Enter date in this format yyyy-mm-dd \n >>"))
    try:
        # year = time_str[0:4]
        # month = time_str[5:7]
        # day = time_str[8:10]
        date = time_str.split("-", 3)
        year = int(date[0]) if int(date[0]) >= 1583 else None
        month = int(date[1]) if 1 <= int(date[1]) <= 12 else None
        day = int(date[2]) if 1 <= int(date[2]) <= 31 else None
        if year is None:
            raise ValueError("Invalid year")
        if month is None:
            raise ValueError("Invalid month")
        if day is None:
            raise ValueError("Invalid day")
        print("Valid date")
    except ValueError as e:
        print(e)

input_date()