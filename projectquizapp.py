# Quiz App

# Questions, options, aur answers ko lists mein store karenge
questions = [
    {
        "question": "What is Sidrat al-Muntaha?",
        "options": ["A lote tree of the farthest boundary", "Drink for the people of Jannah", "Food for the people of Jannah","An olive tree of the farthest boundary",],
        "answer": 0
    },
    {
        "question": "What is the virtue of reciting Ayatul Kursi before going to bed at night to sleep?",
        "options": ["You are protected from harm till sunrise ", "Gives you strength", "House in Jannah", "Takes away hunger"],
        "answer": 0
    },
    {
        "question": " What does Zam Zam mean?",
        "options": ["drink", "water well", "stop", "Holy water"],
        "answer": 2
    }
]

# Score ko initialize karenge
score = 0

# Welcome Screen
print("Welcome to the Quiz App!")
print("Instructions: Choose the correct answer from the options.")

# Question Screen
for question in questions:
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = int(input("Enter the correct answer number: ")) - 1
    if answer == question["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print(f"Incorrect answer. The correct answer is {question['options'][question['answer']]}")

# Score Screen
print(f"Your final score is {score} out of {len(questions)}")
print("Do you want to play again? (yes/no)")
play_again = input().lower()
if play_again == "yes":
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        answer = int(input("Enter the correct answer number: ")) - 1
        if answer == question["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print(f"Incorrect answer. The correct answer is {question['options'][question['answer']]}")
    print(f"Your final score is {score} out of {len(questions)}")
else:
    print("Thanks for playing!")