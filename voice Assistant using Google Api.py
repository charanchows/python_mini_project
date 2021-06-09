import speech_recognition as sr
import webbrowser
import time
import pyttsx3

sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=5000

speak=pyttsx3.init()
text="hai how can i help u"
speak.say(text)
speak.runAndWait()

print("hey,how can i help u")
time.sleep(0.5)

with sr.Microphone() as source:
    print("try by saying something")
    speak.say("say something")
    speak.runAndWait()
    time.sleep(1)
    audio=r.listen(source)
    time.sleep(0.1)
    try:
        text=r.recognize_google(audio)
        print("You said : {}".format(text))
        url='https://www.google.co.in/search?q='
        search_url=url+text
        webbrowser.open(search_url)
    except:
        print("Can't recognize")
