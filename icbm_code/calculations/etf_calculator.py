# # Goal: Create function that determines which ETFs to show based on investment
# objective and ESG preference

import esg
import investment_objective as io

final_esg = esg.EnvironmentalSocialGovernance()
final_io = io.InvestmentObjective()


# options are ESG Value and Growth, ESG Value, Non-ESG Value and Growth,
# Non-ESG Value -

class ETFCalculator:
    """Determines which ETFs to pull from the Database"""

    def __init__(self, etf_table=""):
        self.etf_table = etf_table

    # WILL NEED TO UPDATE THIS ONCE WE FIGURE OUT HOW TO SHOW RESULTS FROM
    # TWO DIFFERENT TABLES - USING NON-ESG FOR LOW, ESG FOR MED AND HIGH
    def etf_calculator(self):
        """Displays ETFs based on ESG and Investment Objective"""
        esg_category = final_esg.esg_category
        objective = final_io.objective
        if esg_category == "Low" and objective == "Income":
            self.etf_table = "nonEsgValueDB"
        if esg_category == "Medium" and objective == "Balanced":
            self.etf_table == "nonEsgVa"


