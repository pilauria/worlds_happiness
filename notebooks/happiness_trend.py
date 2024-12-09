import pandas as pd
import numpy as np

# Load the datasets
happiness_2015 = pd.read_csv('../data/World_Happiness_2015.csv')
happiness_2016 = pd.read_csv('../data/World_Happiness_2016.csv')
happiness_2017 = pd.read_csv('../data/World_Happiness_2017.csv')

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

# Function to calculate global happiness statistics
def calculate_happiness_stats(df):
    return {
        'mean': df['Happiness_Score'].mean(),
        'median': df['Happiness_Score'].median(),
        'min': df['Happiness_Score'].min(),
        'max': df['Happiness_Score'].max(),
        'std': df['Happiness_Score'].std()
    }

# Calculate statistics for each year
stats_2015 = calculate_happiness_stats(happiness_2015)
stats_2016 = calculate_happiness_stats(happiness_2016)
stats_2017 = calculate_happiness_stats(happiness_2017)

# Print detailed statistics
print("Happiness Score Statistics:")
print("2015:", stats_2015)
print("2016:", stats_2016)
print("2017:", stats_2017)

# Merge datasets to compare countries across years
# Use outer merge to keep all countries
merged_data = pd.merge(
    happiness_2015[['Country', 'Happiness_Score']], 
    happiness_2016[['Country', 'Happiness_Score']], 
    on='Country', 
    how='outer', 
    suffixes=('_2015', '_2016')
)

merged_data = pd.merge(
    merged_data, 
    happiness_2017[['Country', 'Happiness_Score']], 
    on='Country', 
    how='outer'
)
merged_data.columns = ['Country', 'Score_2015', 'Score_2016', 'Score_2017']

# Calculate change between years
merged_data['Change_2015_2016'] = merged_data['Score_2016'] - merged_data['Score_2015']
merged_data['Change_2016_2017'] = merged_data['Score_2017'] - merged_data['Score_2016']

# Print overall trend
print("\nOverall Trend Analysis:")
print(f"Mean Change 2015 to 2016: {merged_data['Change_2015_2016'].mean():.4f}")
print(f"Mean Change 2016 to 2017: {merged_data['Change_2016_2017'].mean():.4f}")

# Percentage of countries with positive/negative changes
print("\nCountry Change Percentages:")
pct_improved_2015_2016 = (merged_data['Change_2015_2016'] > 0).mean() * 100
pct_improved_2016_2017 = (merged_data['Change_2016_2017'] > 0).mean() * 100

print(f"Percentage of Countries Improving 2015-2016: {pct_improved_2015_2016:.2f}%")
print(f"Percentage of Countries Improving 2016-2017: {pct_improved_2016_2017:.2f}%")
