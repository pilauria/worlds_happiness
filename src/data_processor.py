import pandas as pd
import numpy as np

class HappinessDataProcessor:
    @staticmethod
    def load_data(filepath):
        """
        Load happiness data from CSV file
        
        Args:
            filepath (str): Path to the CSV file
        
        Returns:
            pd.DataFrame: Loaded and preprocessed dataframe
        """
        try:
            df = pd.read_csv(filepath)
            return df
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return None
    
    @staticmethod
    def calculate_regional_stats(df):
        """
        Calculate comprehensive regional statistics
        
        Args:
            df (pd.DataFrame): Input dataframe
        
        Returns:
            pd.DataFrame: Regional statistics
        """
        regional_stats = df.groupby('Region')['Happiness_Score'].agg([
            ('Mean', 'mean'),
            ('Median', 'median'),
            ('Std Dev', 'std'),
            ('Min', 'min'),
            ('Max', 'max')
        ]).reset_index()
        
        return regional_stats
    
    @staticmethod
    def normalize_happiness_scores(df):
        """
        Normalize happiness scores using min-max scaling
        
        Args:
            df (pd.DataFrame): Input dataframe
        
        Returns:
            pd.DataFrame: Dataframe with normalized happiness scores
        """
        df_copy = df.copy()
        df_copy['Normalized_Happiness'] = (df_copy['Happiness_Score'] - df_copy['Happiness_Score'].min()) / \
                                          (df_copy['Happiness_Score'].max() - df_copy['Happiness_Score'].min())
        return df_copy

def main():
    # Example usage
    processor = HappinessDataProcessor()
    df = processor.load_data('../data/regional_happiness_stats.csv')
    
    if df is not None:
        # Calculate regional stats
        regional_stats = processor.calculate_regional_stats(df)
        print("Regional Statistics:")
        print(regional_stats)
        
        # Normalize scores
        normalized_df = processor.normalize_happiness_scores(df)
        print("\nNormalized Happiness Scores:")
        print(normalized_df[['Region', 'Happiness_Score', 'Normalized_Happiness']].head())

if __name__ == '__main__':
    main()
