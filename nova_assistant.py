import site
import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import subprocess
import time

r = sr.Recognizer()

WAKE_WORD = "nov"
awake = True

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

KNOWN_WEBSITES = [
    "youtube",
    "google",
    "gmail",
    "facebook",
    "instagram",
    "twitter",
    "linkedin"
]

def speak(text):
    print("🔊 Nova says:", text)

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    # Prefer modern voice if available
    voice_id = voices[0].id
    for v in voices:
        if "prabhat" in v.name.lower() :
            voice_id = v.id
            break

    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 190)  # faster, natural

    engine.say(text)
    engine.runAndWait() 
    engine.stop()


def listen():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            print("🎤 Listening...")
            audio = r.listen(source, timeout=4, phrase_time_limit=4)
        text = r.recognize_google(audio).lower()
        print("🗣️ Heard:", text)
        return text
    except:
        return ""


def open_application(app):
    app = app.lower()

    # App aliases (Windows-safe)
    APP_ALIASES = {
        "chrome": "chrome",
        "notepad": "notepad",  
        "calculator": "calc", 
        "calc": "calc",
        "command prompt": "cmd",
        "cmd": "cmd",
        "vs code": "code",
        "vscode": "code"
    }

     # ✅ WhatsApp via URI scheme 
    if app == "whatsapp":
        speak("Opening WhatsApp")
        os.startfile("whatsapp:")
        return True
    # Try alias first
    if app in APP_ALIASES:
        try:
            speak(f"Opening {app}")
            os.startfile(APP_ALIASES[app])
            return True
        except:
            pass

    # Try direct start
    try:
        speak(f"Opening {app}")
        os.startfile(app)      
        return True
    except:
        speak("I cannot find that application")
        return False



def open_website(site):
    if not site.startswith("http"):
        site = "https://" + site

    subprocess.Popen([CHROME_PATH, site])

speak("Good Morning, I am nova. how can I help you today?")

awake = True  # start active

while True:
    command = listen()
    if not command:
        continue

    print("You said:", command)

    # ❌ EXIT
    if any(word in command for word in ["quit", "exit", "stop","close"]):
        speak("Goodbye, Have a nice day!")
        break

    # 💤 SLEEP
    if "sleep" in command:
        speak("Going to sleep")
        awake = False
        continue

    # 🔊 WAKE
    if not awake:
        if WAKE_WORD in command:
            speak("Yes, I am listening")
            awake = True
        continue

    # ⏰ TIME
    if "time" in command:
        speak(f"The time is {datetime.datetime.now().strftime('%H:%M')}")
        continue

    # 📅 DATE
    if "date" in command:
        speak(f"Today is {datetime.datetime.now().strftime('%d %B %Y')}")
        continue

    # 📧 EMAIL
    if "email" in command or "gmail" in command:
        speak("Opening Gmail")
        open_website("https://mail.google.com")
        continue

   # 📂 OPEN APPS / WEBSITES
    if command.startswith("open "):
        target = command.replace("open", "").strip()

        # 🌐 Known websites
        if target in KNOWN_WEBSITES:
            speak(f"Opening {target}")
            open_website(target + ".com")
            continue

        # 🖥️ Applications
        if open_application(target):
            continue

        # 🔍 Fallback to website WITHOUT error message
        speak(f"Opening {target}")
        open_website(target + ".com")
        continue

 # 🔎 QUESTIONS / SEARCH
    if any(q in command for q in ["what", "who", "when", "result", "score"]):
        speak("Here is what I found")
        webbrowser.open(f"https://www.google.com/search?q={command}")
        continue

    # 🤖 FALLBACK
    speak("Here is what I found")
    webbrowser.open(f"https://www.google.com/search?q={command}")
