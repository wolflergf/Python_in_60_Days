todos = []

while True:
    user_action = input("Type add / show / edit / exit: ").lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ").capitalize().strip()
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(index + 1, "-", item)
        case "edit":
            for index, item in enumerate(todos):
                print(index + 1, "-", item)
            number = int(input("what number do tou like to replace? ").strip()) - 1
            todos[number] = input("Enter a new todo: ").capitalize().strip()
        case "exit":
            break
print("Bye!")
