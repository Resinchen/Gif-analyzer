import struct


class DLS:
    def __init__(self, data):
        self.widthLS = struct.unpack('H', data[0:2])[0]
        self.heightLS = struct.unpack('H', data[2:4])[0]


        _flags = self._set_flags(data[4:5])
        self.flag_CT = _flags[0]
        self.flag_Color = self._set_Color(_flags[1])
        self.flag_SF = _flags[2]
        self.flag_Size = self._set_Size(_flags[3])

        self.backGround = struct.unpack('B', data[5:6])
        self.resolution = struct.unpack('B', data[6:7])

    def _set_flags(self, data):
        str = self._bin(data)
        flags = [str[:1], str[1:4], str[4:5], str[5:8]]
        return flags

    def _set_Color(self, flag):
        color_count = {'000': 8, '001': 64,
                       '010': 512, '011': 4096,
                       '100': 32768, '101': 262144,
                       '110': 2097152, '111': 16777216}
        return color_count[flag]

    def _set_Size(self, flag):
        size_palette = {'000': 2, '001': 4,
                        '010': 8, '011': 16,
                        '100': 32, '101': 64,
                        '110': 128, '111': 256}
        return size_palette[flag]

    def _bin(self, byte):
        pre_data = hex(struct.unpack('B', byte)[0])
        r = str(pre_data).split('x')[1][:2]
        if len(r) == 1:
            r = '0' + r
        d = {'0': '0000', '1': '0001',
             '2': '0010', '3': '0011',
             '4': '0100', '5': '0101',
             '6': '0110', '7': '0111',
             '8': '1000', '9': '1001',
             'a': '1010', 'b': '1011',
             'c': '1100', 'd': '1101',
             'e': '1110', 'f': '1111'}
        s = ''
        for a in r:
            s += d[a]
        return s
