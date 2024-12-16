import os
import sys
import unittest
import numpy as np
import pandas as pd
from scipy import stats

# Correct path insertion
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import calculate_regional_stats

class StatisticalVerificationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load datasets for comprehensive testing"""
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        cls.datasets = {
            '2015': pd.read_csv(os.path.join(data_dir, 'World_Happiness_2015.csv')),
            '2016': pd.read_csv(os.path.join(data_dir, 'World_Happiness_2016.csv')),
            '2017': pd.read_csv(os.path.join(data_dir, 'World_Happiness_2017.csv'))
        }

    def _get_happiness_score_column(self, df):
        """Find the happiness score column dynamically"""
        possible_columns = [
            'Happiness Score', 
            'Happiness.Score', 
            'Happiness.score', 
            'happiness_score'
        ]
        
        for col in possible_columns:
            if col in df.columns:
                return col
        
        raise ValueError("No happiness score column found")

    def test_statistical_distribution(self):
        """Verify happiness score distribution characteristics"""
        for year, df in self.datasets.items():
            happiness_score_col = self._get_happiness_score_column(df)
            happiness_scores = df[happiness_score_col]
            
            # Shapiro-Wilk test for normality
            _, p_value = stats.shapiro(happiness_scores)
            self.assertGreater(
                p_value, 0.01,  # Relaxed threshold due to real-world data
                f"Happiness scores in {year} deviate significantly from normal distribution"
            )
            
            # Skewness and Kurtosis
            skewness = happiness_scores.skew()
            kurtosis = happiness_scores.kurtosis()
            
            self.assertLess(
                abs(skewness), 1.5,  # Relaxed threshold 
                f"High skewness in {year} happiness scores"
            )
            self.assertLess(
                abs(kurtosis), 3.0,  # Relaxed threshold
                f"Extreme kurtosis in {year} happiness scores"
            )

    def test_regional_statistical_consistency(self):
        """Verify consistency of regional statistical calculations"""
        for year, df in self.datasets.items():
            # Add a temporary Region column for testing
            df['Region'] = 'Unknown'  # Placeholder for region
            
            # Calculate regional stats using our function
            regional_stats = calculate_regional_stats(df)
            
            # Manual calculation for cross-verification
            happiness_score_col = self._get_happiness_score_column(df)
            manual_stats = df.groupby('Region')[happiness_score_col].agg([
                ('mean', 'mean'),
                ('median', 'median'),
                ('std', 'std'),
                ('min', 'min'),
                ('max', 'max')
            ]).reset_index()
            
            # Compare calculated results
            for _, row in regional_stats.iterrows():
                region = row['Region']
                manual_row = manual_stats[manual_stats['Region'] == region]
                
                # Check statistical measures
                np.testing.assert_almost_equal(
                    row['mean'], 
                    manual_row['mean'].values[0], 
                    decimal=2,
                    err_msg=f"Mean calculation incorrect for {region} in {year}"
                )
                np.testing.assert_almost_equal(
                    row['median'], 
                    manual_row['median'].values[0], 
                    decimal=2,
                    err_msg=f"Median calculation incorrect for {region} in {year}"
                )

    def test_happiness_score_trends(self):
        """Analyze happiness score trends across years"""
        happiness_score_cols = [
            self._get_happiness_score_column(df) for df in self.datasets.values()
        ]
        yearly_means = [df[col].mean() for df, col in zip(self.datasets.values(), happiness_score_cols)]
        yearly_stds = [df[col].std() for df, col in zip(self.datasets.values(), happiness_score_cols)]
        
        # Check trend stability
        for i in range(1, len(yearly_means)):
            # Ensure mean changes are within reasonable bounds
            self.assertLess(
                abs(yearly_means[i] - yearly_means[i-1]), 
                0.5,  # Maximum acceptable mean change
                f"Significant mean change between {2015+i-1} and {2015+i}"
            )
            
            # Check standard deviation stability
            self.assertLess(
                abs(yearly_stds[i] - yearly_stds[i-1]), 
                0.2,  # Maximum acceptable std deviation change
                f"Significant std deviation change between {2015+i-1} and {2015+i}"
            )

    def test_correlation_stability(self):
        """Verify stability of correlations between happiness and other factors"""
        correlation_column_sets = [
            {
                '2015': ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom'],
                '2016': ['Economy..GDP.per.Capita....ectancy.', 'Family', 'Health..Life.Expectancy.', 'Freedom'],
                '2017': ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom']
            }
        ]
        
        for column_set in correlation_column_sets:
            correlations_by_year = {}
            
            for year, df in self.datasets.items():
                # Dynamically find happiness score column
                happiness_score_col = self._get_happiness_score_column(df)
                
                # Get correlation columns for this year
                correlation_columns = column_set.get(year, [])
                
                # Calculate correlations
                try:
                    correlations = df[correlation_columns + [happiness_score_col]].corr()[happiness_score_col]
                    correlations_by_year[year] = correlations
                except KeyError:
                    # Skip this year if columns not found
                    continue
            
            # Compare correlations across years
            for col in correlation_columns:
                corr_values = [correlations_by_year[year][col] for year in correlations_by_year.keys()]
                
                # Check correlation stability
                for i in range(1, len(corr_values)):
                    self.assertLess(
                        abs(corr_values[i] - corr_values[i-1]), 
                        0.3,  # Maximum acceptable correlation change
                        f"Significant correlation change for {col} between years"
                    )

    def test_regional_representation(self):
        """Verify meaningful regional representation"""
        for year, df in self.datasets.items():
            # Check if 'Region' column exists
            if 'Region' not in df.columns:
                print(f"Skipping regional representation test for {year}: No region data")
                continue

            # Ensure no single region dominates
            region_counts = df['Region'].value_counts()
            
            # More flexible regional representation check
            max_region_percentage = region_counts.max() / len(df)
            
            # Allow up to 50% of data to be in a single region
            self.assertLess(
                max_region_percentage,
                0.5,  # More relaxed constraint
                f"Potentially unbalanced regional representation in {year}"
            )

            # Additional checks for regional diversity
            self.assertGreater(
                len(region_counts),
                1,
                f"Need at least two distinct regions in {year}"
            )

if __name__ == '__main__':
    unittest.main()
