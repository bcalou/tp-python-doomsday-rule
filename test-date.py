from doomsday.date import is_valid_date

if not is_valid_date('2021-10-10'):
    print('\033[91m❌ 2021-10-10 should be valid')

elif not is_valid_date('1996-02-29'):
    print('\033[91m❌ 1996-02-29 should be valid')

elif not is_valid_date('2000-02-29'):
    print('\033[91m❌ 2000-02-29 should be valid')

elif not is_valid_date('2148-01-31'):
    print('\033[91m❌ 2148-01-31 should be valid')

elif is_valid_date('2021-20-00'):
    print('\033[91m❌ 2021-20-00 should not be valid')

elif is_valid_date('2021-20-02'):
    print('\033[91m❌ 2021-20-02 should not be valid')

elif is_valid_date('1582-05-05'):
    print('\033[91m❌ 1582-05-05 should not be valid')

elif is_valid_date('1900-02-29'):
    print('\033[91m❌ 1900-02-29 should not be valid')

elif is_valid_date('2021-04-31'):
    print('\033[91m❌ 2021-04-31 should not be valid')

elif is_valid_date(2021043):
    print('\033[91m❌ 2021043 should not be valid')

elif is_valid_date([2020, 4, 30]):
    print('\033[91m❌ [2020, 4, 30] should not be valid')

elif is_valid_date('01-01-2020'):
    print('\033[91m❌ 01-01-2020 should not be valid')

elif is_valid_date('1582-02-21'):
    print('\033[91m❌ 1582-02-21 should not be valid')

else:
    print('\033[92m✓ OK')