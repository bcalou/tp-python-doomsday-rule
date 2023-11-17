from doomsday.date import is_valid_date
from doomsday.algorithm import get_weekday_for_date

def main() -> None:
    
    stop = False

    while not stop :
        input_date = input("\n Enter a date and I'll get the day (quit to stop the programm) : ")
        print("\n")

        if input_date.lower() == "quit" :
            stop = True
        else :
            if is_valid_date(input_date):
                print("You asked for " + get_weekday_for_date(input_date))
    
    print("bye bye")


main()
