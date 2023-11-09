DAYS_NAMES = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)

# Number of days per month for a common year
DAYS_PER_MONTH_COMMON_YEAR = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# Month length are the same for a leap year, except for february
DAYS_PER_MONTH_LEAP_YEAR = (
    (DAYS_PER_MONTH_COMMON_YEAR[0], 29) + DAYS_PER_MONTH_COMMON_YEAR[2:]
)

# A loop of 4 numbers starting from the 17th century
CENTURY_ANCHOR_WEEKDAYS = (2, 0, 5, 3)

# List of doomsday for each month of a common year
DOOMSDAYS_COMMON_YEAR = (3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5)

# Doomsdays change for the first two months on leap years
DOOMSDAYS_LEAP_YEAR = (4, 1) + DOOMSDAYS_COMMON_YEAR[2:]
