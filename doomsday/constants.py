DAYS_NAMES: list[str] = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

DAYS_PER_MONTH: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

CENTURY_ANCHORS: list[int] = [2, 0, 5, 3]

COMMON_YEAR_DOOMSDAYS: list[int] = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]

# Doomsdays change for the first to month on leap years
LEAP_YEAR_DOOMSDAYS: list[int] = [4, 1] + COMMON_YEAR_DOOMSDAYS[2:]
