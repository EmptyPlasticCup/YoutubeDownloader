from pytube import YouTube
import pafy
import os


print('''


██╗░░░██╗░█████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
░╚████╔╝░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██████╦╝█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝░░░██║░░░╚██████╔╝██████╦╝███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝

██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

by Emptycup
Twitter - @EmptyGlassCup

text art - https://fsymbols.com/text-art/
''')

input('Press Enter to continue...')

errorCount = 0
while True:
    try:
        url = input('Enter Video URL: ')
        video = YouTube(url)
        break
    except:
        if errorCount == 0:
            print('Error! Please check the url and try again.')
            errorCount = 1
        elif errorCount >= 1:
            print(f'''

Error! An error has occured {errorCount + 1} times. If you a sure that you type the URL correctly, the issue might lie
with pytube itself. You can't do much to fix it. 
            
            ''')
            errorCount += 1
        else:
            print('You should never see this message... This error should never occur')

while True:
    path = input('Enter download path. (If left blank, the downloads folder will be used): ')
    if path == '':
        os.path.join(os.path.expanduser('~'), 'Downloads')
    if not os.path.exists:
        print('Invalid file path. Please check your path again.')
    else:
        break

while True:
    format = str(input('Download as an audio or a video file?: '))
    if format.lower() == 'video' or 'v':
        print('Downloading...')
        video.streams.get_highest_resolution().download(path)
        break
    elif format.lower() == 'audio' or 'a':
        print('Downloading...')
        pafy.new(url).getbestaudio(preftype='m4a', ftypestrict='True').download(filepath=path)
        break
    else:
        print('Invalid format. Please answer as either video or audio!')

print('Done!')
