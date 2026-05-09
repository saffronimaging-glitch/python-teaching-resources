# DEBUG THE OOP QUIZ


# Debug 1

class Question

    def __init__(self, question_text):

        self.question_text = question_text


# Debug 2

class Question:

    def __init__(self, question_text):

        question_text = question_text


question1 = Question("2 + 2?")

print(question1.question_text)


# Debug 3

class Question:

    def ask_question(self):
        print("Question asked")


question1 = Question

question1.ask_question()


# Debug 4

class Question:

    def __init__(self, question_text):

        self.question_text = question_text


questions = [

    Question("Question 1"),
    Question("Question 2")

]


for question in questions
    print(question.question_text)
