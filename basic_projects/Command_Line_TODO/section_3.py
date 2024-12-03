todos = []

while True:
    user_action = input("Type add, show or exit: ").lower().strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ").capitalize()
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(index + 1, "-", item)
        case "exit":
            print("Bye")
            break
