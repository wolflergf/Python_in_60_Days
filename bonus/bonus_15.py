import json

with open("bonus/files/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for quest in data:
    print(quest["quest_text"])
