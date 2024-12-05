import matplotlib.pyplot as plt
import seaborn as sns

def plot_happiness_distribution(df):
    """
    Create a distribution plot of happiness scores.
    
    Args:
        df (pd.DataFrame): Input happiness dataset
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Happiness Score', bins=20)
    plt.title('Distribution of Happiness Scores')
    plt.xlabel('Happiness Score')
    plt.ylabel('Count')

def plot_regional_comparison(df):
    """
    Create a box plot comparing happiness scores across regions.
    
    Args:
        df (pd.DataFrame): Input happiness dataset
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Region', y='Happiness Score')
    plt.xticks(rotation=45)
    plt.title('Happiness Scores by Region')
    plt.tight_layout()

def correlation_heatmap(df):
    """
    Create a correlation heatmap for numerical variables.
    
    Args:
        df (pd.DataFrame): Input happiness dataset
    """
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
