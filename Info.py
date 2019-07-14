from AnalisException import IndexFrameException


class Info:
    def __init__(self, mainframe):
        self.version = mainframe.header.version

        self.width = mainframe.dls.widthLS
        self.height = mainframe.dls.heightLS
        self.palette = mainframe.global_palette
        self.count_color = len(mainframe.global_palette.colors)
        self.frames = mainframe.frames
        self.count_image = len(mainframe.frames)

    def get_info(self):
        return self.version, self.width, self.height, self.count_color, self.count_image

    def get_info_of_frame(self, number_of_frame):

        if number_of_frame < 0 or number_of_frame > self.count_image:
            raise IndexFrameException('Вышли за количество кадров')

        frame = self.frames[number_of_frame]

        description_image = frame.descriptor_image

        left = description_image.left
        top = description_image.top

        width = description_image.widthI
        height = description_image.heightI

        local_palette = description_image.local_palette

        addon_graphical_control = frame.addon_graphical_control
        addon_comment = frame.addon_comment
        addon_app = frame.addon_app

        return left, top, width, height, local_palette, addon_graphical_control, addon_comment, addon_app, description_image
