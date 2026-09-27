
import datetime
import webbrowser
import os

def kavi_stark():
    print("=== KAVI STARK v1.0 ===")
    print("Commands: time, open google/youtube/github, search <query>, exit")
    while True:
        cmd = input("\nYou: ").lower()
        if 'time' in cmd:
            print(datetime.datetime.now().strftime("%H:%M:%S"))
        elif 'open google' in cmd:
            webbrowser.open("https://google.com")
        elif 'open youtube' in cmd:
            webbrowser.open("https://youtube.com")
        elif 'search' in cmd:
            q = cmd.replace('search','')
            webbrowser.open(f"https://google.com/search?q={q}")
        elif 'exit' in cmd:
            print("KAVI Offline")
            break

if __name__ == "__main__":
    kavi_stark()
