import speech_recognition as sr
import subprocess
import pyautogui
import playsound as ps

resource = sr.Recognizer()

cd = False
tp = False
cnt = 0

while True:
    with sr.Microphone() as source:
        resource.adjust_for_ambient_noise(source)
        audio = resource.listen(source)
        speech = str('nothing')
        try:
            speech = resource.recognize_google(audio)
            speech = speech.lower()

        except:
            speech = 'sorry'
            print('sorry')

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
            if cnt == 1:
                ps.playsound('..//audio//command.mp3')
                # winsound.PlaySound('..//audio//command.mp3', 0)
                cnt = 0

            cmd = speech

            if cmd == 'open browser' or cmd == 'openbrowser':
                subprocess.call(
                    'C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe')
            if cmd == 'open microsoft word':
                subprocess.call(
                    'C://Program Files (x86)//Microsoft Office//root//Office16//WINWORD.EXE')
            if cmd == 'open note' or cmd == 'Open Note':
                subprocess.call('Notepad.exe')
            if cmd == 'new tab' or cmd == 'newtab':
                pyautogui.hotkey('ctrlleft', 't')
            if cmd == 'close' or cmd == 'closed':
                pyautogui.hotkey('ctrlleft', 'w')
            if cmd == 'alter application' or cmd == 'alterapplication':
                pyautogui.keyDown('altleft')
                pyautogui.press('tab')

        if tp == True:
            if cnt == 1:
                ps.playsound('..//audio//typing.mp3')
                cnt = 0
            if speech != 'typing':
                pyautogui.write(' ' + speech)
