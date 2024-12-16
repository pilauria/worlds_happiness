import os
import sys
import unittest
import pandas as pd

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import load_happiness_data, calculate_regional_stats

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Use absolute path to the data file
        self.data_path = os.path.join(
            os.path.dirname(__file__), 
            '..', 
            'data', 
            'World_Happiness_2015.csv'
        )
        self.df = load_happiness_data(self.data_path)
    
    def test_load_happiness_data(self):
        """Test loading of happiness data"""
        self.assertIsNotNone(self.df, "DataFrame should not be None")
        self.assertFalse(self.df.empty, "DataFrame should not be empty")
    
    def test_calculate_basic_stats(self):
        """Test basic statistical calculations"""
        stats = calculate_regional_stats(self.df)
        self.assertIsNotNone(stats, "Regional stats should not be None")
        self.assertTrue(len(stats) > 0, "Regional stats should have entries")

if __name__ == '__main__':
    unittest.main()
