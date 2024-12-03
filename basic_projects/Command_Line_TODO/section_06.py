todos = []

while True:
    user_action = input("Type add / show / edit / complete / exit: ").lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ").capitalize().strip() + "\n"

            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("./todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":

            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
        case "edit":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            number = int(input("what number do tou like to replace? ").strip()) - 1
            todos[number] = input("Enter a new todo: ").capitalize().strip() + "\n"
        case "complete":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}".strip()
                print(row)
            number = int(input("Number of the todo to complete: ").strip()) - 1
            todos.pop(number)
        case "exit":
            break
        case _:
            print("Enter a valid command.")
print("Bye!")
