ok_list = ['a', 'b', 'c']
while True:
    question = "enter a letter: "
    answer = input(question)
    if answer in ok_list:
        print("Thanks!")
        break
    else:
        print("You entered an invalid value. Please try again")
        continue
