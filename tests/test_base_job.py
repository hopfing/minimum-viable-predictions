import unittest
from mvp.base_job import BaseJob


class TestBaseJob(unittest.TestCase):

    def test_invalid_league(self):
        with self.assertRaises(ValueError):
            BaseJob('baseball', '2025-06-01')

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            BaseJob('mlb', '06-01-2025')
