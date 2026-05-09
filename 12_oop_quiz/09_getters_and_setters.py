# GETTERS AND SETTERS

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.__correct_answer = correct_answer


    def get_answer(self):
        return self.__correct_answer


    def set_answer(self, new_answer):
        self.__correct_answer = new_answer


question1 = Question("2 + 2?", "4")

print(question1.get_answer())

question1.set_answer("four")

print(question1.get_answer())
