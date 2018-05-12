import pkgutil
import inspect
import traceback

mod_lib = None


def find_mods():
    """ Find and import modules from the module directories """
    global mod_lib
    mod_lib = []
    print('Looking for modules')
    for finder, name, _ in pkgutil.iter_modules('Modules'):
        try:
            mod = finder.find_module(name).load_module(name)
            for member in dir(mod):
                obj = getattr(mod, member)
                if inspect.isclass(obj):
                    for parent in obj.__bases__:
                        if 'Module' is parent.__name__:
                            mod_lib.append(obj())
        except Exception as e:
            print(traceback.format_exc())
    mod_lib.sort(key=lambda mod: mod.priority, reverse=True)


def list_mods():
    """ Print modules in order """
    global mod_lib
    print("Module order: " + str([mod.name for mod in mod_lib])[1:-1]+'\n')


def disable_mod(name):
    """ Attempts to disable the specified mod """
    global mod_lib
    for mod in mod_lib:
        if name in mod.name:
            mod.enabled = False


def enable_mod(name):
    """ Attempts to enable the specified mod """
    global mod_lib
    for mod in mod_lib:
        if name in mod.name:
            mod.enabled = True
