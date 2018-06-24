from time import ctime
from gtts import gTTS
import speech_recognition as sr
import re
import webbrowser
import requests
from pygame import mixer
import json
import time

friend_names_ids = {'Arnav Malhotra': '100000020829231', 'Devanshu Arora': '100000107630051',
                    'Ekjyot Singh': '100000178848732', 'Sanjay Gupta': '100000263223495',
                    'Jaspreet Singh': '100000299399013', 'Siddharth Goel': '100000306570738',
                    'Ankit Shubham': '100000420621649', 'Aham Aggarwal': '100000422439730',
                    'Animesh Agarwal': '100000456922821', 'Abhinav Garg': '100000470714562',
                    'Vinayak Arora': '100000481776995', 'Saurabh Bajaj': '100000482809514',
                    'Vaibhav Singh': '100000508123389', 'Lakshya Sharma': '100000520393060',
                    'Gautam Malhotra': '100000560183020', 'Enayat Jugnu Surjit': '100000562193167',
                    'Chinmaya Garg': '100000566769352', 'Aditya Gupta': '100000646686668',
                    'Ashish Kumar': '100000717785422', 'Ashutosh Sagar': '100000734258867',
                    'Ashutosh Sharma': '100000771613592', 'Lovish Kumar': '100000913523532',
                    'Mukesh Bhatia': '100000951644527', 'Jashan Bawa': '100000953533958',
                    'Ajay Jindal': '100000965274907', 'Anurag Sharma': '100000984778007',
                    'Shaivya Gupta': '100000997743981', 'Vishal Arora': '100001003595977',
                    'Anurag Moudgil': '100001057518359', 'Akhil Gupta': '100001077720266',
                    'Deep Kiran': '100001063225913', 'Anirudh Khandelwal': '100001069366351',
                    'Sarthak Sahu': '100001164068230', 'Abhaykaran Moudgil': '100001187770670',
                    'Abhishek Singh Kumar': '100001214236041', 'Sahil Waraich': '100001221037308',
                    'Mradul Goyal': '100001237394484', 'Bikram Veer': '100001248822973',
                    'Hardik Kaushal': '100001268085406', 'Aayush Wadhwa': '100001322000878',
                    'Anmol Singh': '100001344054049', 'Rajinder Tangri': '100001381166111',
                    'Bharat Chhabra': '100001382611058', 'Jatinder Pal Singh': '100001429900589',
                    'Gurstar Dhillon': '100001445008622', 'Rajpal Arora': '100001462249905',
                    'Ashish Niranjan': '100001482536993', 'Anmol Bajaj': '100001568462161',
                    'Harvinder Dhiman': '100001584105925', 'Aggarwal Virat': '100001606405373',
                    'Arpit Arya': '100001675431078', 'Sagar Vats': '100001686885659', 'Anil Mehta': '100001709375437',
                    'Nikhil Anand': '100001719049505',
                    'Gopi Kular': '100001741851174', 'Anuj Jain': '100001754647175',
                    'Navsharan Singh': '100001815229563', 'Archit Rawat': '100001871918146',
                    'Baljeet Singh': '100001872576620', 'Aaditya Sharma': '100001877738285',
                    'Amit Mangotra': '100001886385188', 'Sunpreet Mann': '100001889756099',
                    'Archit Gaba': '100001922640698', 'Rajbir Singh': '100001951533439',
                    'Dilpreet Bhullar': '100001952794288', 'Himanshu Sharma': '100002077131673',
                    'Ravinder Chadha': '100002102796859', 'Sumit Mahajan': '100002188761330',
                    'Nikhil Bhasin': '100002241507999', 'Aditya Gokhroo': '100002299867177',
                    'Gourav Tangri': '100002313022355', 'Jashan Cheema': '100002387258489',
                    'Ramnish Chaudhary': '100002418901121', 'Mishall Ghotra': '100002452682778',
                    'Bhanu Goyal': '100002483282844', 'Anuj Agarwal': '100002492106880',
                    'Ajay Pachaira': '100002503945659', 'Ankur Varshney': '100002519246982',
                    'Aman Kataria': '100002612252661', 'Kundan Nigam': '100002630547714',
                    'Tekbir Hundal': '100002655879948', 'Shipra Gupta': '100002666901711',
                    'Sarthak Sondhi': '100002731834436', 'Guriqbal Sandhu': '100002800866229',
                    'Angadjot Singh Bhasin': '100002840687250', 'Apoorv Tripathi': '100002867299930',
                    'Ajay Kundu': '100002938710018', 'Amritpal Singh': '100002986721612',
                    'Anshul Salgotra': '100002994604009', 'Abhay Premi': '100003020213987',
                    'Taranjot Kahlon': '100003021006354', 'Anish Aggarwal': '100003106470563',
                    'Shubham Garg': '100003107902415', 'Shubh Kaler': '100003182064060',
                    'Abhi Mahajan': '100003236903000', 'Ankit Garg': '100003284532796',
                    'Dikshit Sharma': '100003301498610', 'Raman Joshi': '100003324551208',
                    'Adit Kr Ishna': '100003566887362', 'Ajay Singh': '100003598437544',
                    'Dhruv Garg': '100003647519194', 'Aniket Dwivedi': '100003653325251',
                    'Nonu Wahi': '100003688274854', 'Anand Prakash Singh': '100003704409060',
                    'Chandan Vanwari': '100003707608536', 'Chandan Sobti': '100003838666713',
                    'Shubham Kumar': '100003982448595', 'Mohit Bansal': '100003992553780',
                    'Bhupesh Soni': '100004172584817', 'Aastha Khatgarh': '100004194228098',
                    'Manbir Singh Mann': '100004292258161', 'Rohit Mehta': '100004424792789',
                    'Mohit Kant': '100004435278077', 'Kunwar Jalsoor Singh': '100004644851646',
                    'Aarti Goyal': '100004769225139', 'Gulshan Gakhar': '100004966598669',
                    'Ishika Matta': '100004977073501', 'Amitpal Singh': '100005010008030',
                    'Davinder Kaur': '100005015737606', 'Harsimran Ahluwalia': '100005166843092',
                    'Jai Deep Maan': '100005192231429', 'Amar Deep': '100005474204577',
                    'Abhishek Singh': '100005664244983', 'Gaurav Dua': '100006130261705',
                    'Sukhpal Singh Gill': '100006282366359', 'Manpreet Johal': '100006337212978',
                    'Asad Tanveer': '100006413610566', 'Shivali Maheshwari': '100006440172183',
                    'Sarvesh Pratap Shahi': '100006522096344', 'Divyansh Jain': '100006766713113',
                    'Manu Goel': '100006782083671', 'Aditya Bisht': '100006981828289', 'Aman Jaswal': 'amanjaswal0006',
                    'Aman Kumar': 'speckyaman', 'Abhimanyu Sharma': 'abhimanyusharmasip', 'Akkshita Nakra': 'Akkshita'}

i = 0


def get_friend_info(fid):
    url = 'https://www.facebook.com/' + fid
    html = requests.get(url)
    html = str(html.content)
    json_data = html.split('<script type="application/ld+json">')

    if len(json_data) > 1:
        json_data = json_data[1]
        json_data = json_data.split('</script>')
        json_data = json_data[0]
        json_object = json.loads(json_data)

        friend_name = json_object['name']
        friend_info = friend_name

        for key in json_object:
            if isinstance(json_object[key], dict):
                for k in json_object[key]:
                    # print(k, json_object[key][k])
                    if k == 'addressLocality':
                        friend_info = friend_info + ' lives in ' + json_object[key][k] + '.'
            elif isinstance(json_object[key], list):
                for obj in json_object[key]:
                    for k in obj:
                        # print(k, obj[k])
                        if k == 'name':
                            friend_info = friend_info + ' associated with ' + obj[k] + '.'
            elif isinstance(json_object[key], str):
                # print(key, json_object[key])
                if key == 'jobTitle':
                    friend_info = friend_info + ' works as '+json_object[key]+'.'

        friend_info = friend_info.lower()

        return friend_info


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
        speak("Hello Mr. Abhishek Salwan")

    elif "can you do" in command:
        speak("I can tell you about your friends")

    elif "time" in command:
        speak(ctime())

    elif 'friends' in command:
        for key in friend_names_ids:
            speak(key)
            time.sleep(1)

    else:
        check = False
        for key in friend_names_ids:
            if key.lower() in command:
                speak(get_friend_info(friend_names_ids[key]))
                check = True
                break

        if not check:
            speak("I don't understand.")


speak('I am ready for your command')

# loop to continue executing multiple commands
while True:
    assistant(my_command())
