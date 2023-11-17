from doomsday.date import is_valid_date

def main() -> None:
    
    stop = False

    while not stop :
        input_date = input("\n Enter a date and I'll get the day (quit to stop the programm) : ")
        print("\n")

    if input_date.lower() == "quit" :
        stop = True
    else :
        print(is_valid_date('2023-12-12'))
    
    print("bye bye")


main()
