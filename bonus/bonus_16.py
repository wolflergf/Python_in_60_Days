import PySimpleGUI as sg
from zip_creator import make_archive


sg.theme("DarkAmber")
layout = [[sg.Text("Select files to compress:"), sg.Input(), sg.FilesBrowse("Open", key="files")],
          [sg.Text("Select destination folder:"), sg.Input(), sg.FolderBrowse("Open", key="folder")],
          [sg.Button("Compress"), sg.Text(key="output")]]

window = sg.Window("My ZIP App", layout)


while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")


window.close()
