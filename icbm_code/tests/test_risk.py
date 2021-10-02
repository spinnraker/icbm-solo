import unittest
from icbm_code.calculations.risk_profile import RiskProfile


class TestRisk(unittest.TestCase):
    """Test for risk_profile.py"""

    def setUp(self) -> None:
        self.risk = RiskProfile()
    # Unit tests to verify scores
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

    def test_risk_second_q_a(self):
        """Test passing value 'a' and returning risk score of 2"""
        self.risk.calc_second_answer('a')
        self.assertIs(self.risk.second_answer_score, 2)

    def test_risk_second_q_b(self):
        """Test passing value 'b' and returning risk score of 3"""
        self.risk.calc_second_answer('b')
        self.assertIs(self.risk.second_answer_score, 3)

    def test_risk_second_q_c(self):
        """Test passing value 'c' and returning risk score of 4"""
        self.risk.calc_second_answer('c')
        self.assertIs(self.risk.second_answer_score, 4)

    def test_risk_second_q_d(self):
        """Test passing value 'd' and returning risk score of 5"""
        self.risk.calc_second_answer('d')
        self.assertIs(self.risk.second_answer_score, 5)

    def test_risk_third_q_a(self):
        """Test passing value 'a' and returning risk score of 1"""
        self.risk.calc_third_answer('a')
        self.assertIs(self.risk.third_answer_score, 1)

    def test_risk_third_q_b(self):
        """Test passing value 'c' and returning risk score of 3"""
        self.risk.calc_third_answer('b')
        self.assertIs(self.risk.third_answer_score, 3)

    def test_risk_third_q_c(self):
        """Test passing value 'c' and returning risk score of 5"""
        self.risk.calc_third_answer('c')
        self.assertIs(self.risk.third_answer_score, 5)

    def test_risk_fourth_q_a(self):
        """Test passing value 'a' and returning risk score of 1"""
        self.risk.calc_fourth_answer('a')
        self.assertIs(self.risk.fourth_answer_score, 1)

    def test_risk_fourth_q_b(self):
        """Test passing value 'b' and returning risk score of 3"""
        self.risk.calc_fourth_answer('b')
        self.assertIs(self.risk.fourth_answer_score, 3)

    def test_risk_fourth_q_c(self):
        """Test passing value 'c' and returning risk score of 5"""
        self.risk.calc_fourth_answer('c')
        self.assertIs(self.risk.fourth_answer_score, 5)

    # Unit tests to verify categories
    def test_set_risk_less_8(self):
        """Test for scores less than 8"""
        self.risk.first_answer_score = 1
        self.risk.second_answer_score = 2
        self.risk.third_answer_score = 1
        self.risk.fourth_answer_score = 1
        self.risk.set_risk_score()
        self.assertEqual(self.risk.risk_category, "Conservative")
        self.assertNotEqual(self.risk.risk_category, "Moderate")
        self.assertNotEqual(self.risk.risk_category, "Aggressive")

    def test_set_risk_8(self):
        """Test for scores equal to 8"""
        self.risk.first_answer_score = 1
        self.risk.second_answer_score = 1
        self.risk.third_answer_score = 3
        self.risk.fourth_answer_score = 3
        self.risk.set_risk_score()
        self.assertEqual(self.risk.risk_category, "Conservative")
        self.assertNotEqual(self.risk.risk_category, "Moderate")
        self.assertNotEqual(self.risk.risk_category, "Aggressive")

    def test_set_risk_9(self):
        """Test for scores equal to 9"""
        self.risk.first_answer_score = 1
        self.risk.second_answer_score = 2
        self.risk.third_answer_score = 3
        self.risk.fourth_answer_score = 3
        self.risk.set_risk_score()
        self.assertEqual(self.risk.risk_category, "Moderate")
        self.assertNotEqual(self.risk.risk_category, "Conservative")
        self.assertNotEqual(self.risk.risk_category, "Aggressive")

    def test_set_risk_less_15(self):
        """Test for scores less than 15"""
        self.risk.first_answer_score = 2
        self.risk.second_answer_score = 2
        self.risk.third_answer_score = 5
        self.risk.fourth_answer_score = 5
        self.risk.set_risk_score()
        self.assertEqual(self.risk.risk_category, "Moderate")
        self.assertNotEqual(self.risk.risk_category, "Conservative")
        self.assertNotEqual(self.risk.risk_category, "Aggressive")

    def test_set_risk_15(self):
        """Test for scores equal to 15"""
        self.risk.first_answer_score = 4
        self.risk.second_answer_score = 4
        self.risk.third_answer_score = 4
        self.risk.fourth_answer_score = 3
        self.risk.set_risk_score()
        self.assertEqual(self.risk.risk_category, "Moderate")
        self.assertNotEqual(self.risk.risk_category, "Conservative")
        self.assertNotEqual(self.risk.risk_category, "Aggressive")

    def test_set_risk_16(self):
        """Test for scores greater than 15"""
        self.risk.first_answer_score = 5
        self.risk.second_answer_score = 5
        self.risk.third_answer_score = 3
        self.risk.fourth_answer_score = 6
        self.risk.set_risk_score()
        self.assertEqual(self.risk.risk_category, "Aggressive")
        self.assertNotEqual(self.risk.risk_category, "Conservative")
        self.assertNotEqual(self.risk.risk_category, "Moderate")

if __name__ == '__main__':
    unittest.main()
