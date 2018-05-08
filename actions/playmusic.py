import os
from os.path import basename
import sys
import random

music_listening = None

WORDS ={
    'play_shuffle':
        {
            'groups':
                [
                    ['party', 'time'],
                    ['party', 'mix']
                ]
        },
    'play_random':
        {
            'groups':
                [
                    ['play', 'music'],
                    'music'
                ]
        },
    'play_specific_music':
        {
            'groups':
                [
                    'play'
                ]
        }
}

def play_shuffle(text):
    try:
        random.shuffle(music_listening)
        for i in range(0, len(music_listening)):
            print("Music")

    except IndexError as e:
        print("No music files found: {0}".format(e))
