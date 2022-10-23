"""Performs unit tests on functions in functions_lib.py"""

import unittest
import os
import sys

sys.path.append('../')

import functions_lib as fl # nopep8

class BaseTestCases:
    class BaseTest(unittest.TestCase):
        def common_test(self):
            x = 4
            self.assertEqual(x, 4)

class TestFunctionsLib(BaseTestCases.BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.test_file_name_lower = "test_file_lower.txt"
        f = open(cls.test_file_name_lower, 'w')

        cls.test_file_list_lower = []
        test_str_lower = ['apple', 'orange', 'strawberry', 'banana', 'kiwi']

        for string in test_str_lower:
            cls.test_file_list_lower.append(string)
            f.write(string + '\n')

        f.close()


        cls.test_file_name_mixed = "test_file_mixed.txt"
        g = open(cls.test_file_name_mixed, 'w')

        cls.test_file_list_mixed = []
        test_str_mixed = ['APPLE', 'ORange', 'strawberry', 'banana',
                              'kiwi']

        for string in test_str_mixed:
            cls.test_file_list_mixed.append(string.lower())
            g.write(string + '\n')

        g.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_file_name_lower)
        os.remove(cls.test_file_name_mixed)

    # test file_reader() function
    def test_file_reader(self):

        # test if file contents converted to list by line
        file_list_lower = fl.file_reader(self.test_file_name_lower)
        self.assertEqual(file_list_lower, self.test_file_list_lower)

        # test if list contains only lowercase characters
        file_list_mixed = fl.file_reader(self.test_file_name_mixed)
        self.assertEqual(file_list_mixed, self.test_file_list_mixed)

        # test if FileNotFoundError raised
        self.assertRaises(FileNotFoundError, fl.file_reader, "test_file.txt")


if __name__ == '__main__':
    unittest.main()
