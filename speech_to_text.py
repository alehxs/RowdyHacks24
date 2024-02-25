#necessary imports
import speech_recognition
import pyttsx3

sr = speech_recognition.Recognizer()


with speech_recognition.Microphone() as source2:

    print(" Silence please")

    sr.adjust_for_ambient_noise(source2, duration = 2)

    print(" Speak now please... ")

    audio2 = sr.listen(source2,timeout=5)

    try:
        textt = sr.recognize_google(audio2)
        extt = textt.lower()

        print(" Did you say :- " + textt)

    except speech_recognition.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
