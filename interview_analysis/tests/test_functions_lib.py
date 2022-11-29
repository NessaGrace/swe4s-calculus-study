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

        # prepare empty file
        cls.empty_file = "empty.txt"
        open(cls.empty_file, 'w').close()

        # prepare second list to filter out
        cls.list_to_filter = ['apple', 'orange']

        # prepare list of sentences
        cls.sentence_list = ['I like pie.', 'I like cake.']

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_file_name_lower)
        os.remove(cls.test_file_name_mixed)
        os.remove(cls.empty_file)
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

        # test if FileNotFoundError, TypeError raised appropriately
        self.assertRaises(FileNotFoundError, fl.file_reader, "test_file.txt")
        self.assertRaises(TypeError, fl.file_reader, 2)
        self.assertRaises(TypeError, fl.file_reader, ["a", "b"])

        # test if error raised for empty file
        self.assertRaises(Exception, fl.file_reader, self.empty_file)

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

        # test error raising for invalid input
        self.assertRaises(TypeError, fl.filter_by_line, "a", ["a", "b"])
        self.assertRaises(TypeError, fl.filter_by_line, 1, [1, 2])
        self.assertRaises(TypeError, fl.filter_by_line, ["a", "b"], 2)

    # test sentence_splitter() function
    def test_sentence_splitter(self):
        sentences_split_fcn = fl.sentence_splitter(self.sentence_list)

        words_list = ['I', 'like', 'pie.', 'I', 'like', 'cake.']

        # test if function successfully splits sentences into words
        self.assertEqual(sentences_split_fcn, words_list)
        # test if new list is no longer equal to list of sentences
        self.assertNotEqual(sentences_split_fcn, self.sentence_list)
        # test that new list has more elements than list of sentences
        self.assertTrue(len(sentences_split_fcn) > len(self.sentence_list))
        self.assertFalse(len(sentences_split_fcn) <= len(self.sentence_list))

        # test error raising for invalid input
        self.assertRaises(TypeError, fl.sentence_splitter, (1, 2))
        self.assertRaises(TypeError, fl.sentence_splitter, "a")
        self.assertRaises(TypeError, fl.sentence_splitter, [1, 2])
        self.assertRaises(TypeError, fl.sentence_splitter, [1, "a"])

    # test remove_punctuation function:
    def test_remove_punctuation(self):
        punc = ["I", "like", "pie,", "but", "I", "like", "s'mores", "better.",
                "I", "love", "strawberries!"]

        no_punc = ["I", "like", "pie", "but", "I", "like", "smores", "better",
                "I", "love", "strawberries"]

        no_punc_fcn = fl.remove_punctuation(punc)

        # test if punctuation is removed successfully
        self.assertEqual(no_punc, no_punc_fcn)
        self.assertNotEqual(punc, no_punc_fcn)

        # test error raising for invalid input
        self.assertRaises(TypeError, fl.remove_punctuation, "ants")
        self.assertRaises(TypeError, fl.remove_punctuation, [1, 2])
        self.assertRaises(TypeError, fl.remove_punctuation, [1, "a"])

    # test compare_files() function:
    def test_compare_files(self):
        # file_list_lower = fl.file_reader(self.test_file_name_lower)
        # file_list_mixed = fl.file_reader(self.test_file_name_mixed)
        list1 = ['ray', 'of', 'light', 'rainbow', 'cloud']
        list2 = ['ray', 'of', 'light', 'sky', 'woods']
        comp_percent = fl.compare_files(list1,
                                        list2)

        percent_sim = (3/5)*100

        self.assertEqual(percent_sim, comp_percent)


if __name__ == '__main__':
    unittest.main()

