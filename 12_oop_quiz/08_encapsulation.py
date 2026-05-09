# ENCAPSULATION
# Protecting object data

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text

        # Private attribute
        self.__correct_answer = correct_answer


question1 = Question("2 + 2?", "4")

print(question1.question_text)

# This would normally be avoided:
# print(question1.__correct_answer)
