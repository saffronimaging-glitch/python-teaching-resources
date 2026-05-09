# __init__ AND self

class Question:

    def __init__(self, question_text, correct_answer):

        # Store values inside the object
        self.question_text = question_text
        self.correct_answer = correct_answer


question1 = Question("Capital of France?", "Paris")

print(question1.question_text)
print(question1.correct_answer)
