# from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos("todos.txt", todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            # item = item.split()
            row = "{}-{}".format(index + 1, item)
            print(row, end="")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            del todos[index]

            functions.write_todos("todos.txt", todos)

            messenge = "Todo {} was removed from the list.".format(todo_to_remove)
            print(messenge)

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
