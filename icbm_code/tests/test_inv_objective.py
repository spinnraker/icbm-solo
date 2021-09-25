import unittest
from icbm_code.calculations.investment_objective import InvestmentObjective


class MyTestCase(unittest.TestCase):
    """Test for Investment Objective class"""

    def setUp(self) -> None:
        self.io = InvestmentObjective()

    def test_set_io_first_question_a(self):
        # Test passing value 'a' and returning io score of 1
        self.io.calc_first_answer('a')
        self.assertIs(self.io.first_answer_score, 1)
        self.assertIsNot(self.io.first_answer_score, 2)


    # def test_set_time_a(self):
    #     # Test passing value 'a' and returning time score of 1
    #     self.th.set_time('a')
    #     self.assertIs(self.th.time_score, 1)
    #     self.assertIsNot(self.th.time_score, 3)
    #     self.assertEqual(self.th.horizon_category, "Ultra-Short Term")
    #     self.assertNotEqual(self.th.horizon_category, "Long Term")


if __name__ == '__main__':
    unittest.main()
