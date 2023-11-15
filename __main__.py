from doomsday.algorithm import get_weekday_for_date
from tests.test_algorithm import TestAlgorithm
from tests.test_date import TestDate


def main() -> None:
    dates = ["2000-01-01",
             "2001-01-29",
             "2017-12-15",
             "2023-11-15",
             "2111-12-12"]  # Saturday, Monday, Friday, Wednesday, Saturday
    for date in dates:
        print("{0} is a {1}.".format(date, get_weekday_for_date(date)))

    test_date = TestDate()
    test_date.test_valid_dates()
    test_date.test_invalid_dates()

    test_algorithm = TestAlgorithm()
    test_algorithm.test_algorithm()


main()
