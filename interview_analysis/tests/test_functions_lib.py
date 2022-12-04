"""Performs unit tests on functions in functions_lib.py

    * test_file_reader - tests fl.file_reader()
    * test_filter_by_line - tests fl.filter_by_line()
    * test_sentence_splitter - tests fl.sentence_splitter()
    * test_remove_punctuation - tests fl.remove_punctuation()
    * test_word_counter - tests fl.word_counter()
    * test_compare_files - tests fl.compare_files()
"""

import unittest
import os
import sys
from string import ascii_letters, punctuation, ascii_lowercase
import random

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
        cls.test_str_lower = ['apple', 'orange', 'strawberry', 'banana',
                              'kiwi']

        for element in cls.test_str_lower:
            cls.test_file_list_lower.append(element)
            f.write(element + '\n')

        f.close()

        # prepare file with upper and lower case
        cls.test_file_name_mixed = "test_file_mixed.txt"
        g = open(cls.test_file_name_mixed, 'w')

        cls.test_file_list_mixed = []
        cls.test_str_mixed = ['APPLE', 'ORange', 'strawberry', 'banana',
                              'kiwi']

        for element in cls.test_str_mixed:
            cls.test_file_list_mixed.append(element.lower())
            g.write(element + '\n')

        g.close()

        # prepare file with random strings
        cls.test_file_name_random = "test_file_random.txt"
        g = open(cls.test_file_name_random, 'w')

        cls.test_file_list_random = []

        cls.test_str_rand = []
        for i in range(5):
            cls.test_str_rand.append(''.join(
                random.choices(ascii_letters, k=8)))

        for element in cls.test_str_rand:
            cls.test_file_list_random.append(element.lower())
            g.write(element + '\n')

        g.close()

        # prepare empty file
        cls.empty_file = "empty.txt"
        open(cls.empty_file, 'w').close()

        # prepare second list to filter out
        cls.list_to_filter = ['apple', 'orange']

        # prepare random list to filter out
        cls.rand_list_filter = [cls.test_str_rand[0], cls.test_str_rand[1]]

        # prepare list of sentences
        cls.sentence_list = ['I like pie.', 'I like cake.']

        # prepare random list of multi-word strings
        cls.ran1 = ''.join(random.choices(ascii_letters, k=8))
        cls.ran2 = ''.join(random.choices(ascii_letters, k=8))
        cls.ran3 = ''.join(random.choices(ascii_letters, k=8))
        cls.ran4 = ''.join(random.choices(ascii_letters, k=8))
        cls.mult_rand = [cls.ran1 + " " + cls.ran2, cls.ran3 + " " + cls.ran4]

        # prepare lists of strings with punctuation
        cls.punc1 = ["I", "like", "pie,", "but", "I", "like", "s'mores",
                     "better.", "I", "love", "strawberries!"]
        cls.punc2 = ["hi", "'", ".", ",", "?", "!", ":", ";", "-", "[", "]",
                     "(", ")", "{", "}", "$", "%", "#", "@", '"', "/", "+",
                     "="]

        # prepare random list of strings with punctuation
        cls.punc_rand = []
        for i in range(5):
            cls.punc_rand.append(''.join(
                random.choices(punctuation, k=8)))

        # prepare lists to test word_counter()
        cls.word_list = ["sing", "piano", "musical", "theater", "rock",
                         "classical", "music", "song", "songs", "play"]
        cls.search_list = ["i", "love", "to", "sing", "i", "play", "piano",
                           "too", "but", "i", "like", "to", "sing", "better",
                           "i", "love", "to", "sing", "musical", "theater",
                           "most", "rock", "is", "fun", "to", "sing", "too",
                           "bohemian", "rhapsody", "is", "one", "of", "my",
                           "favorite", "songs", "and", "queen", "is", "my",
                           "favorite", "band"]

        # prepare random lists to test word_counter()
        cls.rand_words = [cls.ran1, cls.ran2, cls.ran3, cls.ran4]
        cls.rand_search = [cls.ran1, cls.ran2, cls.ran3, cls.ran4, cls.ran1]

        # prepare lists to test compare_files()
        cls.comp_list1 = ['ray', 'of', 'light', 'rainbow', 'cloud']
        cls.comp_list2 = ['ray', 'of', 'light', 'sky', 'woods']

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_file_name_lower)
        os.remove(cls.test_file_name_mixed)
        os.remove(cls.test_file_name_random)
        os.remove(cls.empty_file)
        cls.test_file_list_lower = None
        cls.test_str_lower = None
        cls.test_file_list_mixed = None
        cls.test_str_mixed = None
        cls.test_file_list_random = None
        cls.test_str_rand = None
        cls.list_to_filter = None
        cls.rand_list_filter = None
        cls.sentence_list = None
        cls.ran1 = None
        cls.ran2 = None
        cls.ran3 = None
        cls.ran4 = None
        cls.mult_rand = None
        cls.punc1 = None
        cls.punc2 = None
        cls.punc_rand = None
        cls.word_list = None
        cls.search_list = None
        cls.rand_words = None
        cls.rand_search = None
        cls.comp_list1 = None
        cls.comp_list2 = None

    # test file_reader() function
    def test_file_reader(self):

        # test if file contents converted to list by line
        file_list_lower = fl.file_reader(self.test_file_name_lower)
        self.assertEqual(file_list_lower, self.test_file_list_lower)
        self.assertNotEqual(file_list_lower, self.test_str_mixed)

        # test if list contains only lowercase characters
        file_list_mixed = fl.file_reader(self.test_file_name_mixed)
        self.assertEqual(file_list_mixed, self.test_file_list_mixed)

        # test function for file of random strings
        file_list_rand = fl.file_reader(self.test_file_name_random)
        self.assertEqual(file_list_rand, self.test_file_list_random)

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

        # test if function works with randomness
        filtered_rand = fl.filter_by_line(self.test_str_rand,
                                          self.rand_list_filter)
        test_rand_filt = [self.test_str_rand[2],
                          self.test_str_rand[3],
                          self.test_str_rand[4]]
        self.assertEqual(filtered_rand, test_rand_filt)

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

        # test function with randomness
        sen_split_rand_fcn = fl.sentence_splitter(self.mult_rand)
        sen_split_rand_test = [self.ran1, self.ran2, self.ran3, self.ran4]
        self.assertEqual(sen_split_rand_fcn, sen_split_rand_test)

        # test error raising for invalid input
        self.assertRaises(TypeError, fl.sentence_splitter, (1, 2))
        self.assertRaises(TypeError, fl.sentence_splitter, "a")
        self.assertRaises(TypeError, fl.sentence_splitter, [1, 2])
        self.assertRaises(TypeError, fl.sentence_splitter, [1, "a"])

    # test remove_punctuation() function
    def test_remove_punctuation(self):
        no_punc1 = ["I", "like", "pie", "but", "I", "like", "smores",
                    "better", "I", "love", "strawberries"]

        no_punc1_fcn = fl.remove_punctuation(self.punc1)

        no_punc2 = ["hi", "", "", "", "", "", "", "", "", "", "",
                    "", "", "", "", "", "", "", "", '', "", "",
                    ""]

        no_punc2_fcn = fl.remove_punctuation(self.punc2)

        # test if punctuation is removed successfully
        self.assertEqual(no_punc1, no_punc1_fcn)
        self.assertNotEqual(self.punc1, no_punc1_fcn)

        # more comprehensive example with all punctuation types
        self.assertEqual(no_punc2, no_punc2_fcn)
        self.assertNotEqual(no_punc2_fcn, self.punc2)

        # test with randomness
        no_punc_rand_fcn = fl.remove_punctuation(self.punc_rand)
        no_punc_rand_test = ['', '', '', '', '']
        self.assertEqual(no_punc_rand_fcn, no_punc_rand_test)

        # test error raising for invalid input
        self.assertRaises(TypeError, fl.remove_punctuation, "ants")
        self.assertRaises(TypeError, fl.remove_punctuation, [1, 2])
        self.assertRaises(TypeError, fl.remove_punctuation, [1, "a"])

    # test word_counter() function
    def test_word_counter(self):
        word_count_fcn = fl.word_counter(self.word_list, self.search_list)
        word_count_test = {'sing': 4, 'play': 1, 'piano': 1, 'musical': 1,
                           'theater': 1, 'rock': 1, 'songs': 1}
        word_count_test2 = {'sing': 4, 'piano': 1, 'musical': 1, 'theater': 1,
                            'rock': 1}

        # test if function outputs correct word counts
        self.assertEqual(word_count_fcn, word_count_test)
        self.assertNotEqual(word_count_fcn, word_count_test2)

        # test if size of dictionaries are the same
        self.assertEqual(len(word_count_fcn), len(word_count_test))

        # test if type is dictionary
        self.assertEqual(type(word_count_fcn), type(word_count_test))

        # test with randomness
        word_count_rand_fcn = fl.word_counter(self.rand_words,
                                              self.rand_search)
        word_count_rand_test = {self.ran1: 2,
                                self.ran2: 1,
                                self.ran3: 1,
                                self.ran4: 1}
        self.assertEqual(word_count_rand_fcn, word_count_rand_test)

        # test if errors for invalid input raised correctly
        self.assertRaises(TypeError, fl.word_counter, ["ab", "cd"], "ab")
        self.assertRaises(TypeError, fl.word_counter, "ab", "cd")
        self.assertRaises(TypeError, fl.word_counter, "cd", ["ab", "cd"])
        self.assertRaises(TypeError, fl.word_counter, ["ab", "cd"], 1)
        self.assertRaises(TypeError, fl.word_counter, 2, ["ef", "gh"])

    # test compare_files() function (still in development):
    def test_compare_files(self):
        comp_percent = fl.compare_files(self.comp_list1,
                                        self.comp_list2)
        percent_sim = (3/5)*100

        # test if function produces expected output
        self.assertEqual(percent_sim, comp_percent)
        self.assertNotEqual(comp_percent, 100.0)

        # test if output type is float
        self.assertEqual(type(comp_percent), float)

        # test if error raised for invalid input
        self.assertRaises(TypeError, fl.word_counter, ["ab", "cd"], "ab")
        self.assertRaises(TypeError, fl.word_counter, "ab", "cd")
        self.assertRaises(TypeError, fl.word_counter, "cd", ["ab", "cd"])
        self.assertRaises(TypeError, fl.word_counter, ["ab", "cd"], 1)
        self.assertRaises(TypeError, fl.word_counter, 2, ["ef", "gh"])


if __name__ == '__main__':
    unittest.main()
