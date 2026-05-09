# QUESTIONS IN A LIST

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


questions = [

    Question("2 + 2?", "4"),
    Question("Capital of France?", "Paris"),
    Question("Colour of the sky?", "blue")

]


for question in questions:
    print(question.question_text)
