# STRETCH CHALLENGE - FULL OOP QUIZ

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


    def ask_question(self):

        answer = input(self.question_text + " ")

        if answer.lower() == self.correct_answer.lower():
            print("Correct!")
            return 1

        else:
            print("Incorrect!")
            return 0


class Quiz:

    def __init__(self):

        self.questions = []
        self.score = 0


    def add_question(self, question):

        self.questions.append(question)


    def run_quiz(self):

        for question in self.questions:
            self.score += question.ask_question()

        print("Final score:", self.score)


quiz = Quiz()

quiz.add_question(Question("2 + 2?", "4"))
quiz.add_question(Question("Capital of France?", "Paris"))
quiz.add_question(Question("What colour is grass?", "green"))

quiz.run_quiz()
