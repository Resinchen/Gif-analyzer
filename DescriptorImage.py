import struct

from Palette import Palette


class DI:
    def __init__(self, data):
        self.code = data[0:1]
        self.left = struct.unpack('H', data[1:3])[0]
        self.top = struct.unpack('H', data[3:5])[0]
        self.widthI = struct.unpack('H', data[5:7])[0]
        self.heightI = struct.unpack('H', data[7:9])[0]

        _flags = self._set_flags(data[9:10])
        self.flag_CT = _flags[0]
        self.flag_I = _flags[1]
        self.flag_SF = _flags[2]
        self.flag_Size = self._set_Size(_flags[3])

        self.local_palette = self._set_local_palette(data[10:10 + 3 * self.flag_Size])

        if self.local_palette is None:
            self.min_len_LZW = struct.unpack('B', data[10:11])[0]
            self.len_cur_block = struct.unpack('B', data[11:12])[0]
            self.data = data[12:12 + self.len_cur_block]

        else:
            self.min_len_LZW = struct.unpack('B', data[10 + 3 * self.flag_Size:11 + 3 * self.flag_Size])[0]
            self.len_cur_block = struct.unpack('B', data[11 + 3 * self.flag_Size:12 + 3 * self.flag_Size])[0]
            self.data = data[12 + 3 * self.flag_Size:12 + 3 * self.flag_Size + self.len_cur_block]

    def _set_Size(self, flag):
        size_palette = {'000': 2, '001': 4,
                        '010': 8, '011': 16,
                        '100': 32, '101': 64,
                        '110': 128, '111': 256}
        return size_palette[flag]

    def _set_flags(self, data):
        str = self._bin(data)
        flags = [str[:1], str[1:2], str[2:3], str[5:8]]
        return flags

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

    def _set_local_palette(self, data_from_palette):
        if self.flag_CT == '1':
            return Palette(data_from_palette, self)
        else:
            return None
