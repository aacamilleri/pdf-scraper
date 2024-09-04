# GUI Library
import PySimpleGUI as sg

# Application Layout
from gui.layout import layout

# Application Title
title: str = "Katie's PDF Screenshotter"

sg.theme('LightPurple')
window = sg.Window(title, layout, element_padding=6)
