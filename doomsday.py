from doomsday.date import is_valid_date


date_input: str = input("Enter a date in format YYYY-MM-dd:\n")
print("Date Valide") if is_valid_date(date_input) else print("Date Invalide")

