# FIRST QUESTION CLASS

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


question1 = Question("What is 2 + 2?", "4")

print(question1.question_text)
print(question1.correct_answer)
