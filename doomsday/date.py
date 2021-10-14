# Check if a given date follows the format YYYY-MM-dd and is valid
# Parameter: a string formated date
def is_valid_date(date: str) -> bool:
    # A formatted date must contain 10 characters
    if len(str(date)) != 10:
        print(color.FAIL + f"\"{date}\" is not valid: it does not contains exactly 10 characters." + color.RESET)
        return False
    date_members = str(date).split("-")

    # Once splitted, date must contain 3 members
    if len(date_members) != 3:
        print(color.FAIL + f"\"{date}\" is not valid: it misses one or more members separated with \"-\"." + color.RESET)
        return False
    
    # Each member must be a number
    for date_member in date_members:
        if not date_member.isnumeric():
            print(color.FAIL + f"\"{date}\" is not valid: {date_member} is not a member." + color.RESET)
            return False
    
    # Check validity for each member ence the day, the month and the year
    year = int(date_members[0])
    month = int(date_members[1])
    day = int(date_members[2])
    if year <= 1583:
        print(color.FAIL + f"\"{date}\" is not valid: year {year} is not past 1583." + color.RESET)
        return False
    if month not in range(1, 13):
        print(color.FAIL + f"\"{date}\" is not valid: month {month} is not between 1 and 12." + color.RESET)
        return False
    if not is_day_valid(day, month, year):
        print(color.FAIL + f"\"{date}\" is not valid: day {day} is not valid for the {month}/{year}." + color.RESET)
        return False
    return True

# Check if the given year in format YYYY is a leap year
# Parameter: the year as an integer
def is_leap_year(year: int) -> bool:
    if(year % 400 != 0):
        return year % 4 == 0 if year % 100 != 0 else False
    return True

# Check if the given day is valid for the given month and year
# Parameters: the day, month and year as integers
def is_day_valid(day: int, month: int, year: int) -> bool:
    # Check if month is february to consider the leap year
    if month == 2:
        if is_leap_year(year):
            if day not in range(1, 30):
                return False
        else:
            if day not in range(1, 29):
                return False
    # Check if month is a 31 days or a 30 days month
    if month in [4, 6, 9, 11]:
        if day not in range(1, 31):
            return False
    else:
        if day not in range(1, 32):
            return False
    # If no error was found, the day is valid
    return True

# A number to label corresponding list for each day and month
day_labels = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
month_labels = ["January", "February", "March", "April", "June", "July", "August", "September", "October", "December"]

# Some color codes for the terminal
class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'