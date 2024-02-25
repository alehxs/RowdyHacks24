from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import speech_recognition as sr

app = Flask(__name__)
socketio = SocketIO(app)

recognizer = sr.Recognizer()

@socketio.on('audio')
def handle_audio(audio):
    try:
        audio_data = audio['data']
        text = recognize_audio(audio_data)
        emit('transcription', {'text': text})
    except Exception as e:
        emit('error', {'message': str(e)})

def recognize_audio(audio_data):
    with sr.AudioData(audio_data) as audio_file:
        text = recognizer.recognize_google(audio_file)
        return text

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
