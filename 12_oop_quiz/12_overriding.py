# OVERRIDING METHODS

class Question:

    def ask_question(self):
        print("Ask the question normally")


class TimedQuestion(Question):

    def ask_question(self):
        print("Ask the question with a timer")


question1 = Question()
question2 = TimedQuestion()

question1.ask_question()
question2.ask_question()
