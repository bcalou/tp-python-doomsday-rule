from enum import Enum, unique, auto


@unique
class Error(Enum):
    WRONG_FORMAT = auto()
    NOT_NUMBER = auto()
    DATE_NOT_EXIST = auto()
    YEAR_BEFORE_1583 = auto()


@unique
class Last_day(Enum):
    SPECIAL_MONTH = 28
    SPECIAL_MONTH_LEAP = 29
    MAX_MONTH = 31
    MIN_MONTH = 30


@unique
class Date_part(Enum):
    YEAR = 0
    MONTH = 1
    DAY = 2


def is_valid_date(date: str) -> bool:
    """is_valid_date test conditions for have a correct date  """

    date_list: list[str] = date.split('-')
    # Verify the format of the date 'YYYY-MM-DD'
    if (len(date_list) != 3):
        return show_error(Error.WRONG_FORMAT, date)

    # Verify that each part of the date is int
    date_list_int: list[int] = []
    for element in date_list:
        if (not element.isnumeric()):
            return show_error(
                Error.NOT_NUMBER, date_list[0])
        date_list_int.append(int(element))

    # Verify that the date is possible Month(1-12) Day(1-lastday)
    if (date_list_int[Date_part.MONTH.value] < 1 or
       date_list_int[Date_part.MONTH.value] > 12):
        return show_error(
            Error.DATE_NOT_EXIST, date_list[Date_part.MONTH.value])

    if (date_list_int[Date_part.DAY.value] < 1 or
       date_list_int[Date_part.DAY.value] >
       find_month_last_day(date_list_int[Date_part.MONTH.value],
                           date_list_int[Date_part.YEAR.value])):
        return show_error(
            Error.DATE_NOT_EXIST, date_list[Date_part.DAY.value])

    # Verify that the year of the date is after 1583
    if (date_list_int[Date_part.YEAR.value] < 1583):
        return show_error(
            Error.YEAR_BEFORE_1583, date_list[Date_part.YEAR.value])

    return True


def show_error(error_code: Error, error_text: str) -> bool:
    """create an error message with a code and a text"""

    if (error_code == Error.WRONG_FORMAT):
        print('Erreur, ' +
              error_text +
              ' n est pas un bon format pour une date.' +
              ' Le format demandé est YYYY-MM-DD.')

    if (error_code == Error.NOT_NUMBER):
        print('Erreur, ' +
              error_text +
              ' n est pas un nombre.')

    if (error_code == Error.DATE_NOT_EXIST):
        print('Erreur, ' +
              error_text +
              ' le mois ou le jour sont incorrects.')

    if (error_code == Error.YEAR_BEFORE_1583):
        print('Erreur, ' +
              error_text +
              ' l année ne doit pas etre en dessous de 1583.')

    return False


def find_month_last_day(month_number: int, year: int) -> int:
    """month_last_day take number of the month
    and return the last day of month"""

    # Case 31
    if ((month_number % 2 == 1 and month_number <= 7) or
       (month_number % 2 == 0 and month_number >= 8)):
        return Last_day.MAX_MONTH.value

    # Case 28-29
    if (month_number == 2):
        if (is_leap(year)):
            return Last_day.SPECIAL_MONTH_LEAP.value
        return Last_day.SPECIAL_MONTH.value

    # Case 30
    return Last_day.MIN_MONTH.value


def is_leap(year: int) -> bool:
    """return if the year is leap"""
    if year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0):
        return True
    return False
