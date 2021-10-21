from doomsday.algorithm import get_day_for_date
from doomsday.date import is_valid_date

# This script get the user input, run the algorithm with user data and return the value 

while True: 
    input_date = input("Please, enter a date in format YYYY-MM-dd: \n")
    is_date_valid = is_valid_date(input_date)
    if is_date_valid:
        day_of_the_week = get_day_for_date(input_date)
        print("The day of the week for the date " + input_date + " is " + day_of_the_week)
        break

