ERROR_CODE_WRONG_FORMAT = (1)
ERROR_CODE_NOT_NUMBER = (2)
ERROR_CODE_DATE_NOT_EXIST = (3)
ERROR_CODE_YEAR_BEFORE_1583 = (4)

MAX_MONTH_LAST_DAY = (31)
MIN_MONTH_LAST_DAY = (30)
SPECIAL_MONTH_LAST_DAY = (28)
SPECIAL_MONTH_LAST_LEAD_DAY = (29)

YEAR = (0)
MONTH = (1)
DAY = (2)


def is_valid_date(date: str) -> bool:
    """is_valid_date test conditions for have a correct date  """

    date_list: list[str] = date.split('-')
    # Verify the format of the date 'YYYY-MM-DD'
    if (len(date_list) != 3):
        return List_of_possible_error(ERROR_CODE_WRONG_FORMAT, date)

    # Verify that each part of the date is int
    date_list_int: list[int] = []
    for element in date_list:
        if (not element.isnumeric()):
            return List_of_possible_error(
                ERROR_CODE_NOT_NUMBER, date_list[0])
        date_list_int.append(int(element))

    # Verify that the date is possible Month(1-12) Day(1-lastday)
    if (date_list_int[MONTH] < 1 or
       date_list_int[MONTH] > 12):
        return List_of_possible_error(
            ERROR_CODE_DATE_NOT_EXIST, date_list[MONTH])

    if (date_list_int[DAY] < 1 or
       date_list_int[DAY] >
       Month_last_day(date_list_int[MONTH], date_list_int[YEAR])):
        return List_of_possible_error(
            ERROR_CODE_DATE_NOT_EXIST, date_list[2])

    # Verify that the year of the date is after 1583
    if (date_list_int[YEAR] < 1583):
        return List_of_possible_error(
            ERROR_CODE_YEAR_BEFORE_1583, date_list[0])

    return True


def List_of_possible_error(error_code: int, error_text: str) -> bool:
    """create an error message with a code and a text"""

    if (error_code == ERROR_CODE_WRONG_FORMAT):
        print('Erreur, ' +
              error_text +
              ' n est pas un bon format pour une date.' +
              ' Le format demandé est YYYY-MM-DD.')

    if (error_code == ERROR_CODE_NOT_NUMBER):
        print('Erreur, ' +
              error_text +
              ' n est pas un nombre.')

    if (error_code == ERROR_CODE_DATE_NOT_EXIST):
        print('Erreur, ' +
              error_text +
              ' le mois ou le jour sont incorrects.')

    if (error_code == ERROR_CODE_YEAR_BEFORE_1583):
        print('Erreur, ' +
              error_text +
              ' l année ne doit pas etre en dessous de 1583.')

    return False


def Month_last_day(month_number: int, year: int) -> int:
    """Month_last_day take number of the month
    and return the last day of month"""

    # Case 31
    if ((month_number % 2 == 1 and month_number <= 7) or
       (month_number % 2 == 0 and month_number >= 8)):
        return MAX_MONTH_LAST_DAY

    # Case 28-29
    if (month_number == 2):
        if (get_leap(year)):
            return SPECIAL_MONTH_LAST_LEAD_DAY
        return SPECIAL_MONTH_LAST_DAY

    # Case 30
    return MIN_MONTH_LAST_DAY


def get_leap(year: int) -> bool:
    """change the variable if the year is leap"""
    if year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0):
        return True
    return False
