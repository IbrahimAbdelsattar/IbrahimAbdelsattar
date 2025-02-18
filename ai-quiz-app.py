# AI Quiz App

# Import required libraries
import time
import random
import json

# Quiz questions and answers
quiz_questions = {
    "AI Basics": {
        "What is the primary goal of Artificial Intelligence?": "To create intelligent machines",
        "What is Machine Learning?": "A subset of AI that involves training models on data",
        "What is Natural Language Processing?": "A field of AI that deals with human language"
    },"Machine Learning": {
        "What is Supervised Learning?": "A type of Machine Learning where the model is trained on labeled data",
        "What is Unsupervised Learning?": "A type of Machine Learning where the model is trained on unlabeled data",
        "What is Reinforcement Learning?": "A type of Machine Learning where the model learns through trial and error"
    },
    "Deep Learning": {
        "What is Deep Learning?": "A subset of Machine Learning that uses neural networks",
        "What is a Convolutional Neural Network?": "A type of neural network for image analysis",
        "What is a Recurrent Neural Network?": "A type of neural network for sequential data"
    }
}

# Initialize score and leaderboard
score = 0
leaderboard = {}

# Welcome message
print("Welcome to the AI Quiz App!")
print("You will be asked 9 questions from 3 categories: AI Basics, Machine Learning, and Deep Learning .")
print("You have 30 seconds to answer each question. Good luck!")

# Ask quiz questions
for category, questions in quiz_questions.items():
    print(f"\nCategory: {category}")
    for question, answer in questions.items():
        start_time = time.time()
        user_answer = input(question + ": ")
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 30:
            print("Time's up! You took too long to answer.")
        elif user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {answer}.")

# Display final score
print(f"\nYour final score is {score} out of 9.")

# Update leaderboard
name = input("Please enter your name: ")
leaderboard[name] = score
with open("leaderboard.json", "w") as f:
    json.dump(leaderboard, f)

# Display leaderboard
print("\nLeaderboard:")
with open("leaderboard.json", "r") as f:
    leaderboard = json.load(f)
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for name, score in sorted_leaderboard:
        print(f"{name}: {score}")

# Pass/fail message
if score >= 6:
    print("\nYou passed! Congratulations!")
else:
    print("\nYou didn't pass. Better luck next time!")