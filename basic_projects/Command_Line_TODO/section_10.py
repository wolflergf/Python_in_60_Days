while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"

        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}".strip()
            print(row)

    elif user_action.startswith("edit"):
        try:
            with open("./todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
            number = int(input("what number do tou like to replace? ").strip()) - 1
            todos[number] = input("Enter a new todo: ").capitalize().strip() + "\n"

            with open("./todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid.")
            user_action = (
                input("Type add / show / edit / complete / exit: ").lower().strip()
            )

    elif user_action.startswith("complete"):
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

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
