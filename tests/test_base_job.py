import unittest
from mvp.base_job import BaseJob


class TestBaseJob(unittest.TestCase):

    def test_invalid_league(self):
        with self.assertRaises(ValueError):
            BaseJob('baseball', '2025-06-01')

    def test_valid_league(self):
        try:
            BaseJob('mlb', '2025-06-01')
        except ValueError:
            self.fail(
                'BaseJob raised ValueError unexpectedly for valid league'
            )

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            BaseJob('mlb', '06-01-2025')

    def test_period_normalization(self):
        test_job = BaseJob('mlb', '2025-06-01')
        self.assertEqual(
            test_job.normalize_period('1st-half'), 'first_half'
        )
        self.assertEqual(
            test_job.normalize_period('2nd-quarter'), 'second_quarter'
        )
