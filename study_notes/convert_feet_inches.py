import FreeSimpleGUI as sg

layout = [
    [sg.Text("Enter Feet: "), sg.Input()],
    [sg.Text("Enter Inches: "), sg.Input()],
    [sg.Button("Convert")],
]

window = sg.Window("Covertor", layout)


event, values = window.read()
window.close()
