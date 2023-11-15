import doomsday.date as date
import doomsday.algorithm as algorithm


def main() -> None:
    date_string: str = input("Date (format YYYY-MM-DD): ")

    if (not date.is_valid_date(date_string)):
        return

    weekday_at_given_date: str = algorithm.get_weekday_for_date(date_string)
    print(f"The date {date_string} is a {weekday_at_given_date}.")


main()
