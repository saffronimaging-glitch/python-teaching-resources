# PROCEDURAL QUIZ USING FUNCTIONS

score = 0


def ask_question(question, answer):

    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        return 1

    else:
        print("Incorrect!")
        return 0


score += ask_question("What is 2 + 2?", "4")
score += ask_question("Capital of France?", "Paris")
score += ask_question("What data type is True or False?", "Boolean")


print("Final score:", score)
