import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use absolute path to load data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path_2015 = os.path.join(current_dir, '..', 'data', 'World_Happiness_2015.csv')
data_path_2016 = os.path.join(current_dir, '..', 'data', 'World_Happiness_2016.csv')
data_path_2017 = os.path.join(current_dir, '..', 'data', 'World_Happiness_2017.csv')

happiness_2015 = pd.read_csv(data_path_2015)
happiness_2016 = pd.read_csv(data_path_2016)
happiness_2017 = pd.read_csv(data_path_2017)

# Create output directory if it doesn't exist
output_dir = os.path.join(current_dir, '..', 'data')
os.makedirs(output_dir, exist_ok=True)

# Standardize column names
happiness_2015 = happiness_2015.rename(columns={
    'Happiness Score': 'Happiness_Score', 
    'Happiness Rank': 'Happiness_Rank'
})
happiness_2016 = happiness_2016.rename(columns={
    'Happiness Score': 'Happiness_Score', 
    'Happiness Rank': 'Happiness_Rank'
})
happiness_2017 = happiness_2017.rename(columns={
    'Happiness.Score': 'Happiness_Score', 
    'Happiness.Rank': 'Happiness_Rank'
})

# Add year column to each dataset
happiness_2015['Year'] = 2015
happiness_2016['Year'] = 2016
happiness_2017['Year'] = 2017

# Combine datasets
combined_data = pd.concat([
    happiness_2015[['Country', 'Happiness_Score', 'Year']],
    happiness_2016[['Country', 'Happiness_Score', 'Year']],
    happiness_2017[['Country', 'Happiness_Score', 'Year']]
])

# Set up the plot 
plt.figure(figsize=(16, 10))

# 1. Box Plot of Happiness Scores by Year
plt.subplot(2, 2, 1)
sns.boxplot(x='Year', y='Happiness_Score', data=combined_data)
plt.title('Distribution of Happiness Scores by Year', fontsize=12)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Happiness Score', fontsize=10)

# 2. Violin Plot of Happiness Scores
plt.subplot(2, 2, 2)
sns.violinplot(x='Year', y='Happiness_Score', data=combined_data)
plt.title('Violin Plot of Happiness Scores', fontsize=12)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Happiness Score', fontsize=10)

# 3. Scatter Plot of Top 10 Countries
plt.subplot(2, 2, 3)
top_countries = combined_data.groupby('Country')['Happiness_Score'].mean().nlargest(10).index
top_countries_data = combined_data[combined_data['Country'].isin(top_countries)]

sns.scatterplot(x='Year', y='Happiness_Score', hue='Country', data=top_countries_data)
plt.title('Top 10 Countries Happiness Scores', fontsize=12)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Happiness Score', fontsize=10)
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# 4. Bar Plot of Mean Happiness Scores by Year
plt.subplot(2, 2, 4)
yearly_mean = combined_data.groupby('Year')['Happiness_Score'].mean()
yearly_mean.plot(kind='bar')
plt.title('Mean Happiness Score by Year', fontsize=12)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Mean Happiness Score', fontsize=10)

# Adjust layout and save
plt.tight_layout()
plt.suptitle('World Happiness Trends (2015-2017)', fontsize=16, y=1.02)
plt.savefig(os.path.join(output_dir, 'happiness_trends.png'), dpi=300, bbox_inches='tight')
plt.show()
