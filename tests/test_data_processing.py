import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_processing import load_happiness_data, calculate_basic_stats, get_regional_stats

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.data_path = "../data/World_Happiness_2015.csv"
        self.df = load_happiness_data(self.data_path)

    def test_load_happiness_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertFalse(self.df.empty)

    def test_calculate_basic_stats(self):
        stats = calculate_basic_stats(self.df)
        self.assertIsInstance(stats, pd.DataFrame)

    def test_get_regional_stats(self):
        regional_stats = get_regional_stats(self.df)
        self.assertIsInstance(regional_stats, pd.DataFrame)
        self.assertTrue('mean' in regional_stats.columns)

if __name__ == '__main__':
    unittest.main()
