import pkgutil
import donica.modules as folder
from donica.encode_speech import Speech


class ModuleRouter(object):
    def __init__(self):
        self.modules = self.get_modules()
        self.speech = Speech()

    @classmethod
    def get_modules(cls):
        location = folder

        modules = []
        for finder, name, ispkg in pkgutil.walk_packages(path=location.__path__,
                                                         prefix=location.__name__+'.'):
            try:
                loader = finder.find_module(name)
                mod = loader.load_module(name)
            except Exception as e:
                raise e
            else:
                if hasattr(mod, 'WORDS'):
                    print('Found module %s with words: %r', name, mod.WORDS)
                    modules.append(mod)
                else:
                    print('Skipping modules because of error')

        modules.sort(key=lambda mods: mod.PRIORITY if hasattr(mods, 'PRIORITY')
                     else 0, reverse=True)
        return modules

    def query(self, texts):
        for module in self.modules:
            for text in texts:
                if module.is_valid(text):
                    try:
                        speaker_msg = module.handle(text)
                        self.speech.send_speak(speaker_msg)
                    except Exception:
                        print('I had trouble with that operation')
                    else:
                        print('Handling of phrase %s by module %s completed', text, module.__name__)
                    finally:
                        return
