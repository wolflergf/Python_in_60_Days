FILE_PATH = "./todos.txt"


def get_todos(filepath=FILE_PATH) -> list[str]:
    """Retrieves task list from a text file.

    Returns:
        list[str]: A list containing tasks read from the file.
    """
    with open(filepath, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILE_PATH) -> None:
    """Write the tash to a text file.

    Args:
        file_path (str): The path to the text file where tasks will be saved.
        todos_arg (list of str): A list of tasks, each as a string, to be written to the file.
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos("./todos.txt")

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
            number = int(input("what number do tou like to replace? ").strip()) - 1
            todos[number] = input("Enter a new todo: ").capitalize().strip() + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        todos = get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)
        number = int(input("Number of the todo to complete: ").strip()) - 1
        todos.pop(number)

        write_todos(todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
