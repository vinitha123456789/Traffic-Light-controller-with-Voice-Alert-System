import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Recognized:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Main loop
while True:
    command = recognize_speech()
    if command == "red":
        change_light("red")
    elif command == "yellow":
        change_light("yellow")
    elif command == "green":
        change_light("green")
