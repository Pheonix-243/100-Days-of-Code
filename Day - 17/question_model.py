from data import question_data


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


questions = [Question(q["text"], q["answer"]) for q in question_data]

score = 0


for i , question in enumerate(questions, 1):
    user_ans = input(f"{question.question} (True/False)").strip().capitalize()
    if user_ans == question.question:
        print("That is right!😻")
        score += 1
    else:
        print("That is wrong Bro! What the heck? You gotta sit up! Stop being dump like ChatGPT")

print(f"Quiz over! your score was {score}")

