# STRETCH CHALLENGE - SCORE SYSTEM
# This links functions, parameters, return values and selection.

def ask_question(question, correct_answer, points):
    user_answer = input(question + " ")

    if user_answer.lower() == correct_answer.lower():
        print("Correct! You earned", points, "points.")
        return points
    else:
        print("Incorrect. You earned 0 points.")
        return 0


def display_grade(score):
    print("\nFinal score:", score)

    if score >= 5:
        print("Excellent result!")
    elif score >= 3:
        print("Good effort!")
    else:
        print("Keep practising!")


score = 0

score += ask_question("What is 2 + 2?", "4", 1)
score += ask_question("What keyword creates a function in Python?", "def", 2)
score += ask_question("What data type is True or False?", "boolean", 2)

display_grade(score)
