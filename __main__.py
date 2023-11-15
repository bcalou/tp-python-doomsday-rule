import datetime

def input_date() -> None:
    """Asks for a date and check if its valid"""
    time_str = str(input("Enter date in this format yyyy-mm-dd \n >>"))
    try:
        # year = time_str[0:4]
        # month = time_str[5:7]
        # day = time_str[8:10]
        date = time_str.split("-", 3)
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        if (year > 999 and 1 <= month <= 12 and 1 <= day <= 31):
            print("Valid date")
        else: 
            raise Exception("Invalid date")
    except Exception as e:
        print(e)

input_date()