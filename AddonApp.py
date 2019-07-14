class AA:
    def __init__(self, data):
        self.code = data[0:1]
        self.id = data[2:10]
        self.id_code = data[10:13]
        self.subblock = data[13:-1]
        self.end = data[-1:]


