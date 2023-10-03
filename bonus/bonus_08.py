date = input("Enter today's date: ")
mood = input("How do you rate your modd today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open("./bonus/journal/{}.txt".format(date), "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)
