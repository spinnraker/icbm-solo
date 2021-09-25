import time_horizon as th
import investment_objective as io

# Program asks users a series of questions to determine which
# securities to suggests (educational purpose ONLY)

# Initialize time horizon object
user_score_th = th.TimeHorizon()  # Initialize time horizon instance

# Determine time horizon
question_1 = "How long are you planning on investing your money?"
question_1 += "\na. Less than 3 years \nb. 3-5 years\nc. 6-10 years\n" \
              "d. More than 11 years\nEnter your answer: "

answer_1 = input(question_1)
user_score_th.set_time(answer_1)

# Determine Investment Objective
user_score_io = io.InvestmentObjective()  # Initialize investment objective
# instance

# Determine time horizon
question_2 = "\nWhen it comes to investing, I am more interested in capital " \
             "growth than maintaining the principal value."
question_2 += "\na. Strongly Disagree \nb. Somewhat disagree \nc. Neutral" \
              "\nd. Somewhat agree \ne.	Strongly agree\nEnter your answer: "

answer_2 = input(question_2)

question_3 = "\nIf investing in a stock, would you rather:"
question_3 += "\na.	Buy Companies that may make significant technological " \
              "advances that are still selling at their low initial offering " \
              "price. \nb.	Established, well-known companies that have a " \
              "potential for continued growth \nc.'Blue chip' stocks that " \
              "pay dividends \nEnter your answer: "

answer_3 = input(question_3)
user_score_io.set_objective(answer_2, answer_3)

print(user_score_th.get_time())
print(user_score_io.get_objective())
