# FULL PROCEDURAL QUIZ GAME

score = 0


def welcome_message():
    print("Welcome to the Quiz Game!")
    print("-------------------------")


def ask_question(question, answer):

    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        return 1

    else:
        print("Incorrect.\n")
        return 0


def display_final_score(score):

    print("-------------------------")
    print("Final Score:", score)

    if score == 3:
        print("Excellent!")

    elif score == 2:
        print("Good effort!")

    else:
        print("Keep practising!")


# Main Program

welcome_message()

score += ask_question("What is 2 + 2?", "4")
score += ask_question("What colour is grass?", "green")
score += ask_question("What keyword creates a function in Python?", "def")

display_final_score(score)
