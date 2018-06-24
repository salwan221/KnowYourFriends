from time import ctime
from gtts import gTTS
import speech_recognition as sr
import re
import webbrowser
import requests
from pygame import mixer
import json
import time

i = 0


def speak(audio_string):
    global i
    i = i + 1
    print(audio_string)
    tts = gTTS(text=audio_string, lang='en', slow=False)
    tts.save("audio" + str(i) + ".mp3")
    mixer.init()
    mixer.music.load("audio" + str(i) + ".mp3")
    mixer.music.play()


def my_command():
    """listens for commands"""

    r = sr.Recognizer()

    with sr.Microphone(device_index=0, chunk_size=2048, sample_rate=48000) as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = my_command()

    return command


def assistant(command):
    """if statements for executing commands"""

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain +'.com'
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what are you doing' in command:
        speak('Just doing my thing')

    elif 'joke' in command:
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"}
        )
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('oops!I ran out of jokes')

    elif "how are you" in command:
        speak("I am fine")

    elif "hello" in command:
        speak("Hello Mr. Aryaman Mahajan")

    elif "can you do" in command:
        speak("I can answer your questions")

    elif "time" in command:
        speak(ctime())

    else:
        speak("I don't understand")


speak('I am ready for your command')

# loop to continue executing multiple commands
while True:
    assistant(my_command())
