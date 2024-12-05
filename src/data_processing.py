import pandas as pd
import numpy as np

def load_happiness_data(filepath):
    """
    Load and preprocess the World Happiness dataset.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Preprocessed happiness dataset
    """
    df = pd.read_csv(filepath)
    return df

def calculate_basic_stats(df):
    """
    Calculate basic statistics for numerical columns.
    
    Args:
        df (pd.DataFrame): Input happiness dataset
        
    Returns:
        pd.DataFrame: Statistical summary
    """
    return df.describe()

def get_regional_stats(df):
    """
    Calculate happiness statistics by region.
    
    Args:
        df (pd.DataFrame): Input happiness dataset
        
    Returns:
        pd.DataFrame: Regional statistics
    """
    return df.groupby('Region')['Happiness Score'].agg(['mean', 'std', 'count'])
