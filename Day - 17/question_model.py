from data import question_data


class Question:
    def __init__(self ,question, answer):
        self.question = question
        self.answer = answer

questions = []
for text in question_data:
    ques = Question(text["text"], text["answer"])
    questions.append(ques)

print(questions[1].question)
print(questions[1].answer)
