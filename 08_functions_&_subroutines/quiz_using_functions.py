# QUIZ USING FUNCTIONS

def ask_question(question, correct_answer):
    user_answer = input(question + " ")

    if user_answer.lower() == correct_answer.lower(): # why do we use .lower here?
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0


score = 0

score += ask_question("What is 2 + 2?", "4")
score += ask_question("What keyword creates a function in Python?", "def")
score += ask_question("What data type is True or False?", "boolean")

print("Final score:", score)
