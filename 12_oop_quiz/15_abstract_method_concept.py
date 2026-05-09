# ABSTRACT METHOD CONCEPT
# A parent class defines a method that child classes should create.

class Question:

    def ask_question(self):

        print("Question types should create their own ask_question() method.")


class TimedQuestion(Question):

    def ask_question(self):

        print("Timed question asked here.")


class MultipleChoiceQuestion(Question):

    def ask_question(self):

        print("Multiple choice question asked here.")


question1 = TimedQuestion()
question2 = MultipleChoiceQuestion()

question1.ask_question()
question2.ask_question()
