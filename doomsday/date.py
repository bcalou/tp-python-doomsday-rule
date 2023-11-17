import doomsday.date_toolbox as tool
import doomsday.errors as EEEE
import doomsday.const as const

def is_valid_date(date: str) -> bool:
    '''
        Check if date = fine (don't ask questions).
    '''
    if is_valid_format(date) :
        split_date: list[int] = tool.parse_date_to_ints(date)

        if (is_valid_year(split_date[0]) and
        is_valid_month(split_date[1]) and
        is_valid_day(split_date)) :
            return True


    return False


def is_valid_day(date: list[int]) -> bool:
    '''
        day = gud ?
    '''
    year: int = date[0]
    month: int = date[1]
    day: int = date[2]

    is_valid = False

    if day > 0 :

        if month == 2 :
            is_valid = is_valid_day_case_february(year, day)

        elif month in const.PHALANX_MONTH() :
            if day < 32 :

                is_valid = True

        else :
            if day < 31 :

                is_valid = True

    if not is_valid :
        EEEE.wrong_day(day, month, tool.is_leap_year(year))

    return is_valid


def is_valid_day_case_february(year: int, day: int) :
    '''
        Subshit from is_valid_day() checking for february.
    '''
    if tool.is_leap_year(year) :
        if day < 30 :

            return True
                
    else :
        if day < 29 :
                     
            return True
    
    return False


def is_valid_month(month: int) -> bool:
    '''
        is month valid
    '''
    if month < 1 or month > 12 :
        EEEE.wrong_month(month)

        return False

    return True


def is_valid_year(year: int) -> bool:
    '''
        Does the year fulfill is role correctly in our requirements ?
    '''

    if  year < 1583 :
        EEEE.wrong_year(year)

        return False

    return True


def is_valid_format(date: str) -> bool:
    '''
        Says if the date format is valid.
    '''

    split_date = tool.split_date(date)

    if len(split_date) == 3 :

        return check_year_month_day(split_date)
        
    else :
        EEEE.wrong_format()

        return False
    

def check_year_month_day(split_date: list[str]) -> bool :
    '''
        Subshit from is_valid_format() helping to tell date format validity for
        each date part.
    '''
    if (len(split_date[0]) == 0 or                            
        len(split_date[1]) < 1 and len(split_date[1]) > 2 or 
        len(split_date[2]) < 1 and len(split_date[2]) > 2 ):
            
            EEEE.wrong_format()

            return False
    
    for element in split_date :
        if (not element.isnumeric()) :
            EEEE.not_numeric_value(element)

            return False

    return True