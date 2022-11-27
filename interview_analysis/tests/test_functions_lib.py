"""Performs unit tests on functions in functions_lib.py

    * test_file_reader - tests functions_lib.file_reader()
"""

import unittest
import os
import sys

sys.path.append('../')

import functions_lib as fl  # nopep8


# establish base test case wrapper
class BaseTestCases:
    class BaseTest(unittest.TestCase):
        def common_test(self):
            x = 4
            self.assertEqual(x, 4)


# begin testing from functions_lib.py
class TestFunctionsLib(BaseTestCases.BaseTest):

    @classmethod
    def setUpClass(cls):
        # prepare file with all lowercase contents
        cls.test_file_name_lower = "test_file_lower.txt"
        f = open(cls.test_file_name_lower, 'w')

        cls.test_file_list_lower = []
        cls.test_str_lower = ['apple', 'orange', 'strawberry', 'banana', 'kiwi']

        for string in cls.test_str_lower:
            cls.test_file_list_lower.append(string)
            f.write(string + '\n')

        f.close()

        # prepare file with upper and lower case
        cls.test_file_name_mixed = "test_file_mixed.txt"
        g = open(cls.test_file_name_mixed, 'w')

        cls.test_file_list_mixed = []
        cls.test_str_mixed = ['APPLE', 'ORange', 'strawberry', 'banana',
                          'kiwi']

        for string in cls.test_str_mixed:
            cls.test_file_list_mixed.append(string.lower())
            g.write(string + '\n')

        g.close()

        # prepare second list to filter out
        cls.list_to_filter = ['apple', 'orange']

        # prepare list of sentences
        cls.sentence_list = ['I like pie.', 'I like cake.']

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_file_name_lower)
        os.remove(cls.test_file_name_mixed)
        cls.list_to_filter = None
        cls.sentence_list = None

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
        self.assertRaises(TypeError, fl.file_reader, 2)
        self.assertRaises(TypeError, fl.file_reader, ["a", "b"])

    # test filter_by_line() function
    def test_filter_by_line(self):
        filtered_list_fcn = fl.filter_by_line(self.test_str_lower,
                                           self.list_to_filter)

        filtered_list_test = ['strawberry', 'banana', 'kiwi']

        # test if list filtered by function matches expected output
        self.assertEqual(filtered_list_fcn, filtered_list_test)
        # test if length of filtered list matches expected list length
        self.assertEqual(len(filtered_list_fcn), len(filtered_list_test))
        # test negative assertion
        self.assertNotEqual(self.test_str_lower, filtered_list_fcn)
        # test if length of filtered list less than length of original list
        self.assertTrue(len(filtered_list_fcn) < len(self.test_str_lower))
        self.assertFalse(len(filtered_list_fcn) > len(self.test_str_lower))
        self.assertFalse(len(filtered_list_fcn) == len(self.test_str_lower))

        # test error raising
        self.assertRaises(TypeError, fl.filter_by_line, "a", ["a", "b"])
        self.assertRaises(TypeError, fl.filter_by_line, 1, [1, 2])
        self.assertRaises(TypeError, fl.filter_by_line, ["a", "b"], 2)

    # test sentence_splitter() function
    def test_sentence_splitter(self):
        sentences_split_fcn = fl.sentence_splitter(self.sentence_list)

        words_list = ['I', 'like', 'pie.', 'I', 'like', 'cake.']

        # test if function successfully splits sentences into words
        self.assertEqual(sentences_split_fcn, words_list)


if __name__ == '__main__':
    unittest.main()
