class NotGifException(Exception):
    """Пользовательский класс исключения: файл не является gif-файлом"""
    pass

class IndexFrameException(Exception):
    """Пользовательский класс исключения: вышли за кол-во кадров"""
    pass