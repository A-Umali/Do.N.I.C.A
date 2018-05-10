import dispatch


class EventDispatcher:
    def __init__(self):
        self.dispatcher = dispatch
        self.sleep_status = False
        self.active_status = False
