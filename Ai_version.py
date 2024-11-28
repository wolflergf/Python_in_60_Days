import os
from typing import List


class TodoManager:
    def __init__(self, filename: str = "todos.txt"):
        self.filename = filename
        self.todos: List[str] = self.load_todos()

    def load_todos(self) -> List[str]:
        """Load todos from file if it exists, otherwise return empty list."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return [line.strip() for line in file.readlines()]
            except Exception as e:
                print(f"Error loading todos: {e}")
                return []
        return []

    def save_todos(self) -> None:
        """Save todos to file."""
        try:
            with open(self.filename, "w") as file:
                file.write("\n".join(self.todos))
        except Exception as e:
            print(f"Error saving todos: {e}")

    def display_todos(self) -> None:
        """Display all todos with their indices."""
        if not self.todos:
            print("No todos found!")
            return
        for index, item in enumerate(self.todos, 1):
            print(f"{index}. {item}")

    def add_todo(self, todo: str) -> None:
        """Add a new todo and save to file."""
        if todo:
            self.todos.append(todo)
            self.save_todos()
            print("Todo added successfully!")
        else:
            print("Todo cannot be empty!")

    def edit_todo(self, index: int, new_todo: str) -> None:
        """Edit an existing todo by index."""
        if 0 <= index < len(self.todos) and new_todo:
            self.todos[index] = new_todo
            self.save_todos()
            print("Todo updated successfully!")
        else:
            print("Invalid index or empty todo!")

    def complete_todo(self, index: int) -> None:
        """Remove a completed todo by index."""
        if 0 <= index < len(self.todos):
            completed_todo = self.todos.pop(index)
            self.save_todos()
            print(f"Completed and removed: {completed_todo}")
        else:
            print("Invalid index!")


def get_valid_index(prompt: str, max_index: int) -> int:
    """Get a valid index from user input."""
    while True:
        try:
            index = int(input(prompt).strip()) - 1
            if 0 <= index < max_index:
                return index
            print(f"Please enter a number between 1 and {max_index}")
        except ValueError:
            print("Please enter a valid number!")


def main():
    todo_manager = TodoManager()

    commands = {
        "add": "Add a new todo",
        "show": "Display all todos",
        "edit": "Edit an existing todo",
        "complete": "Mark a todo as complete",
        "exit": "Exit the application",
    }

    print("Welcome to Todo Manager!")

    while True:
        print("\nAvailable commands:")
        for cmd, desc in commands.items():
            print(f"- {cmd}: {desc}")

        user_action = input("\nEnter a command: ").lower().strip()

        match user_action:
            case "add":
                todo = input("Enter a todo: ").strip().capitalize()
                todo_manager.add_todo(todo)

            case "show":
                todo_manager.display_todos()

            case "edit":
                if not todo_manager.todos:
                    print("No todos to edit!")
                    continue

                todo_manager.display_todos()
                index = get_valid_index(
                    "Enter the number to edit: ", len(todo_manager.todos)
                )
                new_todo = input("Enter the new todo: ").strip().capitalize()
                todo_manager.edit_todo(index, new_todo)

            case "complete":
                if not todo_manager.todos:
                    print("No todos to complete!")
                    continue

                todo_manager.display_todos()
                index = get_valid_index(
                    "Enter the number to complete: ", len(todo_manager.todos)
                )
                todo_manager.complete_todo(index)

            case "exit":
                print("Goodbye!")
                break

            case _:
                print("Invalid command! Please try again.")


if __name__ == "__main__":
    main()
