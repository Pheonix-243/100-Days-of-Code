import time
import json
from data import question_data


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


# Load previous leaderboard or create empty one
leaderboard_file = "leaderboard.json"
try:
    with open(leaderboard_file, "r") as file:
        leaderboard = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    leaderboard = {}

# Create question objects
questions = [Question(q["text"], q["answer"]) for q in question_data]

# Ask for player's name
player_name = input("Enter your name: ").strip().capitalize()
score = 0

# Quiz loop with timer
for i, question in enumerate(questions, 1):
    print(f"\nQ{i}. {question.question} (True/False): ")

    start_time = time.time()
    user_ans = input("Your answer here: ").strip().capitalize()
    elapsed_time = time.time() - start_time

    if elapsed_time > 5:
        print("⏳ Time up! You lost this one! 😭\n")
    elif user_ans == question.answer:
        print("✅ That is right!😻\n")
        score += 1
    else:
        print(f"❌ That is wrong, bro! The answer is {question.answer}\n")

# Update leaderboard
leaderboard[player_name] = score
sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

# Save leaderboard
with open(leaderboard_file, "w") as file:
    json.dump(leaderboard, file, indent=4)

# Display final results
print(f"\n🎉 Quiz over! {player_name}, your score was {score}/{len(questions)}")

# Show leaderboard
print("\n🏆 LEADERBOARD 🏆")
for rank, (name, top_score) in enumerate(sorted_leaderboard, 1):
    print(f"{rank}. {name} - {top_score} points")
