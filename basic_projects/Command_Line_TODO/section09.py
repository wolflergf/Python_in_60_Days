while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    if "add" in user_action:
        todo = user_action[4:].capitalize() + "\n"

        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    if "show" in user_action:
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)

    if "edit" in user_action:
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)
        number = int(input("what number do tou like to replace? ").strip()) - 1
        todos[number] = input("Enter a new todo: ").capitalize().strip() + "\n"

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    if "complete" in user_action:
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)
        number = int(input("Number of the todo to complete: ").strip()) - 1
        todos.pop(number)

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    if "exit" in user_action:
        break

print("Bye!")
