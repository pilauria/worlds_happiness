import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class HappinessVisualizer:
    def __init__(self, data_path):
        """
        Initialize visualizer with data path
        
        Args:
            data_path (str): Path to happiness dataset
        """
        self.data = pd.read_csv(data_path)
        self.output_dir = os.path.join(os.path.dirname(data_path), '..')
    
    def plot_regional_happiness(self, output_filename='regional_happiness.png'):
        """
        Create bar plot of happiness scores by region
        
        Args:
            output_filename (str): Name of output plot file
        """
        plt.figure(figsize=(12, 6))
        sns.barplot(x='Region', y='Happiness_Score', data=self.data)
        plt.title('Happiness Scores by Region')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save plot
        output_path = os.path.join(self.output_dir, 'data', output_filename)
        plt.savefig(output_path)
        plt.close()
    
    def plot_happiness_trends(self, output_filename='happiness_trends.png'):
        """
        Create line plot of happiness trends over years
        
        Args:
            output_filename (str): Name of output plot file
        """
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='Year', y='Happiness_Score', hue='Region', data=self.data)
        plt.title('Happiness Trends by Region')
        plt.tight_layout()
        
        # Save plot
        output_path = os.path.join(self.output_dir, 'data', output_filename)
        plt.savefig(output_path)
        plt.close()

def main():
    # Example usage
    data_path = '../data/regional_happiness_stats.csv'
    visualizer = HappinessVisualizer(data_path)
    
    # Generate plots
    visualizer.plot_regional_happiness()
    visualizer.plot_happiness_trends()

if __name__ == '__main__':
    main()
