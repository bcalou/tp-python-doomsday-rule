def get_weekday_for_date(date_str):
    WEEKDAYS = (
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    )

    from datetime import datetime
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        lastTwoNumbersCentury = date_obj.year % 100

        if lastTwoNumbersCentury % 2 != 0:
            lastTwoNumbersCentury += 11

        lastTwoNumbersCentury //= 2

        if lastTwoNumbersCentury % 2 != 0:
            lastTwoNumbersCentury += 11

        i = 0
        while i < 8:
            if (lastTwoNumbersCentury + i) % 7 == 0:
                closest_multiple_of_seven = lastTwoNumbersCentury + i
                break

        numbers_by_century = [2, 0, 5, 3]

        number_to_add_century = numbers_by_century[(date_obj.year // 100) % 4]

        anchor_day = WEEKDAYS[closest_multiple_of_seven + number_to_add_century]

        print(anchor_day)


    except ValueError:
        # If the conversion fails, print an error message
        print("Incorrect date format. Please use the format YYYY-MM-dd.")
        return None


get_weekday_for_date('2021-10-10')
