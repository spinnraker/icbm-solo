import unittest
from time_horizon import TimeHorizon


class TestTimeHorizon(unittest.TestCase):
    """Test for class TimeHorizon."""
    def setUp(self):
        self.th = TimeHorizon()

    def test_set_time_a(self):
        # Test passing value 'a' and returning time score of 1
        self.th.set_time('a')
        self.assertIs(self.th.time_score, 1)
        self.assertIsNot(self.th.time_score, 3)
        self.assertEqual(self.th.horizon_category, "Ultra-Short Term")

    def test_set_time_b(self):
        # Test passing value 'b' and returning time score of 2
        self.th.set_time('b')
        self.assertIs(self.th.time_score, 2)
        self.assertIsNot(self.th.time_score, 3)
        self.assertEqual(self.th.horizon_category, "Short Term")

    def test_set_time_c(self):
        # Test passing value 'c' and returning time score of 3
        self.th.set_time('c')
        self.assertIs(self.th.time_score, 3)
        self.assertIsNot(self.th.time_score, 4)
        self.assertEqual(self.th.horizon_category, "Intermediate Term")

    def test_set_time_d(self):
        # Test passing value 'd' and returning time score of 4
        self.th.set_time('d')
        self.assertIs(self.th.time_score, 4)
        self.assertIsNot(self.th.time_score, 3)
        self.assertEqual(self.th.horizon_category, "Long Term")


if __name__ == '__main__':
    unittest.main()
