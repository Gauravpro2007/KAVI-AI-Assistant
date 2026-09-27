
"""
KAVI - Knowledgeable Artificial Virtual Intelligence
Version: FINAL 2.0 | Built by Gaurav Raghuvanshi
A Stark-inspired desktop assistant
"""

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import requests
from rich.console import Console
from rich.panel import Panel

console = Console()

# Init TTS
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
except:
    engine = None

def speak(text):
    console.print(f"[bold cyan]KAVI:[/bold cyan] {text}")
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            pass

def wish_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good Morning Sir, KAVI online")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir, KAVI online")
    else:
        speak("Good Evening Sir, KAVI online")
    console.print(Panel("KAVI STARK SYSTEM ONLINE", style="bold green"))

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        console.print("[yellow]Listening...[/yellow]")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
            query = r.recognize_google(audio, language='en-in')
            console.print(f"[bold white]You:[/bold white] {query}")
            return query.lower()
        except:
            return ""

def execute_command(query):
    if not query:
        return True
    
    if 'open google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif 'open youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif 'open github' in query:
        webbrowser.open("https://github.com/Gauravpro2007")
        speak("Opening your GitHub")
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif 'date' in query:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {date}")
    elif 'search' in query:
        search_q = query.replace('search', '').strip()
        webbrowser.open(f"https://google.com/search?q={search_q}")
        speak(f"Searching for {search_q}")
    elif 'play' in query:
        song = query.replace('play', '').strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        speak(f"Playing {song} on YouTube")
    elif 'exit' in query or 'stop' in query or 'offline' in query:
        speak("Going offline Sir, Have a great day")
        return False
    else:
        speak("I didn't catch that, can you repeat?")
    
    return True

def main():
    wish_user()
    speak("How can I help you today?")
    running = True
    while running:
        query = listen()
        running = execute_command(query)

if __name__ == "__main__":
    main()
