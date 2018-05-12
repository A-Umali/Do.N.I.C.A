

class Module(object):
    def __init__(self, name, mod_tasks=[], priority=0, greedy=True, enabled=True):
        self.name = name
        self.tasks = mod_tasks
        self.priority = priority
        self.tasks.sort(key=lambda task: task.priority, reverse = True)

        self.greedy = greedy
        self.enabled = enabled

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True
