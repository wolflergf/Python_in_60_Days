import PySimpleGUI as sg


sg.theme("DarkAmber")
layout = [[sg.Text("Select files to compress:"), sg.Input(), sg.FilesBrowse("Open")],
          [sg.Text("Select destination folder:"), sg.Input(), sg.FolderBrowse("Open")],
          [sg.Button("Compress")],
          [sg.Button("Exit")]]

window = sg.Window("My ZIP App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    print("You entered ", values[0])

window.close()
