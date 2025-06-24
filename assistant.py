import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
import platform
import os
import sys

is_android = 'android' in platform.platform().lower()

if is_android:
    def speak(text):
        os.system(f'termux-tts-speak "{text}"')
else:
    engine = pyttsx3.init()
    def speak(text):
        engine.say(text)
        engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    return command

def run_assistant():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")
    elif 'search' in command:
        topic = command.replace('search', '')
        info = wikipedia.summary(topic, sentences=2)
        speak(info)
    elif 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'exit' in command:
        speak("Goodbye!")
        sys.exit()
    else:
        speak("Please say that again.")

while True:
    run_assistant()
