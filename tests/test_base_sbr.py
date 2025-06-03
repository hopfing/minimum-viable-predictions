import unittest

from mvp.config import League
from mvp.sportsbookreview.base_sbr import SBRBase, SBRLeague, SBRPeriod


class TestSBRBase(unittest.TestCase):

    def test_invalid_sbr_league(self):
        with self.assertRaises(ValueError):
            SBRBase('football', '2025-06-01')

    def test_valid_sbr_league(self):
        try:
            SBRBase('wnba', '2025-06-01')
        except ValueError:
            self.fail(
                'SBRBase raised ValueError unexpectedly for valid league'
            )

    def test_empty_url_path(self):
        with self.assertRaises(ValueError):
            SBRLeague(
                name=League.MLB, url_path='', periods=[SBRPeriod.FULL_GAME]
            )

    def test_invalid_period_value_raises(self):
        with self.assertRaises(ValueError):
            SBRLeague(
                name=League.MLB,
                url_path='mlb-baseball',
                periods=['5th-period']
            )
