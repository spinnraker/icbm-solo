import unittest
from icbm_code.calculations.risk_profile import RiskProfile


class TestRisk(unittest.TestCase):
    """Test for risk_profile.py"""

    def setUp(self) -> None:
        self.risk = RiskProfile()

    def test_risk_first_q_a(self):
        """Test passing value 'a' and returning risk score of 1"""
        self.risk.calc_first_answer('a')
        self.assertIs(self.risk.first_answer_score, 1)

    def test_risk_first_q_b(self):
        """Test passing value 'b' and returning risk score of 2"""
        self.risk.calc_first_answer('b')
        self.assertIs(self.risk.first_answer_score, 2)

    def test_risk_first_q_c(self):
        """Test passing value 'c' and returning risk score of 3"""
        self.risk.calc_first_answer('c')
        self.assertIs(self.risk.first_answer_score, 3)

    def test_risk_first_q_d(self):
        """Test passing value 'd' and returning risk score of 4"""
        self.risk.calc_first_answer('d')
        self.assertIs(self.risk.first_answer_score, 4)

    def test_risk_first_q_e(self):
        """Tests passing value 'e' and returning risk score of 5"""
        self.risk.calc_first_answer('e')
        self.assertIs(self.risk.first_answer_score, 5)


if __name__ == '__main__':
    unittest.main()
