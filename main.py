import speech_recognition as sr
import pyttsx3 #python text to speech
import sysop
import sys
import webbrowser
import requests
import musiclibrary
import time 
import search
import weather
import os
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index as needed
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)
newsapi = os.getenv("NEWSAPI_KEY")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    print(f"Processing: {c}")
    c_lower = c.lower()

    if "open google" in c_lower:
        webbrowser.open("https://google.com")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
    elif "stop listening" in c_lower:
        speak("Goodbye sir.")
        sys.exit()
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c_lower:
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c_lower:
        webbrowser.open("https://spotify.com")
    elif c_lower.startswith("play"):
        song = " ".join(c.split(" ")[1:]).strip() # play wolf dsnfkldsf
        link = musiclibrary.music.get(song.lower())
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
    elif "news" in c_lower:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for i, article in enumerate(articles[:10], 1):
                speak