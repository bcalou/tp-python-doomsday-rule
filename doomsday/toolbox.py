def is_leap_year(year: int) -> bool:
    '''
        Check if the year is a leap year.
    '''
    if year % 100 == 0:
        if year % 400 == 0:

            return True
        
    elif year % 4 == 0:

        return True
    
    return False


def parse_date_to_ints(date: str) -> list[int] :
    '''
        Get a list of each individual parts of the date.
    '''
    return date_elements_to_ints(split_date(date))


def date_elements_to_ints(split_date: list[str]) -> list[int] :
    '''
        Return the int side of the force. You'd ask me why did I made two 
        different functions to get the same result. 
        AHAHAHAAAAAHHH, behold my tremendous genius (and -1 on my score) !!!
    '''

    split_date_int: list[int] = []

    for date_part in split_date :
        split_date_int.append(int(date_part))
    
    return split_date_int


def split_date(date: str) -> list[str]:
    '''
        Give an array containing each elements of the date.
        -> if not a date, return an array containing only the string
    '''

    if "-" in date :
        return date.split("-")
                          
    elif "." in date :
        return date.split(".")
                          
    elif "/" in date :
        return date.split("/")
    
    elif "_" in date :
        return date.split("_")
    
    return date.split()