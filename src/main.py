from vosk import Model, KaldiRecognizer
import pyaudio
import subprocess
import pyautogui
import playsound as ps
import winsound

model = Model("../resources/vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

cd = False
tp = False
cnt = 0

while True:
    data = stream.read(4096)

    if len(data) == 0:
        break

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        speech = text[14:-3]
        print(speech)

        if speech == 'commander':
            cd = True
            tp = False
            cnt = 1
        if speech == 'typing':
            tp = True
            cd = False
            cnt = 1

        if cd == True:
            # if cnt == 1:
            #     ps.playsound('..//audio//command.mp3')
            #     # winsound.PlaySound('..//audio//command.mp3', 0)
            #     cnt = 0

            cmd = text[14:-3]

            if cmd == 'open browser' or cmd == 'openbrowser':
                subprocess.call(
                    'C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe')
            if cmd == 'open microsoft word':
                subprocess.call('C://Program Files (x86)//Microsoft Office//root//Office16//WINWORD.EXE')
            if cmd == 'open note' or cmd == 'opennotepad':
                subprocess.call('Notepad.exe')
            if cmd == 'new' or cmd == 'new':
                pyautogui.hotkey('ctrlleft', 't')
            if cmd == 'close' or cmd == 'closed':
                pyautogui.hotkey('ctrlleft', 'w')
            if cmd == 'switch app' or cmd == 'switchapp':
                pyautogui.hotkey('altleft', 'tab')

        if tp == True:
            # if cnt == 1:
            #     ps.playsound('..//audio//typing.mp3')
            #     cnt = 0
            pyautogui.write(speech)
