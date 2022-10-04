from doomsday.date import is_valid_date

error: bool = False

if not is_valid_date('2021-10-10'):
    error = True
    print('\033[91m❌ 2021-10-10 should be valid')

if not is_valid_date('1996-02-29'):
    error = True
    print('\033[91m❌ 1996-02-29 should be valid')

if not is_valid_date('2000-02-29'):
    error = True
    print('\033[91m❌ 2000-02-29 should be valid')

if not is_valid_date('2148-01-31'):
    error = True
    print('\033[91m❌ 2148-01-31 should be valid')

if not is_valid_date('2148-1-2'):
    error = True
    print('\033[91m❌ 2148-1-2 should be valid')

if is_valid_date('2021-20-00'):
    error = True
    print('\033[91m❌ 2021-20-00 should not be valid')

if is_valid_date('2021-20-02'):
    error = True
    print('\033[91m❌ 2021-20-02 should not be valid')

if is_valid_date('1582-05-05'):
    error = True
    print('\033[91m❌ 1582-05-05 should not be valid')

if is_valid_date('1900-02-29'):
    error = True
    print('\033[91m❌ 1900-02-29 should not be valid')

if is_valid_date('2021-04-31'):
    error = True
    print('\033[91m❌ 2021-04-31 should not be valid')

if is_valid_date('01-01-2020'):
    error = True
    print('\033[91m❌ 01-01-2020 should not be valid')

if is_valid_date('01-01-'):
    error = True
    print('\033[91m❌ 01-01- should not be valid')

if is_valid_date('-01-2020'):
    error = True
    print('\033[91m❌ -01-2020 should not be valid')

if is_valid_date('10-01-2020-02'):
    error = True
    print('\033[91m❌ 10-01-2020-02 should not be valid')

if is_valid_date('10-01'):
    error = True
    print('\033[91m❌ 10-01 should not be valid')

if not error:
    print('\033[92m✓ OK')
