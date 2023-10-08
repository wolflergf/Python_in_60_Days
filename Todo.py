def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit delete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.split("\n")
            row = "{}-{}".format(index + 1, item)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.append(index)

            write_todos("todos.txt", todos)

            messenge = "Todo {} was removed from the list.".format(todo_to_remove)
            print(messenge)

        except IndexError:
            print("There is no item with that number")
            continue
