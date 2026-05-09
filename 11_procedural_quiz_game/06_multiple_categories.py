# MULTIPLE QUIZ CATEGORIES
# This begins to show the limitations of procedural programming.

maths_questions = [
    "What is 10 x 10?",
    "What is 50 / 5?"
]

maths_answers = [
    "100",
    "10"
]


science_questions = [
    "What planet do we live on?",
    "What gas do humans breathe in?"
]

science_answers = [
    "earth",
    "oxygen"
]


score = 0


def ask_questions(questions, answers):

    score = 0

    for index in range(len(questions)):

        user_answer = input(questions[index] + " ")

        if user_answer.lower() == answers[index]:
            print("Correct!")
            score += 1

        else:
            print("Incorrect!")

    return score


print("MATHS QUIZ")
score += ask_questions(maths_questions, maths_answers)

print("\nSCIENCE QUIZ")
score += ask_questions(science_questions, science_answers)

print("\nFinal score:", score)
