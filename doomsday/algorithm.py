def get_anchor_day(year: int) -> int:

    # Extract the century
    century = year // 100 * 100

    # Century offset
    anchor = ((century // 100) % 4) * 5

    # Add the offset based on the century
    anchor = (anchor + 2) % 7

    return anchor


def get_doomsday(year):

    # Extract the last two digits of the year
    year_digits = year % 100

    # Divide by 12 and take the remainder
    quotient = year_digits // 12
    remainder = year_digits - 12*quotient

    # Apply the doomsday formula
    doomsday = (remainder // 4)

    doomsday = (quotient+remainder+doomsday+get_anchor_day(year)) % 7
    
    return doomsday

def get_weekday_for_date(date: str):

    year, month, day = map(int, date.split("-"))

    anchor_day = get_anchor_day(year)

    # Get Doomsday
    doomsday = get_doomsday(year)

    # Calculate day_of_week_index
    day_of_week_index = (day - doomsday + anchor_day) % 7

    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Get the corresponding day in the array
    return days_of_week[day_of_week_index]
