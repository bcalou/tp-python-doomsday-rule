DAYS = (
    "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"
)

MULTIPLE_OF_SEVEN = (
    #The maximum value that can be used is 35
    7, 14, 21, 28, 35
)

INDEX_FOR_CENTURY = (
    2, 0, 5, 3
)


def get_weekday_for_date(date: str) -> str:
    """Return the name of the day corresponding to the given date"""

    year, month, day = (int(value) for value in date.split("-"))
    anchor_day: int = get_anchor_day(str(year))


    return "pouet"


def get_anchor_day(year: str) -> int:
    """Return the anchor day for the given year"""

    #Get the last two numbers in the year
    anchor_day: int = int(year[-2:len(year)])
    century: int = int(year[0:-2])

    for i in range(2):
        if anchor_day % 2 != 0:
            anchor_day += 11
        anchor_day //= 2

    #Find the lowest multiple of seven greater than the value we have,
    # and keep the difference between this multiple and our value
    for multiple in MULTIPLE_OF_SEVEN:
        if multiple - 7 < anchor_day < multiple:
            anchor_day = multiple - anchor_day

    anchor_day += INDEX_FOR_CENTURY[century % 4]

    return anchor_day
