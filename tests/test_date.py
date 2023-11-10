import unittest

from doomsday.date import is_valid_date


class TestDate(unittest.TestCase):
    def test_valid_dates(self):
        valid_dates: list[str] = [
            '2021-10-10',
            '1996-02-29',
            '2000-02-29',
            '2148-01-31',
            '2148-1-2'
        ]

        for date in valid_dates:
            self.assertTrue(
                is_valid_date(date),
                f"{date} should be a valid date input"
            )

    def test_invalid_dates(self):
        invalid_dates: list[str] = [
            '2021-20-00',
            '2021-20-02',
            '1582-05-05',
            '1900-02-29',
            '2021-04-31',
            '01-01-2020',
            '01-01-',
            '-01-2020',
            '10-01-2020-02',
            '10-01'
        ]

        for date in invalid_dates:
            self.assertFalse(
                is_valid_date(date),
                f"{date} should be considered as an invalid date input"
            )
