"""
Constants
"""

DAYS_NAMES: tuple[str, ...] = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)

COMMON_YEAR_DAYS_PER_MONTH: tuple[int, ...] = (
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
)

# Month length are the same for a leap year, except for february
LEAP_YEAR_DAYS_PER_MONTH: tuple[int, ...] = (
    (COMMON_YEAR_DAYS_PER_MONTH[0], 29) + COMMON_YEAR_DAYS_PER_MONTH[2:]
)

CENTURY_ANCHORS: tuple[int, ...] = (2, 0, 5, 3)

COMMON_YEAR_DOOMSDAYS: tuple[int, ...] = (3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5)

# Doomsdays change for the first two month on leap years
LEAP_YEAR_DOOMSDAYS: tuple[int, ...] = (4, 1) + COMMON_YEAR_DOOMSDAYS[2:]
