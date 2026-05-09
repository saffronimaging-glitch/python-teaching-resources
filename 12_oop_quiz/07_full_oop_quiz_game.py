# FULL OOP QUIZ GAME

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


    def ask_question(self):

        user_answer = input(self.question_text + " ")

        if user_answer.lower() == self.correct_answer.lower():
            print("Correct!\n")
            return 1

        else:
            print("Incorrect.\n")
            return 0


questions = [

    Question("What is 2 + 2?", "4"),
    Question("Capital of France?", "Paris"),
    Question("What keyword creates a function?", "def")

]


score = 0


for question in questions:
    score += question.ask_question()


print("Final score:", score)
