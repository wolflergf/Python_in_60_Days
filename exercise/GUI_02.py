import PySimpleGUI as sg

sg.theme("Python")
layout = [[sg.Text("Enter feet:"), sg.Input()],
          [sg.Text("Enter inches:"), sg.Input()],
          [sg.Button("Convert")]]

window = sg.Window("Convertor", layout)

window.read()
window.close()
