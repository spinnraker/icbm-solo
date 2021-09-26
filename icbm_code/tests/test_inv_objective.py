import unittest
from icbm_code.calculations.investment_objective import InvestmentObjective


class TestInvestmentObjective(unittest.TestCase):
    """Test for investment_objective.py"""

    def setUp(self) -> None:
        self.io = InvestmentObjective()

    # Unit tests to verify scores
    def test_set_io_first_question_a(self):
        """Test passing value 'a' and returning io score of 1"""
        self.io.calc_first_answer('a')
        self.assertIs(self.io.first_answer_score, 1)
        self.assertIsNot(self.io.first_answer_score, 2)

    def test_set_io_first_question_b(self):
        """Test passing value 'b' and returning io score of 2"""
        self.io.calc_first_answer('b')
        self.assertIs(self.io.first_answer_score, 2)
        self.assertIsNot(self.io.first_answer_score, 3)

    def test_set_io_first_question_c(self):
        """Test passing value 'c' and returning io score of 3"""
        self.io.calc_first_answer('c')
        self.assertIs(self.io.first_answer_score, 3)
        self.assertIsNot(self.io.first_answer_score, 4)

    def test_set_io_first_question_d(self):
        """Test passing value 'd' and returning io score of 4"""
        self.io.calc_first_answer('d')
        self.assertIs(self.io.first_answer_score, 4)
        self.assertIsNot(self.io.first_answer_score, 3)

    def test_io_set_second_question_a(self):
        """Test passing value 'a' and returning io score of 5"""
        self.io.calc_second_answer('a')
        self.assertIs(self.io.second_answer_score, 5)
        self.assertIsNot(self.io.second_answer_score, 3)

    def test_io_set_second_question_b(self):
        """Test passing value 'b' and returning io score of 3"""
        self.io.calc_second_answer('b')
        self.assertIs(self.io.second_answer_score, 3)
        self.assertIsNot(self.io.second_answer_score, 1)

    def test_io_second_question_c(self):
        """Test passing value 'c' and returning io score of 1"""
        self.io.calc_second_answer('c')
        self.assertIs(self.io.second_answer_score, 1)
        self.assertIsNot(self.io.second_answer_score, 3)

    # Unit tests to verify categories
    def test_io_set_objective_less_4(self):
        """Test for scores less than 4"""
        self.io.first_answer_score = 1
        self.io.second_answer_score = 2
        self.io.set_objective()
        self.assertEqual(self.io.objective, "Income")
        self.assertNotEqual(self.io.objective, "Balanced")

    def test_io_set_objective_4(self):
        """Test for scores equal to 4"""
        self.io.first_answer_score = 3
        self.io.second_answer_score = 1
        self.io.set_objective()
        self.assertEqual(self.io.objective, "Income")
        self.assertIsNot(self.io.objective, "Growth")

    def test_io_set_objective_5(self):
        """Test for scores equal to 5"""
        self.io.first_answer_score = 2
        self.io.second_answer_score = 3
        self.io.set_objective()
        self.assertEqual(self.io.objective, "Balanced")
        self.assertNotEqual(self.io.objective, "Income")

    def test_io_set_objective_6(self):
        """Test for scores equal to 6"""
        self.io.first_answer_score = 3
        self.io.second_answer_score = 3
        self.io.set_objective()
        self.assertEqual(self.io.objective, "Balanced")
        self.assertNotEqual(self.io.objective, "Growth")

    def test_io_set_objective_7(self):
        """Test for scores greater than 6"""
        self.io.first_answer_score = 2
        self.io.second_answer_score = 5
        self.io.set_objective()
        self.assertEqual(self.io.objective, "Growth")
        self.assertNotEqual(self.io.objective, "Balanced")

if __name__ == '__main__':
    unittest.main()
