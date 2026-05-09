# MODULAR PROGRAMMING EXAMPLE
# Breaking a program into smaller reusable modules.

def welcome_message():
    print("Welcome to the quiz!")


def ask_question(question, answer):

    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        return 1
    else:
        return 0


def display_final_score(score):
    print("Final score:", score)


# Main program

score = 0

welcome_message()

score += ask_question("What is 2 + 2?", "4")
score += ask_question("Capital of France?", "Paris")

display_final_score(score)
