import unittest

from doomsday.algorithm import get_weekday_for_date


class TestAlgorithm(unittest.TestCase):
    def test_algorithm(self):
        dates: dict[str, str] = {
            '2021-02-20': 'Saturday',
            '2021-03-10': 'Wednesday',
            '2021-04-10': 'Saturday',
            '2021-05-10': 'Monday',
            '2021-06-10': 'Thursday',
            '2021-07-10': 'Saturday',
            '2021-08-10': 'Tuesday',
            '2021-09-10': 'Friday',
            '2021-10-10': 'Sunday',
            '2021-11-10': 'Wednesday',
            '2021-12-10': 'Friday',
            '2000-01-10': 'Monday',
            '1900-01-10': 'Wednesday',
            '2000-02-29': 'Tuesday',
            '1900-02-28': 'Wednesday',
            '2159-01-10': 'Wednesday',
            '2259-01-10': 'Monday',
            '2359-01-10': 'Saturday'
        }

        for [date, weekday] in dates.items():
            guessed_weekday: str = get_weekday_for_date(date)
            self.assertEqual(
                guessed_weekday,
                weekday,
                f'{date} is {weekday}, wrong value returned: {guessed_weekday}'
            )
