from doomsday.date import is_valid_date


def get_weekday_for_date(date: str) -> str:
    if not is_valid_date(date):
        return "Invalid date"

    year, month, day = map(int, date.split('-'))
    day_of_week = calculate_doomsday(year, month, day)

    week_days = ["Sunday", "Monday",
                 "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday"]
    return week_days[day_of_week]


def get_year_anchor(year: int) -> int:
    # Define the anchor day for the century
    anchor_day = 2

    # Calculate the century anchor day
    century = year // 100
    century_anchor = (5 * (century % 4) + anchor_day) % 7

    # Calculate the year anchor day
    year_within_century = year % 100
    year_anchor = (century_anchor + (year_within_century // 12)
                   + (year_within_century % 12)
                   + ((year_within_century % 12) // 4)
                   ) % 7

    return year_anchor


def calculate_doomsday(year: int, month: int, day: int) -> int:
    year_anchor = get_year_anchor(year)

    # Define the Doomsday for each month
    doomsday_month = [3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

    # Adjustments for January and February in leap years
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        doomsday_month[0] = 4
        doomsday_month[1] = 1

    # Calculate the day of the week for the given date
    day_of_week = (day - doomsday_month[month - 1] + year_anchor) % 7

    return day_of_week
