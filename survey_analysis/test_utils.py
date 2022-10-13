import unittest
import utils
import random
import numpy as np
import pandas as pd


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # set up sample dataframe to work with
        data = [['A', 10], ['B', 15], ['C', 14], ['D', 15]]
        cls.df = pd.DataFrame(data, columns=['Names', 'Counts'])

    @classmethod
    def tearDownClass(cls):
        df = None

    def test_cramersV(self):
        return -1
    
    def test_filter_data(self):
        # Positive test
        target_df = pd.DataFrame([['A', 10], ['B', 15], ['D', 15]], columns=['Names', 'Counts'])
        self.assertEqual(utils.filter_data(cls.df, 'Counts', [15, 10]), target_df)


if __name__ == '__main__':
    unittest.main()
