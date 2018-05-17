import os
from donica.commands.device.device_type import DeviceType

os.environ["Display"]:'0.0'


class WindowDevice(DeviceType):
    def __init__(self):
        super(WindowDevice, self).__init__(self, device='Windows')