import struct


class TrinityColor:
    def __init__(self, byte_color):
        self.R = struct.unpack('B', byte_color[0:1])[0]
        self.G = struct.unpack('B', byte_color[1:2])[0]
        self.B = struct.unpack('B', byte_color[2:3])[0]

    def __eq__(self, other):
        return self.R == other.R and self.G == other.G and self.B == other.B

    def get_hex(self):
        s = "#"
        h_R = hex(self.R).replace('0x', '')
        h_G = hex(self.G).replace('0x', '')
        h_B = hex(self.B).replace('0x', '')

        h_R = h_R if len(h_R) == 2 else '0' + h_R
        h_G = h_G if len(h_G) == 2 else '0' + h_G
        h_B = h_B if len(h_B) == 2 else '0' + h_B

        return s + h_R + h_G + h_B

    def __str__(self):
        return "({}, {}, {})".format(self.R, self.G, self.B)
