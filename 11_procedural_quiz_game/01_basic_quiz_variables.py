# BASIC PROCEDURAL QUIZ
# Questions and answers stored as variables

question1 = "What is 2 + 2?"
answer1 = "4"

question2 = "What is the capital of France?"
answer2 = "Paris"

question3 = "What keyword creates a function in Python?"
answer3 = "def"


print(question1)
user_answer = input("Answer: ")

if user_answer.lower() == answer1.lower():
    print("Correct!")
else:
    print("Incorrect!")
