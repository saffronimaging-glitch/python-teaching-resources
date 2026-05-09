# POLYMORPHISM

class Question:

    def ask_question(self):
        print("Standard question")


class TimedQuestion(Question):

    def ask_question(self):
        print("Timed question")


class MultipleChoiceQuestion(Question):

    def ask_question(self):
        print("Multiple choice question")


question1 = Question()
question2 = TimedQuestion()
question3 = MultipleChoiceQuestion()


question1.ask_question()
question2.ask_question()
question3.ask_question()
