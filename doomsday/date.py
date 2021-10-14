from typing import Match


def is_valid_date(date) -> bool:
    date = str(date)
    if len(date) == 10:
        year = date[0] + date[1] + date[2] + date[3]
        month = date[5] + date[6]
        day = date[8] + date[9]
        if (year + month + day).isnumeric():
            year, month, day = int(year), int(month), int(day)
            if (date[4] + date[7] == "--"):
                if year >= 1583:
                    if 0 < month <= 12:
                        if 0 < day:
                            if day <= day_count_in_month(month, year):
                                return True
                            else:
                                print("Day too high")
                        else:
                            print("Day must be positive")
                    else:
                        print("Month must be between 1 and 12")
                else:
                    print("Year must be earlier than 1583")
            else:
                print("Separators must be hymens '-'")
        else:
            print("YYYY, MM & dd must be numerics")
    else:
        print("YYYY-MM-dd format must contain 10 characters")

    return False


def is_leap_year(year: int) -> bool:
    if(year % 400 != 0):
        return year % 4 == 0 if year % 100 != 0 else False
    return True


def day_count_in_month(month: int, year: int) -> int:
    month_31_list = [1, 3, 5, 7, 8, 10, 12]
    for month_31 in month_31_list:
        if month == month_31:
            return 31

    month_30_list = [4, 6, 9, 11]
    for month_30 in month_30_list:
        if month == month_30:
            return 30

    return 29 if is_leap_year(year) else 28
