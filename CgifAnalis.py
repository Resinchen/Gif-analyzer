import argparse

from Info import Info
from MainFrame import MainFrame


def parser_args():
    parser = argparse.ArgumentParser(description="Разбирает формат .gif")
    parser.add_argument('inFilename', type=str, help='Имя входного gif-файла ')
    return parser.parse_args()


def print_result(main_frame):
    info = Info(main_frame)
    string = "версия: {}\n" \
             "ширина: {} px\n" \
             "высота: {} px\n" \
             "кол-во цветов: {}\n" \
             "кол-во кадров: {}".format(info.version, info.width, info.height, info.count_color, info.count_image)
    print(string)
    print()

    while True:
        num = input()
        print()

        if num == '':
            break
        
        info_frame = info.get_info_of_frame(int(num) - 1)

        stroke = 'Позиция на эране:\n' \
                 'Слева: {} px\n' \
                 'Сверху: {} px\n' \
                 '\n' \
                 'Размер:\n' \
                 'Ширина: {} px\n' \
                 'Высота: {} px\n' \
                 '\n' \
                 'Локальная палитра - {}\n' \
                 'Расширение графического контроля - {}\n' \
                 'Расширение коментариев - {}\n' \
                 'Расширение приложения - {}\n'

        local_palette = 'Нет' if info_frame[4] is None else 'Есть'
        agc = 'Нет' if info_frame[5] is None else 'Есть'
        ac = 'Нет' if info_frame[6] is None else 'Есть'
        aa = 'Нет' if info_frame[7] is None else 'Есть'

        s = stroke.format(info_frame[0], info_frame[1], info_frame[2], info_frame[3], local_palette, agc, ac, aa)

        print(s)


def main():
    args = parser_args()
    filename = args.inFilename
    mf = MainFrame(filename)
    print_result(mf)


if __name__ == '__main__':
    main()
