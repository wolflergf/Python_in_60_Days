import PySimpleGUI as sg

layout = [[sg.Text("Enter feet: "), sg.Input(key="feet")],
          [sg.Text("Enter a inches: "), sg.Input(key="inches")],
          [sg.Button("Convert"), sg.Text(key="output")]]

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    print(event, values)
    meters = (float(values["feet"]) * 0.3048) + (float(values["inches"]) * 0.0254)
    window["output"].update(value="{} meters".format(meters))

window.close()
