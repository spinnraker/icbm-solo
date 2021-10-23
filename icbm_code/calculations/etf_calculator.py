# # Goal: Create function that determines which ETFs to show based on investment
# objective and ESG preference

import esg
import investment_objective as io

final_esg = esg.EnvironmentalSocialGovernance()
final_io = io.InvestmentObjective()


# options are ESG Value, ESG Balanced, ESG Growth, Traditional Value
# traditional Growth, traditional Balanced -

class ETFCalculator:
    """Determines which ETFs to pull from the Database"""

    def __init__(self, etf_type="", etf_style=""):
        self.etf_type = etf_type
        self.etf_style = etf_style

    # WILL NEED TO UPDATE THIS ONCE WE FIGURE OUT HOW TO SHOW RESULTS FROM
    # TWO DIFFERENT TABLES - USING NON-ESG FOR LOW, ESG FOR MED AND HIGH
    def set_etf_list(self):
        """Displays ETFs based on ESG and Investment Objective"""
        esg_category = final_esg.esg_category
        objective = final_io.objective
        if esg_category == "Low" and objective == "Income":
            self.etf_style = "Non-ESG"
            self.etf_type = "Value"
        elif esg_category == "Low" and objective == "Balanced":
            # self.etf_table = "traditionalBalancedDB"
            self.etf_style = "Non-ESG"
            self.etf_type = "Balanced"
        elif esg_category == "Low" and objective == "Growth":
            self.etf_style = "Non-ESG"
            self.etf_type = "Growth"
            #This portion needs to be updated once we figure out how to show both
        elif esg_category == "Medium" and objective == "Income":
            self.etf_style = "ESG"
            self.etf_type = "Value"
        elif esg_category == "Medium" and objective == "Balanced":
            self.etf_style = "ESG"
            self.etf_type = "Balanced"
        elif esg_category == "Medium" and objective == "Growth":
            self.etf_style = "ESG"
            self.etf_type = "Growth"
        elif esg_category == "High" and objective == "Income":
            self.etf_style = "ESG"
            self.etf_type = "Value"
        elif esg_category == "High" and objective == "Balanced":
            self.etf_style = "Balanced"
            self.etf_type = "Growth"
        elif esg_category == "High" and objective == "Growth":
            self.etf_style = "ESG"
            self.etf_type = "Growth"

    def get_type_style(self):
        return self.etf_type, self.etf_style


# This works
final_io.calc_first_answer('a')
final_io.calc_second_answer('c')
final_esg.calc_second_answer('e')
final_esg.calc_first_answer('e')
final_esg.calc_fourth_answer('e')
final_esg.calc_third_answer('e')

final_esg.set_esg_cat()
final_io.set_objective()

my_result = ETFCalculator()
my_result.set_etf_list()

answer = my_result.get_type_style()
print(answer)