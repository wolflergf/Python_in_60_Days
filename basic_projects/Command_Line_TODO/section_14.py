import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "modules"))
)
import functions

while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("./todos.txt")

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
            number = int(input("what number do tou like to replace? ").strip()) - 1
            todos[number] = input("Enter a new todo: ").capitalize().strip() + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)
        number = int(input("Number of the todo to complete: ").strip()) - 1
        todos.pop(number)

        functions.write_todos(todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
