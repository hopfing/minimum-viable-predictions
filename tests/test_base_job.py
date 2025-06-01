import unittest
from mvp.base_job import BaseJob


class TestBaseJob(unittest.TestCase):

    def test_invalid_league(self):
        with self.assertRaises(TypeError):
            BaseJob('invalid_league', '2025-06-01')
