while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ").capitalize().strip() + "\n"

            with open("./todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("./todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            with open("./todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)

        case "edit":
            with open("./todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
            number = int(input("what number do tou like to replace? ").strip()) - 1
            todos[number] = input("Enter a new todo: ").capitalize().strip() + "\n"

            with open("./todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            with open("./todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
            number = int(input("Number of the todo to complete: ").strip()) - 1
            todos.pop(number)

            with open("./todos.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break
        case _:
            print("Enter a valid command.")
print("Bye!")
