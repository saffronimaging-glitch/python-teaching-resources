# DEBUG THE PROCEDURAL QUIZ


# Debug 1
# This score should increase.

score = 0

score + 1

print(score)


# Debug 2
# This function should return the score.

def ask_question():

    answer = input("What is 2 + 2? ")

    if answer == "4":
        return 1

    else:
        return 0


score = 0

score += ask_question

print(score)


# Debug 3
# This loop should ask all questions.

questions = [
    "Question 1",
    "Question 2",
    "Question 3"
]

for question in range(len(questions)):
    print(question)


# Debug 4
# This should compare answers correctly.

user_answer = "Paris"
correct_answer = "Paris"

if user_answer = correct_answer:
    print("Correct!")
