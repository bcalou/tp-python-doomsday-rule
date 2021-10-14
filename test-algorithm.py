from doomsday.algorithm import *

if get_day_for_date("2021-01-31") != "Sunday":
    print('\033[91m❌ Date for 2021-01-31 should be Sunday')

elif get_day_for_date("2021-02-20") != "Saturday":
    print('\033[91m❌ Date for 2021-02-20 should be Saturday')

elif get_day_for_date("2021-03-10") != "Wednesday":
    print('\033[91m❌ Date for 2021-03-10 should be Wednesday')

elif get_day_for_date("2021-04-10") != "Saturday":
    print('\033[91m❌ Date for 2021-04-10 should be Saturday')

elif get_day_for_date("2021-05-10") != "Monday":
    print('\033[91m❌ Date for 2021-05-10 should be Monday')

elif get_day_for_date("2021-06-10") != "Thursday":
    print('\033[91m❌ Date for 2021-06-10 should be Thursday')

elif get_day_for_date("2021-07-10") != "Saturday":
    print('\033[91m❌ Date for 2021-07-10 should be Saturday')

elif get_day_for_date("2021-08-10") != "Tuesday":
    print('\033[91m❌ Date for 2021-08-10 should be Tuesday')

elif get_day_for_date("2021-09-10") != "Friday":
    print('\033[91m❌ Date for 2021-09-10 should be Friday')

elif get_day_for_date("2021-10-10") != "Sunday":
    print('\033[91m❌ Date for 2021-10-10 should be Sunday')

elif get_day_for_date("2021-11-10") != "Wednesday":
    print('\033[91m❌ Date for 2021-11-10 should be Wednesday')

elif get_day_for_date("2021-12-10") != "Friday":
    print('\033[91m❌ Date for 2021-12-10 should be Friday')

elif get_day_for_date("2000-01-10") != "Monday":
    print('\033[91m❌ Date for 2000-01-10 should be Monday')

elif get_day_for_date("1900-01-10") != "Wednesday":
    print('\033[91m❌ Date for 1900-01-10 should be Wednesday')

elif get_day_for_date("2000-02-29") != "Tuesday":
    print('\033[91m❌ Date for 2000-02-29 should be Tuesday')

elif get_day_for_date("1900-02-28") != "Wednesday":
    print('\033[91m❌ Date for 1900-02-28 should be Wednesday')

elif get_day_for_date("2159-01-10") != "Wednesday":
    print('\033[91m❌ Date for 2159-01-10 should be Wednesday')

elif get_day_for_date("2259-01-10") != "Monday":
    print('\033[91m❌ Date for 2259-01-10 should be Monday')

elif get_day_for_date("2359-01-10") != "Saturday":
    print('\033[91m❌ Date for 2359-01-10 should be Saturday')

else:
    print('\033[92m✓ OK')
