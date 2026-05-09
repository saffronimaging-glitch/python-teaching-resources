# ATTRIBUTES AND METHODS

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


    def ask_question(self):

        user_answer = input(self.question_text + " ")

        if user_answer.lower() == self.correct_answer.lower():
            print("Correct!")
            return 1

        else:
            print("Incorrect!")
            return 0


question1 = Question("What is 5 + 5?", "10")

score = question1.ask_question()

print("Score:", score)
