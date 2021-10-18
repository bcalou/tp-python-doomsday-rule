def transform_string_in_date(date_input: str)->list[int]:
    """Returb date as array format """
    if str(date_input).count('-') != 2:
        return [] 
    #Split the date for each number separated by "-"
    date_format: list[int] = date_input.split("-")
    year: int = int(date_format[0])
    month: int = int(date_format[1])
    day: int = int(date_format[2])
    
    return [day, month, year]