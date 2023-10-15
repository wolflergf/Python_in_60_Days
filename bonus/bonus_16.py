import PySimpleGUI as sg


sg.theme("DarkAmber")
layout = [[sg.Text("Select files to compress:"), sg.Input(), sg.FilesBrowse("Open")],
          [sg.Text("Select destination folder:"), sg.Input(), sg.FolderBrowse("Open")],
          [sg.Button("Compress")]]

window = sg.Window("My ZIP App", layout)

window.read()
window.close()
