from AddonApp import AA
from AddonComment import AC
from DescriptorImage import DI
from AddonGraphcalControl import AGC


class Frame:
    def __init__(self, data_from_frame):
        self.descriptor_image = self._set_DI(data_from_frame)
        self.addon_graphical_control = self._set_AGC(data_from_frame)
        self.addon_comment = self._set_AC(data_from_frame)
        self.addon_app = self._set_AA(data_from_frame)


    def _set_DI(self, data_from_frame):
        start_block = data_from_frame.find(b'\x2c')
        return DI(data_from_frame[start_block:]) if start_block != -1 else None

    def _set_AGC(self, data_from_frame):
        start_block = data_from_frame.find(b'\xf9')
        return AGC(data_from_frame[start_block:start_block+7]) if start_block != -1 else None

    def _set_AC(self, data_from_frame):
        start_block = data_from_frame.find(b'\xfe')
        end_block = data_from_frame.find(b'\x00', start_block+1)
        return AC(data_from_frame[start_block:end_block+1]) if start_block != -1 else None

    def _set_AA(self, data_from_frame):
        start_block = data_from_frame.find(b'\xff')
        end_block = data_from_frame.find(b'\x00', start_block+13)
        return AA(data_from_frame[start_block:end_block+1]) if start_block != -1 else None