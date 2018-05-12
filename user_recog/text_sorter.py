from Configure import config
from text_speech.Speech import Speech
import donica
import re
from Modules import mods

# Looking for keywords from modules

matched_mods = None

def analyze_speech(responses):
    Speech.speak(responses)
    print(responses)


def run_mods(responses):
    match_mods(responses)
    execute_mods(responses)


def mod_select(mods):
    """ Prompt user to specify which module to use to respond """
    print('\n~ Which module (greedy) would you like me to use to respond?')
    print('~ Choices: '+str([mod.name for mod in mods])[1:-1]+'\n')
    mod_select = input('> ')

    for mod in mods:
        if re.search('^.*\\b'+mod.name+'\\b.*$',  mod_select, re.IGNORECASE):
            return mod
    print('No module name found.')


def match_mods(text):
    """ Attempts to match a modules and their tasks """
    matched_mods = []
    for mod in mods.mod_lib:
        if not mod.enabled:
            continue
        """ Find matched tasks and add to module's task queue """
        mod.task_queue = []
        for task in mod.tasks:
            if task.match(text):
                mod.task_queue.append(task)
                if task.greedy:
                    break

        """ Add modules with matched tasks to list """
        if len(mod.task_queue):
            matched_mods.append(mod)


def execute_mods(text):
    """ Executes the modules in prioritized order """
    if len(matched_mods) <= 0:
        Speech.speak('No modules found')
        return

    matched_mods.sort(key=lambda mod: mod.priority, reverse=True)

    normal_mods = []
    greedy_mods = []
    greedy_flag = False
    priority = 0
    for mod in matched_mods:
        if greedy_flag and mod.priority < priority:
            break
        if mod.greedy:
            greedy_mods.append(mod)
            greedy_flag = True
            priority = mod.priority
        else:
            normal_mods.append(mod)

    if len(greedy_mods) is 1:
        normal_mods.append(greedy_mods[0])
    elif len(greedy_mods) > 1:
        if 0 < len(normal_mods):
            print('\n~ Matched mods (non-greedy): '+str([mod.name for mod in normal_mods])[1:-1]+'\n')
        m = mod_select(greedy_mods)
        if not m:
            return
        normal_mods.append(m)
    for mod in normal_mods:
        execute_tasks(mod, text)

def execute_tasks(self, mod, text):
        """ Executes a module's task queue """
        return
    normal_mods.append(m)
    for mod in normal_mods:
        execute_tasks(mod, text)


