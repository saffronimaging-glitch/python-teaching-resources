# INSTANTIATION
# Creating objects from a class

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


question1 = Question("What is 2 + 2?", "4")
question2 = Question("What colour is grass?", "green")
question3 = Question("What keyword creates a loop?", "for")


print(question1.question_text)
print(question2.question_text)
print(question3.question_text)
