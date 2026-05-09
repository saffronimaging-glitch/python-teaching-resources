# INHERITANCE

class Question:

    def __init__(self, question_text, correct_answer):

        self.question_text = question_text
        self.correct_answer = correct_answer


class TimedQuestion(Question):

    def __init__(self, question_text, correct_answer, time_limit):

        super().__init__(question_text, correct_answer)

        self.time_limit = time_limit


question1 = TimedQuestion("2 + 2?", "4", 10)

print(question1.question_text)
print("Time limit:", question1.time_limit)
