import os
import sys
import unittest
import pandas as pd

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestDataLoading(unittest.TestCase):
    def setUp(self):
        # Path to data directory
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    
    def test_csv_files_exist(self):
        """Check if required CSV files exist"""
        required_files = [
            'World_Happiness_2015.csv',
            'World_Happiness_2016.csv',
            'World_Happiness_2017.csv',
            'regional_happiness_stats.csv'
        ]
        
        for file in required_files:
            file_path = os.path.join(self.data_dir, file)
            self.assertTrue(os.path.exists(file_path), f"{file} is missing from data directory")
    
    def test_data_loading(self):
        """Test loading of the main happiness dataset"""
        file_path = os.path.join(self.data_dir, 'World_Happiness_2015.csv')
        
        # Try loading the CSV
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            self.fail(f"Failed to load CSV file: {e}")
        
        # Check basic data integrity
        self.assertFalse(df.empty, "Dataframe is empty")
        
        # Check expected columns
        expected_columns = ['Country', 'Region', 'Happiness Score']
        for col in expected_columns:
            self.assertIn(col, df.columns, f"Missing expected column: {col}")

class TestDataValidation(unittest.TestCase):
    def setUp(self):
        # Path to data directory
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        
        # Load the dataset
        self.df = pd.read_csv(os.path.join(self.data_dir, 'World_Happiness_2015.csv'))
    
    def test_happiness_score_range(self):
        """Validate happiness scores are within expected range"""
        self.assertTrue(
            (self.df['Happiness Score'] >= 0).all() and 
            (self.df['Happiness Score'] <= 10).all(), 
            "Happiness scores should be between 0 and 10"
        )
    
    def test_unique_regions(self):
        """Check that regions are meaningful"""
        invalid_regions = ['', None]
        valid_regions = self.df['Region'].unique()
        
        for region in invalid_regions:
            self.assertNotIn(region, valid_regions, f"Invalid region found: {region}")
        
        # Optional: Check for a minimum number of unique regions
        self.assertGreater(len(valid_regions), 5, "Too few unique regions")

if __name__ == '__main__':
    unittest.main()
