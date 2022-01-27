import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import flask

listener = sr.Recognizer()
alexa = pyttsx3.init()


def talk(text):
    alexa.say(text)
    alexa.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("lstening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'play' in command:
        song = command.replace("play", '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tall me about', '')
        info = wikipedia.summary(look_for, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I did not get it but i am going to search  it for you')
        pywhatkit.search(command)


while True:
    run_alexa()
