import PySimpleGUI as sg
import os

sg.theme('Dark Blue 3')  # please make your windows colorful

tab1=sg.Tab("title1", [[sg.Multiline(s=(150,100), key="first_tab")]])
tab2=sg.Tab("title2", [[sg.Multiline(s=(150,100), key="second_tab")]])
Tg = sg.TabGroup([[tab1, tab2]])


layout = [[sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()],
            [Tg],
            [sg.OK(), sg.Cancel()] ]

window = sg.Window('Get filename example', layout).Finalize()
window.Maximize()

def read_file(file):
    if os.path.isfile(file):
        with open(file, 'r') as file_data:
            for line in file_data:
                print(line)
                return file_data.read()


window["first_tab"].update(read_file("자료형.py"))
event, values = window.read()

window.close()