import unittest
import utils
import pandas as pd
import pandas.testing as pd_testing


class TestUtils(unittest.TestCase):

    def test_cramersV(self):
        return -1
    
    def test_filter_data(self):
        # Set up data
        data = [['A', 10], ['B', 15], ['C', 14], ['D', 15]]
        df = pd.DataFrame(data, columns=['Names', 'Counts'])
        
        # Positive test
        target_df = df.drop(index=2)
        pd_testing.assert_frame_equal(utils.filter_data(df, 'Counts', [15, 10]), target_df)


if __name__ == '__main__':
    unittest.main()
