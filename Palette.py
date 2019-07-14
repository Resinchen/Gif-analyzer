import TrinityColor


class Palette:
    def __init__(self, data_of_palette, dls):
        self.colors = self._set_colors_table(data_of_palette, dls)

    def _set_colors_table(self, data, dls):
        colors = []

        for i in range(0, 3*dls.flag_Size, 3):
            colors.append(TrinityColor.TrinityColor(data[i:i+3]))

        return colors

    def __len__(self):
        return len(self.colors)
