# AGGREGATION / COMPOSITION

class Question:

    def __init__(self, question_text):

        self.question_text = question_text


class Quiz:

    def __init__(self):

        self.questions = []


    def add_question(self, question):

        self.questions.append(question)


quiz = Quiz()

question1 = Question("What is 2 + 2?")
question2 = Question("Capital of France?")

quiz.add_question(question1)
quiz.add_question(question2)


for question in quiz.questions:
    print(question.question_text)
