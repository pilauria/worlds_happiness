import unittest
import pandas as pd
import os

class TestDataLoading(unittest.TestCase):
    def setUp(self):
        # Path to the data directory
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    
    def test_csv_files_exist(self):
        """Check if required CSV files exist"""
        required_files = [
            'regional_happiness_stats.csv',
            'happiness_stats.csv'  # Add other expected CSV files
        ]
        
        for file in required_files:
            file_path = os.path.join(self.data_dir, file)
            self.assertTrue(os.path.exists(file_path), f"{file} is missing from data directory")
    
    def test_data_loading(self):
        """Test loading of the main happiness dataset"""
        file_path = os.path.join(self.data_dir, 'regional_happiness_stats.csv')
        
        # Try loading the CSV
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            self.fail(f"Failed to load CSV file: {e}")
        
        # Check basic data integrity
        self.assertFalse(df.empty, "Dataframe is empty")
        
        # Check expected columns
        expected_columns = ['Region', 'Year', 'Happiness_Score']
        for col in expected_columns:
            self.assertIn(col, df.columns, f"Missing expected column: {col}")

class TestDataValidation(unittest.TestCase):
    def setUp(self):
        # Load the dataset
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.df = pd.read_csv(os.path.join(self.data_dir, 'regional_happiness_stats.csv'))
    
    def test_happiness_score_range(self):
        """Validate happiness scores are within expected range"""
        self.assertTrue(
            (self.df['Happiness_Score'] >= 0).all() and 
            (self.df['Happiness_Score'] <= 10).all(), 
            "Happiness scores should be between 0 and 10"
        )
    
    def test_unique_regions(self):
        """Check that regions are meaningful"""
        invalid_regions = ['', 'Unknown', None]
        valid_regions = self.df['Region'].unique()
        
        for region in invalid_regions:
            self.assertNotIn(region, valid_regions, f"Invalid region found: {region}")

if __name__ == '__main__':
    unittest.main()
