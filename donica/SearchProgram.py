import os
import re
import sys
from threading import Thread
from datetime import datetime
from donica.configuration import Config
dict = {}


def get_drives():
    c = Config()
    get_device = c.config.get('DEFAULT', 'DEVICE')
    if re.search('WINDOWS', get_device, re.I):
        response = os.popen("wmic localdisk get caption")
        list_one = []
        for line in response.readlines():
            line = line.strip('\n')
            line = line.strip('\r')
            line = line.strip(' ')
            if line is 'Caption' or line is '':
                continue
            list_one.append(line)
        return list_one


def search_one(drive):
    for root, dir, files in os.walk(drive, topdown=True):
        for file in files:
            file = file.lower()
            if file in dict:
                file = file+'_1'
                dict[file] = root
            else:
                dict[file] = root


def create():
    time_one = datetime.now()
    list_two = []
    list_one = get_drives()
    print(list_one)
    for each in list_one:
        process_one = Thread(target=search_one(), args=(each,))
        process_one.start()
        list_two.append(process_one)

    for t in list_two:
        # Terminates the thread
        t.join()


def final_search():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Use proper format')
    elif sys.argv[1] == '-c':
        create()
    else:
        time_one = datetime.now()
        try:
            pickle_file = open('finder_data', 'r')
        except Exception as e:
            print(e)
