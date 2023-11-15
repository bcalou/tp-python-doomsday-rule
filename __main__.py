from doomsday.date import is_valid_date


def main():
    while True:
        user_input = input("Please enter a date using the format YYYY-MM-dd : ")

        # Check date input
        if not is_valid_date(user_input):
            print("Incorrect date format. Please use this format : YYYY-MM-dd.")
            continue

        print("Date valide : ", user_input)
        break


if __name__ == "__main__":
    main()
