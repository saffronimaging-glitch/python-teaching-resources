# MULTIPLE QUESTION OBJECTS

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


question1 = Question("2 + 2?", "4")
question2 = Question("Capital of France?", "Paris")
question3 = Question("Colour of grass?", "green")


print(question1.question_text)
print(question2.question_text)
print(question3.question_text)
