import unittest
from icbm_code.calculations.time_horizon import TimeHorizon


class TestTimeHorizon(unittest.TestCase):
    """Tests for time_horizon.py"""

    def setUp(self):
        self.th = TimeHorizon()

    def test_set_time_a(self):
        """Test passing value 'a' and returning a th score of 1"""
        self.th.set_time('a')
        self.assertIs(self.th.time_score, 1)
        self.assertEqual(self.th.horizon_category, "Short Term")
        self.assertNotEqual(self.th.horizon_category, "Long Term")
        self.assertNotEqual(self.th.horizon_category, "Intermediate Term")

    def test_set_time_b(self):
        """Test passing value 'b' and returning a th score of 2"""
        self.th.set_time('b')
        self.assertIs(self.th.time_score, 2)
        self.assertEqual(self.th.horizon_category, "Intermediate Term")
        self.assertNotEqual(self.th.horizon_category, "Short Term")
        self.assertNotEqual(self.th.horizon_category, "Long Term")

    def test_set_time_c(self):
        """Test passing value 'c' and returning a th score of 3"""
        self.th.set_time('c')
        self.assertIs(self.th.time_score, 3)
        self.assertEqual(self.th.horizon_category, "Long Term")
        self.assertNotEqual(self.th.horizon_category, "Intermediate Term")
        self.assertNotEqual(self.th.horizon_category, "Short Term")


if __name__ == '__main__':
    unittest.main()