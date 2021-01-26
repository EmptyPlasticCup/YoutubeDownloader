import PySimpleGUI as sg 
from pytube import YouTube
import os.path

sg.theme('DarkAmber') #can be any theme

#variables
layoutInput = [

    [sg.Text('URL:'), sg.InputText()],
    [sg.Text('Video Destination:'), sg.InputText(), sg.FolderBrowse()],
    [sg.Button('Enter'), sg.Button('Quit')]

]

layoutSuccess = [

    [sg.Text('Download successful!')],
    [sg.Button('Exit')]

]

windowInput = sg.Window('Video Downloader', layoutInput, size = (500,100))
windowOutput = sg.Window('Success!', layoutSuccess, size = (500,100))

appCancelled = True

#code

while True:
    event, values = windowInput.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Enter':
        source = YouTube(str(values[0]))
        path = str(values[1])

        source.streams.get_highest_resolution().download(path)
        windowInput.close
        appCancelled = False
        break

if not appCancelled:
    while True:
        event, values = windowOutput.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
             break


windowInput.close()
windowOutput.close()
