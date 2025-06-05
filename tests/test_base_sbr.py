import unittest

from mvp.sportsbookreview import SBRBase
from mvp.sportsbookreview.sbr_config import SBRLeague, SBRPeriod


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
                url_path='', periods=[SBRPeriod.FULL_GAME]
            )

    def test_invalid_period_value_raises(self):
        with self.assertRaises(ValueError):
            SBRLeague(
                url_path='mlb-baseball',
                periods=['5th-period']
            )
