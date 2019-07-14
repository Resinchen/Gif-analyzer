import struct


class AGC:
    def __init__(self, data):
        self.code = data[0:1]

        _flags = self._set_flags(data[2:3])
        self.flag_reserve = _flags[0]
        self.flag_method_prepare = _flags[1]
        self.flag_input_user = _flags[2]
        self.flag_transparency_color = _flags[3]

        self.time_await = data[3:5]
        self.index_transparency_color = data[5:6]
        self.end = data[6:7]

    def _set_flags(self, data):
        pre_data = hex(struct.unpack('B', data)[0])
        str = self._bin(pre_data)
        flags = [str[:3], str[3:6], str[6:7], str[7:8]]
        return flags

    def _bin(self, byte):
        r = str(byte).split('x')[1][:2]
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