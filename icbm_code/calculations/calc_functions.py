# Goal: create one class that imports and initiates all other classes

import time_horizon as th
import investment_objective as io


class CalcFunctions:
    """Imports all functions created"""

    def __init__(self, time_horizon, investment_objective, esg, risk_tolerance):
        self.time_horizon = time_horizon
        self.investment_objective = investment_objective
        self.esg = esg
        self.risk_tolerance = risk_tolerance

    # Initiate instances
    user_th = th.TimeHorizon()
    user_io = io.InvestmentObjective()

    # def final_calculations(self, time_horizon, investment_objective):
