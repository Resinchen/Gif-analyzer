from AnalisException import NotGifException


class Header:
    def __init__(self, data):
        self.version = data[0:6]
        if self.version != b'GIF89a' and self.version != b'GIF87a':
            raise NotGifException('Это не gif')
