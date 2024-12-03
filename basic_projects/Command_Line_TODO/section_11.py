FILE_PATH = "./todos.txt"
"""Caminho para o arquivo que armazena as tarefas.
"""


def get_todos() -> list[str]:
    """Recupera lsita de tarefas a partir de um aquivo de texto.

    Returns:
        list[str]: Uma lista contendo as tarefas lidas do arquivo.
    """
    with open(FILE_PATH, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"

        todos = get_todos()

        todos.append(todo)

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

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

            with open("./todos.txt", "w") as file:
                file.writelines(todos)

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

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
