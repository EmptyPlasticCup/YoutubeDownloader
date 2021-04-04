import PySimpleGUI as sg 
from pytube import YouTube
import pafy


sg.theme('LightBlue1') #can be any theme

#variables
layoutInput = [

    [sg.Text('URL:'), sg.InputText()],
    [sg.Text('Video Destination:'), sg.InputText(), sg.FolderBrowse()],
    [sg.Button('Enter'), sg.Button('Quit')]

]

layoutFileSelection = [

    [sg.Text('Choose File Format')],
    [sg.Button('Audio'), sg.Button('Video')]

]

layoutSuccess = [

    [sg.Text('Download successful!')],
    [sg.Button('Exit')]

]

layoutFail = [

    [sg.Text('We got an error! Please check the URL and the file path again.')],
    [sg.Button('Quit')]

]

success = False

#code

window = sg.Window('Video Downloader', layoutInput, size = (700,100))

while True:
    event, values = window.read()

    try:

        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        elif event == 'Enter':

           url = str(values[0])

           video = YouTube(url)
           path = str(values[1])

           window.hide()
           validCheck = True
           break

    except:
        window.hide()
        window = sg.Window('Error!', layoutFail, size = (500,100),)

        if event == sg.WIN_CLOSED or event == 'Quit':
            break

if validCheck:
    window = sg.Window('File Format', layoutFileSelection, size = (500,100))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Audio':
            pafy.new(url).getbestaudio().download(filepath = path)

            window.hide()
            success = True
            break
        elif event == 'Video':
            video.streams.get_highest_resolution().download(path)
            window.hide()
            success = True
            break



if success:

    window = sg.Window('Success!', layoutSuccess, size = (500,100))

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
             break


window.close()
