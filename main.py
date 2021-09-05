import PyPDF2
import pyttsx3

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 125)
voices = speaker.getProperty('voices')


def reader():
    print('Enter the pdf name:')
    name = input('') + '.pdf'
    text = open(name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(text)
    pages = pdfReader.numPages
    i = int(input('Enter the page number from ..to start listening..(enter 0 for first page)\n'))

    for num in range(i, pages):
        print('To go back to main menu..please wait for end of page')
        first = pdfReader.getPage(num)
        cont = first.extractText()
        speaker.say(cont)
        speaker.runAndWait()
        a = input('Proceed to next page - y/n \n ')
        if a == 'y':
            continue
        elif a == 'n':
            break


speaker.stop()


def changevoice():
    x = input('For male voice press m and for female voice press f \n')
    if x == 'f':
        speaker.setProperty('voice', voices[1].id)
    elif x == 'm':
        speaker.setProperty('voice', voices[0].id)


def changerate():
    a = float(input('Enter the desired rate between (i.e. 0.25,0.5...)'))
    speaker.setProperty('rate', a * 100)


v = 0
while v != 4:
    v = int(input('''Welcome to Free Audio pdf reader ! Now you can listen to any book of your choice completely free.
                 Press :- 1)start reading
                          2)Change the gender of the voice
                          3)Change the speaking rate
                          4)exit\n'''))

    if v == 1:
        reader()

    elif v == 2:
        changevoice()
    elif v == 3:
        changerate()
    else:
        print('Thank you for using audiobook !!')
