import json

with open("bonus/files/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)


for quest in data:
    print(quest["quest_text"])
    for index, alternative in enumerate(quest["alternatives"]):
        print(index + 1, "-", alternative)
    user_choise = int(input("Enter your answer: "))
    quest["user_choise"] = user_choise

score = 0
for index, quest in enumerate(data):
    if quest["user_choise"] == quest["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = "{} {} - Your answer: {}, Correct answer: {}.".format(index + 1, result, quest["user_choise"], quest["correct_answer"])
    print(message)


print(score, "/", len(data))
