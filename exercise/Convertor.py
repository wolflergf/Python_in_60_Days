import PySimpleGUI as sg

layout = [[sg.Text("Enter feet: "), sg.Push(), sg.Input(key="feet")],
          [sg.Text("Enter a inches: "), sg.Push(), sg.Input(key="inches")],
          [sg.Button("Convert"), sg.Button("Exit"), sg.Text(key="output"), sg.Push()]]

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break

    print(event, values)
    meters = (float(values["feet"]) * 0.3048) + (float(values["inches"]) * 0.0254)
    window["output"].update(value="{} meters".format(meters))


window.close()
