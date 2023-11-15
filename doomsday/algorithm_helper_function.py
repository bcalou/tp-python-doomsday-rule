def get_century_doomsday_offset(year: int) -> int:
    """Returns the doomsday offset for a given century"""

    # List of the offsets and exemples
    # 2000      2
    # 1700/2100 0
    # 1800/2200 5
    # 1900/2300 3
    CENTURY_OFFSETS: list[int] = [2, 0, 5, 3]

    century: int = year // 100

    return CENTURY_OFFSETS[century % 4]


def get_year_doomsday(year: int) -> int:
    """Return the doomsday for a given year"""

    century_offset: int = get_century_doomsday_offset(year)

    # The algorithm to find the doomsday for a year:
    # 1: Get the last two digits of the year
    last_2_digit: int = year % 100

    # 2: If the number is odd add 11
    if last_2_digit % 2 == 1:
        last_2_digit += 11

    # 3: Divide the number by 2
    last_2_digit = last_2_digit // 2

    # 4: If the number is odd add 11
    if last_2_digit % 2 == 1:
        last_2_digit += 11

    # 5: Find the difference with the next multiple of 7
    diff_with_next_multiple_of_seven: int = (7 - (last_2_digit % 7)) % 7

    # 6: Add the century offset and apply mod 7, you have the doomsday
    return (diff_with_next_multiple_of_seven + century_offset) % 7
