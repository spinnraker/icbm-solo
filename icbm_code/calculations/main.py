import time_horizon as th
import investment_objective as io
import esg

# Program asks users a series of questions to determine which
# securities to suggests (educational purpose ONLY)

# Initialize time horizon object instance
user_score_th = th.TimeHorizon()

# Determine time horizon
question_1 = "Question 1:"
question_1 += "\nHow long are you planning on investing your money?"
question_1 += "\na. Less than 3 years \nb. 3-5 years\nc. 6-10 years\n" \
              "d. More than 11 years\nEnter your answer: "

answer_1 = input(question_1)
user_score_th.set_time(answer_1)

# Determine Investment Objective
user_score_io = io.InvestmentObjective()  # Initialize investment objective
# instance

question_2 = "\nQuestion 2:"
question_2 += "\nWhen it comes to investing, I am more interested in capital " \
             "growth than maintaining the principal value."
question_2 += "\na. Strongly disagree \nb. Somewhat disagree \nc. Neutral" \
              "\nd. Somewhat agree \ne. Strongly agree \nEnter your answer: "

answer_2 = input(question_2)
user_score_io.calc_first_answer(answer_2)

question_3 = "\nQuestion 3:"
question_3 += "\nIf investing in a stock, would you rather:"
question_3 += "\na. Buy Companies that may make significant technological " \
              "advances that are still selling at their low initial offering " \
              "price. \nb. Established, well-known companies that have a " \
              "potential for continued growth \nc.'Blue chip' stocks that " \
              "pay dividends \nEnter your answer: "

answer_3 = input(question_3)
user_score_io.calc_second_answer(answer_3)
# Pass both answers to function that assigns user's objective
user_score_io.set_objective()

# Determines ESG category
user_score_esg = esg.EnvironmentalSocialGovernance()# Initialize esg instance

question_4 = "\nQuestion 4: "
question_4 += "\nWhen it comes to investing, Environmental issues such as " \
              "Sustainability, Renewable Energy,  Natural resources, and land " \
              "usage are important to me."
question_4 += "\na. Strongly disagree \nb. Somewhat disagree \nc. Neutral" \
              "\nd. Somewhat agree \ne. Strongly agree \nEnter your answer: "

answer_4 = input(question_4)
user_score_esg.calc_first_answer(answer_4)

question_5 = "\nQuestion 5:"
question_5 += "\nI take into consideration or would like to, social aspects of " \
              "companies that I invest in, such as Diversity, local community " \
              "impact, as well as Labor standards, and employees."
question_5 += "\na. Strongly disagree \nb. Somewhat disagree \nc. Neutral" \
              "\nd. Somewhat agree \ne. Strongly agree \nEnter your answer: "

answer_5 = input(question_5)
user_score_esg.calc_second_answer(answer_5)

question_6 = "\nQuestion 6:"
question_6 += "\nInvestors should take into consideration ethical business " \
              "practices, Executive Compensation, and Board Independence when " \
              "choosing which companies to have a stake in."
question_6 += "\na. Strongly disagree \nb. Somewhat disagree \nc. Neutral" \
              "\nd. Somewhat agree \ne. Strongly agree \nEnter your answer: "

answer_6 = input(question_6)
user_score_esg.calc_third_answer(answer_6)

question_7 = "\nQuestion 7:"
question_7 += "\nI like to support companies whose values align with mine."
question_7 += "\na. Strongly disagree \nb. Somewhat disagree \nc. Neutral" \
              "\nd. Somewhat agree \ne. Strongly agree \nEnter your answer: "

answer_7 = input(question_7)
user_score_esg.calc_fourth_answer(answer_7)

# Passing answer values to ESG method
user_score_esg.set_esg_cat()

# Display all answers
print(user_score_th.get_time())
print(user_score_io.get_objective())
print(user_score_esg.get_est_cat())

