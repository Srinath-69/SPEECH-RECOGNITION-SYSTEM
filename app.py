import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Please Speak Anything...")
            r.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = r.listen(source, timeout=10, phrase_time_limit=10)  # Listen with a timeout

            text = r.recognize_google(audio)
            text = text.title()  # Capitalize the first letter of each word

            print(f"Recognized_Text_From_Speech : {text}")
            break  # Exit the loop after recognizing the voice

    except sr.UnknownValueError:
        print("Sorry, Didn't Recognize Anything.")
        r = sr.Recognizer()
        continue
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        break
