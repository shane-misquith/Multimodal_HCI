/*
    Dependencies:

    pip install SpeechRecognition
    pip install pyaudio
*/

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("Voice to text:" + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Audio isn't recognised")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))