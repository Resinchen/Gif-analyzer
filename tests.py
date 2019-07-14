import unittest

from AddonApp import AA
from AddonComment import AC
from AddonGraphcalControl import AGC
from AnalisException import NotGifException, IndexFrameException
from DescriptorImage import DI
from Info import Info
from MainFrame import MainFrame
from Palette import Palette
from TrinityColor import TrinityColor


class TestGifAnalis(unittest.TestCase):
    def setUp(self):
        self.mf = MainFrame('for Tests/1.gif')
        self.info = Info(self.mf)

    def test_color_print(self):
        c = TrinityColor(b'\xff\xff\xff')
        self.assertEqual(str(c), '(255, 255, 255)')

    def test_check_gif(self):
        with self.assertRaises(NotGifException):
            MainFrame('for Tests/not_gif.txt')

    def test_bin_conv(self):
        byte1 = b'\x00'
        bin_byte1 = self.mf.dls._bin(byte1)

        self.assertEqual(bin_byte1, '00000000')

        byte2 = b'*'
        bin_byte2 = self.mf.dls._bin(byte2)

        self.assertEqual(bin_byte2, '00101010')
        self.assertNotEqual(bin_byte2, '1111')

        byte3 = b'\xff'
        bin_byte3 = self.mf.dls._bin(byte3)

        self.assertEqual(bin_byte3, '11111111')

    def test_set_flags(self):
        byte = b'\x0d'
        flags_byte = self.mf.dls._set_flags(byte)

        self.assertListEqual(flags_byte, ['0', '000', '1', '101'])

    def test_check_num_frame(self):
        count_frames = self.info.count_image
        with self.assertRaises(IndexFrameException):
            self.info.get_info_of_frame(0)
            self.info.get_info_of_frame(count_frames + 1)

    def test_get_info(self):
        answer = (b'GIF89a', 4, 4, 8, 2)
        current = self.info.get_info()
        self.assertTupleEqual(current, answer)

    def test_get_info_of_frame(self):
        answer = (0, 0, 4, 4, None, self.mf.frames[1].addon_graphical_control, None, None)
        current = self.info.get_info_of_frame(1)
        self.assertTupleEqual(current, answer)

    def test_addon_graph_ctrl(self):
        data = b'\xf9\x04\x042\x00\x00\x00'
        
        agc = AGC(data)
        self.assertEqual(agc.code, b'\xf9')

        self.assertEqual(agc.flag_reserve, '000')
        self.assertEqual(agc.flag_method_prepare, '001')
        self.assertEqual(agc.flag_input_user, '0')
        self.assertEqual(agc.flag_transparency_color, '0')

        self.assertEqual(agc.time_await, b'2\x00')
        self.assertEqual(agc.index_transparency_color, b'\x00')
        self.assertEqual(agc.end, b'\x00')

    def test_addon_app(self):
        data = b'\xff\x0bNETSCAPE2.0\x03\x01\x00\x00\x00'
        
        aa = AA(data)
        self.assertEqual(aa.code, b'\xff')
        self.assertEqual(aa.id, b'NETSCAPE')
        self.assertEqual(aa.id_code, b'2.0')
        self.assertEqual(aa.subblock, b'\x03\x01\x00\x00')
        self.assertEqual(aa.end, b'\x00')

    def test_addon_comment(self):
        data = b'\xfe\x04\x042\x00\x00\x00'
      
        ac = AC(data)
        self.assertEqual(ac.code, b'\xfe')
        self.assertEqual(ac.comments, b'\x04\x042\x00\x00')
        self.assertEqual(ac.end, b'\x00')

    def test_local_palette(self):
        data = b',\x00\x00\x00\x00\x04\x00\x04\x00\x82\n\xb2]\xc8\xa6-\xf3\xedc\xba`\xa5\x00\x80\xc8\xf1`"' \
               b'\x00\x00\x00\xff\xff\xff\x03\x08\x08\n\xd2B\x90\x94Y\x12\x00'

        di = DI(data)
        palette = Palette(b'\n\xb2]\xc8\xa6-\xf3\xedc\xba`\xa5\x00\x80\xc8\xf1`"\x00\x00\x00\xff\xff\xff', di)

        self.assertEqual(di.flag_CT, '1')
        self.assertListEqual(di.local_palette.colors, palette.colors)
        self.assertEqual(di.len_cur_block, 8)
        self.assertEqual(di.min_len_LZW, 3)
        self.assertEqual(di.data, b'\x08\n\xd2B\x90\x94Y\x12')


if __name__ == '__main__':
    unittest.main()
