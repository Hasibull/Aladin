from vosk import Model, KaldiRecognizer
import pyaudio
import subprocess

model = Model("../resources/vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
while True:
    data = stream.read(4096)

    if len(data) == 0:
        break

    if recognizer.AcceptWaveform(data):
        # print(recognizer.Result())
        text = recognizer.Result()
        print(text[14:-3])
        cmd = text[14:-3]

        if cmd == 'open chrome':
            subprocess.call(
                'C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe')
