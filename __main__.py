import doomsday.date as date
import doomsday.algorithm as algorithm


def main() -> None:
    """main function ask a date, if the date is incorrect ask again,
    when the date is correct,
    main function ask for the day of the date and return it to the user"""

    print("Veuillez entrer une date" +
          "si vous voulez connaitre son jour dans la semaine.")
    input_date: str = input()
    while (not date.is_valid_date(input_date)):
        input_date = input()
    #algorithm.get_weekday_for_date(input_date)


main()
