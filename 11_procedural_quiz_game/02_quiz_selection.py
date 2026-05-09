# QUIZ USING SELECTION

score = 0


question1 = "What colour is grass?"
answer1 = "green"

user_answer = input(question1 + " ")

if user_answer.lower() == answer1.lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


question2 = "What is 5 + 5?"
answer2 = "10"

user_answer = input(question2 + " ")

if user_answer.lower() == answer2.lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("Final score:", score)
