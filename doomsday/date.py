error_code_wrong_format: int = (1)
error_code_not_number: int = (2)
error_code_date_not_exist: int = (3)
error_code_year_before_1583: int = (4)

max_month_last_day: int = (31)
min_month_last_day: int = (30)
special_month_last_day: int = (28)

year: int = (0)
month: int = (1)
day: int = (2)


def is_valid_date(date: str) -> bool:
    """is_valid_date test conditions for have a correct date  """

    date_list: list[str] = date.split('-')
    # Verify the format of the date 'YYYY-MM-DD'
    if (len(date_list) != 3):
        return List_of_possible_error(error_code_wrong_format, date)

    # Verify that each part of the date is int
    date_list_int: list[int] = []
    for element in date_list:
        if (not element.isnumeric()):
            return List_of_possible_error(
                error_code_not_number, date_list[0])
        date_list_int.append(int(element))

    # Verify that the date is possible Month(1-12) Day(1-lastday)

    if (date_list_int[month] < 1 or
       date_list_int[month] > 12):
        return List_of_possible_error(
            error_code_date_not_exist, date_list[month])

    if (date_list_int[day] < 1 or
       date_list_int[day] >
       Month_last_day(date_list_int[month], date_list_int[year])):
        return List_of_possible_error(
            error_code_date_not_exist, date_list[2])

    # Verify that the year of the date is after 1583
    if (date_list_int[year] < 1583):
        return List_of_possible_error(
            error_code_year_before_1583, date_list[0])

    return True


def List_of_possible_error(error_code: int, error_text: str) -> bool:
    """create an error message with a code and a text"""

    if (error_code == error_code_wrong_format):
        print('Erreur, ' +
              error_text +
              ' n est pas un bon format pour une date.' +
              ' Le format demandé est YYYY-MM-DD.')

    if (error_code == error_code_not_number):
        print('Erreur, ' +
              error_text +
              ' n est pas un nombre.')

    if (error_code == error_code_date_not_exist):
        print('Erreur, ' +
              error_text +
              ' le mois ou le jour sont incorrects.')

    if (error_code == error_code_year_before_1583):
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
        return max_month_last_day

    # Case 28-29
    if (month_number == 2):
        return leap_year(year)

    # Case 30
    return min_month_last_day


def leap_year(year: int) -> int:
    """return if year if leap or not"""

    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return 29
    return 28
