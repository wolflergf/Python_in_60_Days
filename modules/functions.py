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
