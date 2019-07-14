from tkinter.filedialog import *

from Info import Info
from MainFrame import MainFrame
from Reader_Image import Reader_Image


class Window:
    def __init__(self):
        self.init_UI()

    def init_UI(self):
        self.root = Tk()
        self.root.title('Gif analise')
        self.root.geometry("300x300+300+300")

        # Кнопка файлового диалога
        self.btn_file_dialog = Button(self.root, text='Выбрать файл', command=self.read_file)
        self.btn_file_dialog.pack()

        # Кнопка начала анализа
        self.btn_analyse = Button(self.root, text='Анализировать', command=self.show_analyse)
        self.btn_analyse.pack()

        # Поле вывода пути
        self.ent_path = Entry(self.root, width=40)
        self.ent_path.pack()

        # Поле ввода номера кадра
        self.ent_num_frame = Entry(self.root, width=2)
        self.ent_num_frame.pack()

        # Кнопка вывода инфы о кадре
        self.btn_show_info_of_frame = Button(self.root, text='Показать информацию о кадре', command=self.show)
        self.btn_show_info_of_frame.pack()

        self.str_var = StringVar()
        self.str_var.set('')

        # Основная информация о гифке
        lbl = Label(self.root, textvariable=self.str_var, fg='red', font=('Helvetica', 12),
                    relief=RIDGE, width=100, height=100, bd=5)
        lbl.pack()

        self.root.mainloop()

    def read_file(self):
        self.ent_path.delete(0, END)
        op = askopenfilename()
        self.ent_path.insert(INSERT, op)

    def show_analyse(self):
        filename = self.ent_path.get()
        self.mf = MainFrame(filename)
        self.info = Info(self.mf)
        self.common_info = self.info.get_info()
        self.str_var.set(self.set_common_info(self.common_info[0], self.common_info[1],
                                              self.common_info[2], self.common_info[3], self.common_info[4]))

    def set_common_info(self, version='', width='', height='', count_color='', count_frames=''):
        string = "версия: {}\n" \
                 "ширина: {} px\n" \
                 "высота: {} px\n" \
                 "кол-во цветов: {}\n" \
                 "кол-во кадров: {}"
        return string.format(version, width, height, count_color, count_frames)

    def show(self):
        num_frame = int(self.ent_num_frame.get())
        FrameWindow(self.root, num_frame, self.info)


class FrameWindow:
    def __init__(self, master, number_frame, info):
        self.init_UI(master, number_frame, info)

    def init_UI(self, master, number_frame, info):
        self.info = info
        self.info_of_frame = self.info.get_info_of_frame(number_frame - 1)

        self.frame_info = StringVar()
        self.frame_info.set(self._set_frame_info(self.info_of_frame[0], self.info_of_frame[1], self.info_of_frame[2],
                                                 self.info_of_frame[3], self.info_of_frame[4], self.info_of_frame[5],
                                                 self.info_of_frame[6], self.info_of_frame[7]))

        self.curent_frame_info = Toplevel(master)
        self.curent_frame_info.title("frame № {}".format(number_frame))
        self.curent_frame_info.geometry("400x300+700+300")

        btn_image = Button(self.curent_frame_info, text='Показать кадр', command=self.show_frame)
        btn_image.pack()

        label = Label(self.curent_frame_info, textvariable=self.frame_info, fg='red', font=('Helvetica', 12),
                      width=300, height=300)
        label.pack()

    def show_frame(self):
        palette = self.info_of_frame[4] if self.info_of_frame[4] is not None else self.info.palette
        ImageWindow(self.curent_frame_info, self.info_of_frame[2], self.info_of_frame[3], palette,  self.info_of_frame[8])

    def _set_frame_info(self, left='', top='', width='', height='', local_palette='', agc='', ac='', aa=''):
        string = 'Позиция на эране:\n' \
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

        local_palette = 'Нет' if local_palette is None else 'Есть'
        agc = 'Нет' if agc is None else 'Есть'
        ac = 'Нет' if ac is None else 'Есть'
        aa = 'Нет' if aa is None else 'Есть'

        return string.format(left, top, width, height, local_palette, agc, ac, aa)


class ImageWindow:
    def __init__(self, master, width, height, palette, descriptor_image):
        self.init_UI(master, width, height, palette, descriptor_image)

    def init_UI(self, master, width, height, palette, descriptor_image):

        image = Reader_Image(descriptor_image.data, descriptor_image.min_len_LZW, palette, width, height)

        self.curent_frame_image = Toplevel(master)
        self.curent_frame_image.geometry("{}x{}+700+300".format(width+20, height+20))

        canvas = Canvas(self.curent_frame_image, width=width+10, height=height+10)
        canvas.pack()
        for i in range(width):
            for j in range(height):
                color = palette.colors[image.image_data[j][i]].get_hex()
                canvas.create_oval(i, j, i, j, width=0, fill=color)

