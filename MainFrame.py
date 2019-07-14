from DescriptorLogicScreen import DLS
from Frame import Frame
from Header import Header
from Palette import Palette


class MainFrame:
    def __init__(self, filename):
        with open(filename, 'rb') as f:
            data = f.read()

        self.header = Header(data[:6])
        self.dls = DLS(data[6:13])
        self.global_palette = Palette(data[13:13 + 3 * self.dls.flag_Size], self.dls)
        self.frames = self._set_frames(data[13 + 3 * self.dls.flag_Size:])

    def _set_frames(self, data):
        result = []

        start_frame = 0
        start_image_block = 0
        end_image_block = 0

        def _choose_min(t1, t2, t3):
            if t1 == t2 == t3 == -1:
                return  -1
            return min([x for x in [t1, t2, t3] if x != -1])

        while True:
            start_image_block = data.find(b'\x2c', start_frame)

            if start_image_block == -1:
                break

            t1 = data.find(b'\x21\xf9', start_image_block)
            t2 = data.find(b'\x21\xfe', start_image_block)
            t3 = data.find(b'\x21\xff', start_image_block)
            e1 = _choose_min(t1, t2, t3)
            e2 = data.find(b'\x00\x3b', start_image_block)

            end_image_block = e2 if e1 == -1 else e1

            datas = data[start_frame:end_image_block + 1]
            result.append(Frame(datas))

            start_frame = end_image_block + 1
        return result
