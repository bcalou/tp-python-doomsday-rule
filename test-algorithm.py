from doomsday.algorithm import get_weekday_for_date

error: bool = False

if get_weekday_for_date("2021-01-31") != "Sunday":
    print('\033[91m❌ Date for 2021-01-31 should be Sunday')

if get_weekday_for_date("2021-02-20") != "Saturday":
    error = True
    print('\033[91m❌ Date for 2021-02-20 should be Saturday')

if get_weekday_for_date("2021-03-10") != "Wednesday":
    error = True
    print('\033[91m❌ Date for 2021-03-10 should be Wednesday')

if get_weekday_for_date("2021-04-10") != "Saturday":
    error = True
    print('\033[91m❌ Date for 2021-04-10 should be Saturday')

if get_weekday_for_date("2021-05-10") != "Monday":
    error = True
    print('\033[91m❌ Date for 2021-05-10 should be Monday')

if get_weekday_for_date("2021-06-10") != "Thursday":
    error = True
    print('\033[91m❌ Date for 2021-06-10 should be Thursday')

if get_weekday_for_date("2021-07-10") != "Saturday":
    error = True
    print('\033[91m❌ Date for 2021-07-10 should be Saturday')

if get_weekday_for_date("2021-08-10") != "Tuesday":
    error = True
    print('\033[91m❌ Date for 2021-08-10 should be Tuesday')

if get_weekday_for_date("2021-09-10") != "Friday":
    error = True
    print('\033[91m❌ Date for 2021-09-10 should be Friday')

if get_weekday_for_date("2021-10-10") != "Sunday":
    error = True
    print('\033[91m❌ Date for 2021-10-10 should be Sunday')

if get_weekday_for_date("2021-11-10") != "Wednesday":
    error = True
    print('\033[91m❌ Date for 2021-11-10 should be Wednesday')

if get_weekday_for_date("2021-12-10") != "Friday":
    error = True
    print('\033[91m❌ Date for 2021-12-10 should be Friday')

if get_weekday_for_date("2000-01-10") != "Monday":
    error = True
    print('\033[91m❌ Date for 2000-01-10 should be Monday')

if get_weekday_for_date("1900-01-10") != "Wednesday":
    error = True
    print('\033[91m❌ Date for 1900-01-10 should be Wednesday')

if get_weekday_for_date("2000-02-29") != "Tuesday":
    error = True
    print('\033[91m❌ Date for 2000-02-29 should be Tuesday')

if get_weekday_for_date("1900-02-28") != "Wednesday":
    error = True
    print('\033[91m❌ Date for 1900-02-28 should be Wednesday')

if get_weekday_for_date("2159-01-10") != "Wednesday":
    error = True
    print('\033[91m❌ Date for 2159-01-10 should be Wednesday')

if get_weekday_for_date("2259-01-10") != "Monday":
    error = True
    print('\033[91m❌ Date for 2259-01-10 should be Monday')

if get_weekday_for_date("2359-01-10") != "Saturday":
    error = True
    print('\033[91m❌ Date for 2359-01-10 should be Saturday')

if not error:
    print('\033[92m✓ OK')
