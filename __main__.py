import doomsday.date as date
import doomsday.algorithm as algorithm


def main() -> None:
    """main function ask a date, if the date is incorrect ask again,
    when the date is correct,
    main function ask for the day of the date and return it to the user"""

    while True:
        input_date: str = input(
            "Please enter a date if you want to know it day on week")
        if (date.is_valid_date(input_date)):
            break
    print(input_date + " is a " + algorithm.get_weekday_for_date(input_date))


main()
