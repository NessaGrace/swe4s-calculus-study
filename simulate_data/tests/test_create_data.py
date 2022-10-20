import unittest
import os
import sys
import random
import numpy as np
sys.path.append("..")
import file_utils as util #nopep8


class TestCreateData(unittest.TestCase):
    def setUp(self):
        self.samp_size = 200

        # Empty file for testing
        self.empty_file = 'empty_file.txt'
        f_empty = open(self.empty_file, 'w')
        f_empty.close()

        # Half filled file
        self.half_file = 'half_file.txt'
        f_half = open(self.half_file, 'w')
        #for i in range(self.samp_size):
            #f_empty.write('\t')
        f_half.close()

    def test_nonexist_file(self):
        self.assertRaises(FileNotFoundError, util.read_data, 'fake_file.txt')

    def test_empty_file(self):
        self.assertRaises(TypeError, util.read_data, self.empty_file)

    def tearDown(self):
        os.remove(self.empty_file)


if __name__ == '__main__':
    unittest.main()
