from doomsday.const import PHALANX_MONTH
########################### Date validity ######################################

def wrong_format() :
    print("******* Error Format *******")
    print("Date Format not valid. Follow this case : YYYY-mm-dd")
    print("****************************")


def not_numeric_value(value: str) :
    print("******* Error Format *******")
    print("One of your value is not numerical :")
    print(f"--> {value} <--")
    print("Try again with only numerical values.")
    print("****************************")


def wrong_month(value: int) :
    print("******* Error Value *******")
    print(f"You entered {value} as month.")
    print("The month must be between 01 and 12.")
    print("***************************")


def wrong_year(value: int) :
    print("******* Error Value *******")
    print(f"You entered {value} as year.")
    print("The year must be past 1583.")
    print("***************************")


def wrong_day(day: int, month: int, is_leap: bool) :
    print("******* Error Value *******")
    print(f"For month number {month}, you entered {day} as day.")
    
    if month == 2 :
        wrong_day_case_february(day, month, is_leap)

    elif month in PHALANX_MONTH() :
        print("In your case, the day must be between 01 and 31")

    else :
        print("In your case, the day must be between 01 and 30")
    print("***************************")


def wrong_day_case_february(day: int, month: int, is_leap: bool) :
        
    if is_leap :
        print ("Your year is leap")
        print("The day must be between 01 and 29.")
    else :
        print("Your year is not leap")
        print("The day must be between 01 and 28.")

################################################################################