import time_horizon as th

# Program asks users a series of questions to determine which
# securities to suggests (educational purpose ONLY)

# Initialize time horizon object
user_score = th.TimeHorizon()

# Determine time horizon
question_1 = "How long are you planning on investing your money?"
question_1 += "\na. Less than 3 years \nb. 3-5 years\nc. 6-10 years\n" \
              "d. More than 11 years\nEnter your answer: "

answer_1 = input(question_1)
user_score.set_time(answer_1)

# Determine Investment Objective
question_2 = "When it comes to investing, I am more interested in capital " \
             "growth than maintaining the principal value."
question_2 += "\na. Strongly Disagree \nb. Somewhat disagree \nc. Neutral" \
              "\nd. Somewhat agree \ne.	Strongly agree"
answer_2 = input(question_2)



print(user_score.get_time())
