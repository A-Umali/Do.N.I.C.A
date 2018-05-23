import pkgutil
import donica.modules as folder


class ModuleRouter(object):
    def __init__(self):
        self.modules = self.get_modules()

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
                if hasattr(mod, 'TITLE'):
                    modules.append(mod)
                else:
                    print('MODULE ROUTER: Skipping modules because of error')
        return modules

    def query(self, titles, message):
        for module in self.modules:
            for title in titles:
                if module.is_valid(title):
                    try:
                        module.handle(message)
                    except Exception:
                        print('MODULE ROUTER: I had trouble with that operation')
                    else:
                        print('MODULE ROUTER: Handling of phrase {} by module {} completed'.format(title,
                                                                                                   module.__name__))
                    finally:
                        return

