def is_valid_date(date: str) -> bool:
    try:
        year, month, day = map(int, date.split('-'))

        if year < 1583:
            return False

        if 1 <= month <= 12 and 1 <= day <= 31:
            if month in [4, 6, 9, 11] and day > 30:
                return False
            elif month == 2:  # February
                if day > 29:
                    return False
                elif day == 29 and not (year % 4 == 0 and
                                        (year % 100 != 0 or year % 400 == 0)):
                    return False  # February 29 is only valid in leap years

            return True
    except ValueError:
        pass

    return False
