import functions
import PySimpleGUI as sg

# label = sg.Text("Type in a to-do")
# input_box = sg.InputText(tooltip="Enter to-do")
# add_button = sg.Button("Add")

# window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
# window.read()
# window.close()

layout = [[sg.Text("Enter a to-do")],
          [sg.InputText(tooltip="Enter to-do", key="todo"), sg.Button("Add")],
          [sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]), sg.Button("Edit")]]

window = sg.Window("My To-Do App", layout, font=("Helvetica", 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = todo = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
