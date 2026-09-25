import sys
import pyaudiowpatch
import webbrowser

sys.modules["pyaudio"] = pyaudiowpatch

import speech_recognition as sr
import pyttsx3
from datetime import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:",text)

    if "hello" in text.lower():
        engine.say("Hello! How can i help you?")
        engine.runAndWait()

    elif "time" in text.lower():
        current_time = datetime.now().strftime("%I:%M %p")

        print("Current time:",current_time)

        engine.say(f"The current time is {current_time}")
        engine.runAndWait()

    elif "date" in text.lower():
        current_date = datetime.now().strftime("%d %B %Y")

        print("Today's date:",current_date)

        engine.say("Today's date is {current_date}")
        engine.runAndWait()
    elif "search" in text.lower():
        search_query = text.lower().replace("search","").strip()

        print("Searching for:",search_query)

        engine.say(f"Searching for {search_query}")
        engine.runAndWait()

        webbrowser.open("https://www.google.com/search?q="+search_query)


    else:
       print("Sorry,I don't know that command yet.")
       engine.say("Sorry,I don't know that command yet.")
       engine.runAndWait()

except sr.UnknownValueError:
    print("Sorry,I couldn't understand you.")
    engine.say("Sorry,I couldn't understand you.")
    engine.runAndWait()


except sr.RequestError:
    print("Sorry,there was a problem with the speech service.")
    engine.say("Sorry, there was a problem with the speech service.")
    engine.runAndWait