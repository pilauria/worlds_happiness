import unittest
import os
import matplotlib.pyplot as plt
import pandas as pd

class TestVisualization(unittest.TestCase):
    def setUp(self):
        # Path to notebooks directory
        self.notebooks_dir = os.path.join(os.path.dirname(__file__), '..', 'notebooks')
        # Path to data directory
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    
    def test_visualization_output(self):
        """Check if visualization script generates output files"""
        # Temporarily suppress matplotlib output
        plt.switch_backend('Agg')
        
        # Import the visualization script
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "happiness_visualization", 
            os.path.join(self.notebooks_dir, "happiness_visualization.py")
        )
        visualization_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(visualization_module)
        
        # Check if plot files are generated
        expected_plot_files = [
            'happiness_by_region.png',
            'happiness_trends.png'
        ]
        
        for plot_file in expected_plot_files:
            plot_path = os.path.join(self.data_dir, plot_file)
            self.assertTrue(os.path.exists(plot_path), f"Plot file {plot_file} was not generated")
    
    def test_plot_content(self):
        """Verify basic properties of generated plots"""
        # Load a plot file
        plot_path = os.path.join(self.data_dir, 'happiness_by_region.png')
        
        # Check file exists and is not empty
        self.assertTrue(os.path.exists(plot_path), "Plot file does not exist")
        self.assertGreater(os.path.getsize(plot_path), 0, "Plot file is empty")

class TestStatisticalAnalysis(unittest.TestCase):
    def setUp(self):
        # Load the dataset
        self.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.df = pd.read_csv(os.path.join(self.data_dir, 'regional_happiness_stats.csv'))
    
    def test_regional_aggregations(self):
        """Verify regional aggregation calculations"""
        # Group by region and calculate mean
        regional_means = self.df.groupby('Region')['Happiness_Score'].mean()
        
        # Check some known regions
        known_regions = [
            'Western Europe', 
            'North America', 
            'Sub-Saharan Africa'
        ]
        
        for region in known_regions:
            self.assertIn(region, regional_means.index, f"Region {region} not found in aggregations")
            
            # Ensure mean is a valid number
            self.assertTrue(
                pd.notna(regional_means[region]), 
                f"Mean for {region} is not a valid number"
            )

if __name__ == '__main__':
    unittest.main()
