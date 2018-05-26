import re
import os
import subprocess
from threading import Thread
import _pickle
from donica.encode_speech import Speech

TITLE = ['OPEN-PROGRAM']


def handle(title, message):
    # Hackish way to find the program name, so I will change it on a later date
    speak = Speech()
    filtered_words = ['please', 'open', 'up', 'you', 'this', 'that', 'there', 'sorry', 'can', 'how', 'about', 'hello',
                      'hi', 'howdy', 'what', 'is', 'okay', 'ok', 'donica']
    find_name = [''.join([f for f in l.split() if not f in filtered_words]) for l in [message]]
    program = ''.join(find_name)
    if os.path.exists(os.path.abspath("finder_data")):
        file = open(os.path.abspath("finder_data"), "rb")
        file_dict = _pickle.load(file)
        file.close()
        file_search = (program + '.exe').lower()
        list = []
        print('Finding Path')
        for key in file_dict:
            if re.fullmatch(file_search, key):
                found_file = file_dict[key] + "\\" + key
                list.append(found_file)
        speak.send_speak('Opening {}'.format(program))
        open_file = "".join(list)
        print(open_file)
        subprocess.Popen(open_file)
    else:
        speak.send_speak('I have not looked through your drives yet, I am going to do that right now'
                         'so next time will be faster. Thank you for being patient')
        create()


def is_valid(title):
    return bool(re.search('command.open.program', title, re.I))


dict1 = {}


def get_drives():
    response = os.popen("wmic logicaldisk get caption")
    list1 = []
    for line in response.readlines():
        line = line.strip('\n')
        line = line.strip('\r')
        line = line.strip(' ')
        if line == "Caption" or line == "":
            continue
        list1.append(line)
    return list1


def search1(drive):
    for root, dir, files in os.walk(drive, topdown=True):
        for file in files:
            file = file.lower()
            if file in dict1:
                file = file + '_1'
                dict1[file] = root
            else:
                dict1[file] = root


def create():
    list2 = []
    list1 = get_drives()
    for each in list1:
        process1 = Thread(target=search1, args=(each,))
        process1.start()
        list2.append(process1)
    for process1 in list2:
        process1.join()
    try:
        with open(os.path.abspath("finder_data"), "wb") as pickle_file:
            _pickle.dump(dict1, pickle_file)
            pickle_file.close()
    except Exception as e:
        raise e
