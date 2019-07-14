class AC:
    def __init__(self, data):
        self.code = data[0:1]
        self.comments = data[1:-1]
        self.end = data[-1:]

