import unittest
from time_horizon import TimeHorizon


class TestTimeHorizon(unittest.TestCase):
    """Test for class TimeHorizon."""
    def setUp(self):
        self.th = TimeHorizon()

    def test_set_time(self):
        # Test passing a value and returning time score
        self.th.set_time('b')
        self.assertIs(self.th.time_score, 2)
        self.assertIsNot(self.th.time_score, 3)

if __name__ == '__main__':
    unittest.main()
