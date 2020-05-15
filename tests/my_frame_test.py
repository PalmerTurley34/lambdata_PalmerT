import unittest

import pandas as pd
from my_lambdata.my_frame import MyFrame
class TestSeparateDate(unittest.TestCase):

    def test_dat_col(self):
        data = pd.DataFrame({'date': ['2016-05-09', '2020-05-06', '1993-12-25']})
        df = MyFrame(data)
        # make sure that my frame keeps the dataframe the same
        self.assertEqual(data['date'].all(), df['date'].all())

        df.separate_date('date')
        # check that the three columns are created as expected
        self.assertTrue(df['Year'].all(), ['2016', '2020', '1993'])
        self.assertTrue(df['Month'].all(), ['05', '05', '12'])
        self.assertTrue(df['Day'].all(), ['09', '06', '25'])



if __name__ == "__main__":
    unittest.main()