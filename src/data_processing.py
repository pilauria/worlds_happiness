import pandas as pd
import numpy as np

def load_happiness_data(filepath):
    """
    Load happiness data from CSV file
    
    Args:
        filepath (str): Path to the CSV file
    
    Returns:
        pd.DataFrame: Loaded dataframe
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def _find_happiness_score_column(df):
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

def calculate_regional_stats(df):
    """
    Calculate comprehensive regional statistics

    Args:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Regional statistics
    """
    # Find happiness score column dynamically
    happiness_score_col = _find_happiness_score_column(df)

    # Placeholder for regional stats calculation
    regional_stats = df.groupby('Region')[happiness_score_col].agg([
        ('mean', 'mean'),
        ('median', 'median'),
        ('std', 'std'),
        ('min', 'min'),
        ('max', 'max')
    ]).reset_index()

    return regional_stats

def main():
    # Example usage
    filepath = '../data/World_Happiness_2015.csv'
    df = load_happiness_data(filepath)
    
    if df is not None:
        # Calculate regional stats
        regional_stats = calculate_regional_stats(df)
        print("Regional Statistics:")
        print(regional_stats)

if __name__ == '__main__':
    main()
