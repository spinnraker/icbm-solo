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

    def test_esg_first_q_b(self):
        """Test passing value 'b' and returning esg score of 2"""
        self.esg.calc_first_answer('b')
        self.assertIs(self.esg.first_answer_score, 2)

    def test_esg_first_q_c(self):
        """Test passing value 'c' and returning esg score of 3"""
        self.esg.calc_first_answer('c')
        self.assertIs(self.esg.first_answer_score, 3)

    def test_esg_first_q_d(self):
        """Test passing value 'd' and returning esg score of 4"""
        self.esg.calc_first_answer('d')
        self.assertIs(self.esg.first_answer_score, 4)

    def test_esg_first_q_e(self):
        """Test passing value 'e' and returning esg score of 5"""
        self.esg.calc_first_answer('e')
        self.assertIs(self.esg.first_answer_score, 5)

    def test_esg_second_q_a(self):
        """Test passing value 'a' an returning esg score of 1"""
        self.esg.calc_second_answer('a')
        self.assertIs(self.esg.second_answer_score, 1)

    def test_esg_second_q_b(self):
        """Test passing value 'b' and returning esg score of 2"""
        self.esg.calc_second_answer('b')
        self.assertIs(self.esg.second_answer_score, 2)

    def test_esg_second_q_c(self):
        """Test passing value 'c' and returning esg score of 3"""
        self.esg.calc_second_answer('c')
        self.assertIs(self.esg.second_answer_score, 3)

    def test_esg_second_q_d(self):
        """Test passing value 'd' and returning esg score of 4"""
        self.esg.calc_second_answer('d')
        self.assertIs(self.esg.second_answer_score, 4)

    def test_esg_second_q_e(self):
        """Test passing value 'e' and returning esg score of 5"""
        self.esg.calc_second_answer('e')
        self.assertIs(self.esg.second_answer_score, 5)

    def test_esg_third_q_a(self):
        """Test passing value 'a' and returning esg score of 1"""
        self.esg.calc_third_answer('a')
        self.assertIs(self.esg.third_answer_score, 1)

    def test_esg_third_q_b(self):
        """Test passing value 'b' and returning esg score of 2"""
        self.esg.calc_third_answer('b')
        self.assertIs(self.esg.third_answer_score, 2)

    def test_esg_third_q_c(self):
        """Test passing value 'c' and returning esg score of 3"""
        self.esg.calc_third_answer('c')
        self.assertIs(self.esg.third_answer_score, 3)

    def test_esg_third_q_d(self):
        """Test passing value 'd' and returning esg score of 4"""
        self.esg.calc_third_answer('d')
        self.assertIs(self.esg.third_answer_score, 4)

    def test_esg_third_q_e(self):
        """Passing value 'e' and returning esg score of 5"""
        self.esg.calc_third_answer('e')
        self.assertIs(self.esg.third_answer_score, 5)

    def test_esg_fourth_q_a(self):
        """Test passing a value 'a' and returning esg score of 1"""
        self.esg.calc_fourth_answer('a')
        self.assertIs(self.esg.fourth_answer_score, 1)

    def test_esg_fourth_q_b(self):
        """Test passing value 'b' and returning esg score of 2"""
        self.esg.calc_fourth_answer('b')
        self.assertIs(self.esg.fourth_answer_score, 2)

    def test_esg_fourth_q_c(self):
        """Test passing value 'c' and returning esg score of 3"""
        self.esg.calc_fourth_answer('c')
        self.assertIs(self.esg.fourth_answer_score, 3)

    def test_esg_fourth_q_d(self):
        """Test passing value 'd' and returning esg score of 4"""
        self.esg.calc_fourth_answer('d')
        self.assertIs(self.esg.fourth_answer_score, 4)

    def test_esg_fourth_q_e(self):
        """Test passing value 'e' and returning esg score of 5"""
        self.esg.calc_fourth_answer('e')
        self.assertIs(self.esg.fourth_answer_score, 5)

    def test_esg_set_cat_less_8(self):
        """Test for scores less than 8"""
        self.esg.first_answer_score = 1
        self.esg.second_answer_score = 1
        self.esg.third_answer_score = 1
        self.esg.fourth_answer_score = 4
        self.esg.set_esg_cat()
        self.assertIs(self.esg.esg_score, 7)
        self.assertEqual(self.esg.esg_category, "Low")
        self.assertNotEqual(self.esg.esg_category, "Medium")
        self.assertNotEqual(self.esg.esg_category, "High")

    def test_esg_set_cat_8(self):
        """Test for scores equal to 8"""
        self.esg.first_answer_score = 1
        self.esg.second_answer_score = 1
        self.esg.third_answer_score = 1
        self.esg.fourth_answer_score = 5
        self.esg.set_esg_cat()
        self.assertIs(self.esg.esg_score, 8)
        self.assertEqual(self.esg.esg_category, "Low")
        self.assertNotEqual(self.esg.esg_category, "Medium")
        self.assertNotEqual(self.esg.esg_category, "High")

    def test_esg_set_cat_9(self):
        """Test for scores equal to 9"""
        self.esg.first_answer_score = 2
        self.esg.second_answer_score = 2
        self.esg.third_answer_score = 2
        self.esg.fourth_answer_score = 3
        self.esg.set_esg_cat()
        self.assertIs(self.esg.esg_score, 9)
        self.assertEqual(self.esg.esg_category, "Medium")
        self.assertNotEqual(self.esg.esg_category, "Low")
        self.assertNotEqual(self.esg.esg_category, "High")

    def test_esg_set_cat_less_15(self):
        """Test for scores less than or equal to 15"""
        self.esg.first_answer_score = 3
        self.esg.second_answer_score = 4
        self.esg.third_answer_score = 4
        self.esg.fourth_answer_score = 4
        self.esg.set_esg_cat()
        self.assertIs(self.esg.esg_score, 15)
        self.assertEqual(self.esg.esg_category, "Medium")
        self.assertNotEqual(self.esg.esg_category, "Low")
        self.assertNotEqual(self.esg.esg_category, "High")

    def test_esg_set_cat_more_15(self):
        """Test for scores greater than 15"""
        self.esg.first_answer_score = 4
        self.esg.second_answer_score = 4
        self.esg.third_answer_score = 4
        self.esg.fourth_answer_score = 4
        self.esg.set_esg_cat()
        self.assertIs(self.esg.esg_score, 16)
        self.assertEqual(self.esg.esg_category, "High")
        self.assertNotEqual(self.esg.esg_category, "Low")
        self.assertNotEqual(self.esg.esg_category, "Medium")


if __name__ == '__main__':
    unittest.main()
