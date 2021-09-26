import unittest
from icbm_code.calculations.esg import EnvironmentalSocialGovernance


class TestESG(unittest.TestCase):
    """Test for esg.py"""

    def setUp(self) -> None:
        self.esg = EnvironmentalSocialGovernance()

    def test_esg_first_q_a(self):
        """Test passing value 'a' and returning esg score of 1"""
        self.esg.calc_first_answer("a")
        self.assertIs(self.esg.first_answer_score, 1)
        self.assertIsNot(self.esg.first_answer_score, 5)

    def test_esg_first_q_b(self):
        """Test passing value 'b' and returning esg score of 2"""
        self.esg.calc_first_answer('b')
        self.assertIs(self.esg.first_answer_score, 2)
        self.assertIsNot(self.esg.first_answer_score, 3)

    def test_esg_first_q_c(self):
        """Test passing value 'c' and returning esg score of 3"""
        self.esg.calc_first_answer('c')
        self.assertIs(self.esg.first_answer_score, 3)
        self.assertIsNot(self.esg.first_answer_score, 4)

    def test_esg_first_q_d(self):
        """Test passing value 'd' and returning esg score of 4"""
        self.esg.calc_first_answer('d')
        self.assertIs(self.esg.first_answer_score, 4)
        self.assertIsNot(self.esg.first_answer_score, 5)

    def test_esg_first_q_e(self):
        """Test passing value 'e' and returning esg score of 5"""
        self.esg.calc_first_answer('e')
        self.assertIs(self.esg.first_answer_score, 5)
        self.assertIsNot(self.esg.first_answer_score, 4)


if __name__ == '__main__':
    unittest.main()
