import unittest
import os
import sys
import random
import numpy as np
import pdb
sys.path.append("..")
import file_utils as util #nopep8


class TestCreateData(unittest.TestCase):
    def setUp(self):
        self.samp_size = 200

        # Empty file for testing
        self.empty_file = 'empty_file.txt'
        f_empty = open(self.empty_file, 'w')
        f_empty.close()

        # File with empty line in middle
        self.mid_file = 'mid_file.txt'
        f_mid = open(self.mid_file, 'w')
        for i in range(int(self.samp_size/2)):
            f_mid.write('something \t something \n')
        f_mid.write('\n')
        for i in range(int(self.samp_size/2-1)):
            f_mid.write('something \t something \n')
        f_mid.close()

    # Check error when input parameter file path does not exist    
    def test_nonexist_file(self):
        self.assertRaises(FileNotFoundError, util.read_data, 'fake_file.txt')

    # Check error when input parameter file is blank
    def test_empty_file(self):
        self.assertRaises(TypeError, util.read_data, self.empty_file)

    # Check error when blank line exists in middle of file
    def test_mid_file(self):
        self.assertRaises(IndexError, util.read_data, self.mid_file)

    def test_probability_summing(self):
        probability = [0.5, 0.5]
        r = util.check_sum(probability)
        self.assertEqual(r, 1)

    def tearDown(self):
        os.remove(self.empty_file)
        os.remove(self.mid_file)


if __name__ == '__main__':
    unittest.main()
