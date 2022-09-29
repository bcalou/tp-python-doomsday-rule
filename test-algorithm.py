from doomsday.algorithm import get_day_for_date

# Mine ################################################
if get_day_for_date("2022-01-01") != "Saturday":
    print(get_day_for_date("2021-01-31") +
          '\033[91m❌ Date for 2021-01-31 should be Saturday\033[0;0m')


if get_day_for_date("2002-03-19") != "Tuesday":
    print(get_day_for_date("2002-03-19") +
          '\033[91m❌ Date for 2021-01-31 should be Tuesday\033[0;0m')

################################################################

if get_day_for_date("2021-01-31") != "Sunday":
    print(get_day_for_date("2021-01-31") +
          '\033[91m❌ Date for 2021-01-31 should be Sunday\033[0;0m')

elif get_day_for_date("2021-02-20") != "Saturday":
    print(get_day_for_date("2021-02-20") +
          '\033[91m❌ Date for 2021-02-20 should be Saturday\033[0;0m')

elif get_day_for_date("2021-03-10") != "Wednesday":
    print(get_day_for_date("2021-03-10") +
          '\033[91m❌ Date for 2021-03-10 should be Wednesday\033[0;0m')

elif get_day_for_date("2021-04-10") != "Saturday":
    print(get_day_for_date("2021-04-10") +
          '\033[91m❌ Date for 2021-04-10 should be Saturday\033[0;0m')

elif get_day_for_date("2021-05-10") != "Monday":
    print(get_day_for_date("2021-05-10") +
          '\033[91m❌ Date for 2021-05-10 should be Monday\033[0;0m')

elif get_day_for_date("2021-06-10") != "Thursday":
    print(get_day_for_date("2021-06-10") +
          '\033[91m❌ Date for 2021-06-10 should be Thursday\033[0;0m')

elif get_day_for_date("2021-07-10") != "Saturday":
    print(get_day_for_date("2021-07-10") +
          '\033[91m❌ Date for 2021-07-10 should be Saturday\033[0;0m')

elif get_day_for_date("2021-08-10") != "Tuesday":
    print(get_day_for_date("2021-08-10") +
          '\033[91m❌ Date for 2021-08-10 should be Tuesday\033[0;0m')

elif get_day_for_date("2021-09-10") != "Friday":
    print(get_day_for_date("2021-09-10") +
          '\033[91m❌ Date for 2021-09-10 should be Friday\033[0;0m')

elif get_day_for_date("2021-10-10") != "Sunday":
    print(get_day_for_date("2021-10-10") +
          '\033[91m❌ Date for 2021-10-10 should be Sunday\033[0;0m')

elif get_day_for_date("2021-11-10") != "Wednesday":
    print(get_day_for_date("2021-11-10") +
          '\033[91m❌ Date for 2021-11-10 should be Wednesday\033[0;0m')

elif get_day_for_date("2021-12-10") != "Friday":
    print(get_day_for_date("2021-12-10") +
          '\033[91m❌ Date for 2021-12-10 should be Friday\033[0;0m')

elif get_day_for_date("2000-01-10") != "Monday":
    print(get_day_for_date("2000-01-10") +
          '\033[91m❌ Date for 2000-01-10 should be Monday\033[0;0m')

elif get_day_for_date("1900-01-10") != "Wednesday":
    print(get_day_for_date("1900-01-10") +
          '\033[91m❌ Date for 1900-01-10 should be Wednesday\033[0;0m')

elif get_day_for_date("2000-02-29") != "Tuesday":
    print(get_day_for_date("2000-02-29") +
          '\033[91m❌ Date for 2000-02-29 should be Tuesday\033[0;0m')

elif get_day_for_date("1900-02-28") != "Wednesday":
    print(get_day_for_date("1900-02-28") +
          '\033[91m❌ Date for 1900-02-28 should be Wednesday\033[0;0m')

elif get_day_for_date("2159-01-10") != "Wednesday":
    print(get_day_for_date("2159-01-10") +
          '\033[91m❌ Date for 2159-01-10 should be Wednesday\033[0;0m')

elif get_day_for_date("2259-01-10") != "Monday":
    print(get_day_for_date("2259-01-10") +
          '\033[91m❌ Date for 2259-01-10 should be Monday\033[0;0m')

elif get_day_for_date("2359-01-10") != "Saturday":
    print(get_day_for_date("2359-01-10") +
          '\033[91m❌ Date for 2359-01-10 should be Saturday\033[0;0m')

else:
    print('\033[92m✓ OK\033[0;0m')
