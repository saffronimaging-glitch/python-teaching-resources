# QUIZ USING ITERATION

questions = [
    "What is 2 + 2?",
    "Capital of France?",
    "What colour is the sky?"
]

answers = [
    "4",
    "paris",
    "blue"
]

score = 0


for index in range(len(questions)):

    user_answer = input(questions[index] + " ")

    if user_answer.lower() == answers[index]:
        print("Correct!")
        score += 1

    else:
        print("Incorrect!")


print("Final score:", score)
