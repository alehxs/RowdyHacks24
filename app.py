from flask import Flask
import speech_recognition
import pyttsx3
import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'



def speech_to_text():
    sr = speech_recognition.Recognizer()
    try:
        # Use microphone as audio source
        with speech_recognition.Microphone() as source:
            print("Silence please...")
            # Adjust for ambient noise
            sr.adjust_for_ambient_noise(source, duration=2)
            print("Speak now please... ")
            # Listen to microphone input
            audio = sr.listen(source, timeout=5)

        # Use Google Speech Recognition to transcribe audio to text
        text = sr.recognize_google(audio)
        text = text.lower()

        print("Did you say: " + text)
        return text

    except speech_recognition.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None


@app.route('/speech-to-text', methods=['POST'])
def get_speech_to_text():
    text = speech_to_text()
    return jsonify({'text': text})


if __name__ == '__main__':
    app.run(debug=True)