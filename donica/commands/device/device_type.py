

class DeviceType:
    def __init__(self, device, mobile):
        self.device = device
        self.mobile = mobile

    def get_type(self):
        if self.device is 'Windows':
            return self.device
        if self.device is 'Mac OS':
            return self.device