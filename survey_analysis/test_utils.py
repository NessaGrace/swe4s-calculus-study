import unittest
import utils
import random
import numpy as np


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # read in simulated survey data
        cls.survey_data = pd.read_csv('test_sim_data.csv')

    @classmethod
    def tearDownClass(cls):
        return -1

    def test_cramersV(self):
        return -1
    
    def test_filter_data(self):
        # Test to see if one 


if __name__ == '__main__':
    unittest.main()
