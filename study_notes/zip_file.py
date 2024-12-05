import FreeSimpleGUI as sg

layout = [
    [sg.Text("Select files to compress:"), sg.Input(), sg.FilesBrowse("Choose")],
    [sg.Text("Select destination folder:"), sg.Input(), sg.FolderBrowse("Choose")],
    [sg.Button("Compress")],
]

window = sg.Window("Zip App", layout)


event, values = window.read()
window.close()
