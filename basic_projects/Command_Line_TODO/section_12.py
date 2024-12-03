def get_todos(file_path) -> list[str]:
    """Recupera lista de tarefas a partir de um aquivo de texto.

    Returns:
        list[str]: Uma lista contendo as tarefas lidas do arquivo.
    """
    with open(file_path, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(file_path, todos_arg):
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"

        todos = get_todos("./todos.txt")

        todos.append(todo)

        write_todos("./todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("./todos.txt")

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = get_todos("./todos.txt")

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
            number = int(input("what number do tou like to replace? ").strip()) - 1
            todos[number] = input("Enter a new todo: ").capitalize().strip() + "\n"

            write_todos("./todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        todos = get_todos("./todos.txt")

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)
        number = int(input("Number of the todo to complete: ").strip()) - 1
        todos.pop(number)

        write_todos("./todos.txt", todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
