import time_horizon as th

# Program asks users a series of questions to determine which
# securities to suggests (educational purpose ONLY)

user_score = th.TimeHorizon()

question_1 = "How long are you planning on investing your money?"
question_1 += "\na. Less than 3 years \nb. 3-5 years\nc. 6-10 years\n" \
              "d. More than 11 years\nEnter your answer: "

answer = input(question_1)

user_score.set_time(answer)
print(user_score.get_time())
