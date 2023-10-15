import functions
import PySimpleGUI as sg

# label = sg.Text("Type in a to-do")
# input_box = sg.InputText(tooltip="Enter to-do")
# add_button = sg.Button("Add")

# window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
# window.read()
# window.close()

sg.theme("DarkAmber")
layout = [[sg.Text("Enter a to-do"), sg.InputText(tooltip="Enter to-do"), sg.Button("Add")],
          [sg.Button("Exit")]]

window = sg.Window("My To-Do App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    print("You entered ", values[0])

window.close()
