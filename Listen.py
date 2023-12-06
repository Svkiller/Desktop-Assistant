import speech_recognition as sr
from Speak import Say

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print("Recognizing........")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said : {query}\n")

    except Exception as e:
            print(e)
            # Say("Say that again sir")
            print("Say that again sir")
            return "None"
    return query.lower()
Listen  