import struct


class Reader_Image:
    def __init__(self, data, LZW_size, colors, width, height):
        self.image_data = self._data_parser(data, LZW_size, colors, width, height)

    def _data_parser(self, data, LZW_size, colors, width, height):
        data_bin_list = self._set_bin_data(data)
        data_bin_big = self._set_data_big(data_bin_list)
        breaked_list_data = self._breaking_data(data_bin_big, LZW_size)
        slovar = self._create_dict(breaked_list_data, colors)
        decoded_data = self._decode_data(breaked_list_data, slovar, width, height)
        return decoded_data

    def _bin(self, byte):
        pre_data = hex(struct.unpack('B', byte)[0])
        r = str(pre_data).split('x')[1][:2]
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

    def _set_bin_data(self, data):
        data_list = []
        for i in range(len(data)):
            data_list.append(self._bin(data[i:i + 1]))
        return data_list

    def _set_data_big(self, data_bin_list):
        data_bin_list.reverse()
        stroke = ""
        for item in data_bin_list:
            stroke += item
        return stroke

    def _breaking_data(self, data_bin_big, LZW_size):
        min_start = LZW_size + 1
        list_data = []
        while len(data_bin_big) > min_start:
            for g in range(2 ** LZW_size):
                sub_data = data_bin_big[-min_start:]
                list_data.append(sub_data)
                data_bin_big = data_bin_big[:-min_start]
            min_start += 1
            LZW_size += 1
        list_data = [int('0b' + x, 2) for x in list_data if x != '']
        return list_data

    def _prepare_breaked_data(self, start_index, old_dict, breaked_list_data):
        for i in range(2, len(breaked_list_data)):
            last_visited = old_dict[breaked_list_data[i - 1]]

            if breaked_list_data[i] in old_dict.keys():
                if old_dict[breaked_list_data[i]] == 'end':
                    break

                current_visited = old_dict[breaked_list_data[i]]
                old_dict[start_index] = last_visited.copy()
                old_dict[start_index].append(current_visited[0])
            else:
                old_dict[start_index] = last_visited.copy()
                old_dict[start_index].append(last_visited[0])
            start_index += 1

        return old_dict

    def _create_dict(self, breaked_list_data, colors):
        result_dict = {}
        i = 0
        while i < len(colors):
            result_dict[i] = [i]
            i += 1
        result_dict[i] = 'clear'
        result_dict[i + 1] = 'end'
        i += 2
        result_dict = self._prepare_breaked_data(i, result_dict, breaked_list_data)

        return result_dict

    def _decode_data(self, breaked_list_data, slovar, width, height):
        decoded_str = ""
        for d in breaked_list_data:
            if slovar[d] == 'end':
                break
            elif slovar[d] == 'clear':
                continue
            for i in slovar[d]:
                decoded_str += str(i)+ " "

        pre_decoded = decoded_str.split(' ')
        decoded_list = []
        h = 0
        for i in range(height):
            l = []
            for j in range(width):
                l.append(int(pre_decoded[h]))
                h += 1
            decoded_list.append(l)

        return decoded_list
