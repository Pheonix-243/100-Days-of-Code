from data import question_data


class Question:
    def __init__(self ,question, answer):
        self.question = question
        self.answer = answer

questions = []
for text in range(len(question_data) - 1):
    ques = Question(question_data[text]["text"], question_data[text]["answer"])
    questions.append(ques)

print(questions[1].question)
print(questions[1].qan)
