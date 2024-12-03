import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "modules"))
)
import FreeSimpleGUI as sg
import functions

layout = [
    [sg.Text("What's your name?")],  # Part 2 - The Layout
    [sg.Input()],
    [sg.Button("Ok")],
]

# Create the window
window = sg.Window("Window Title", layout)  # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()  # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print("Hello", values[0], "! Thanks for trying FreeSimpleGUI")

# Finish up by removing from the screen
window.close()
