import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the datasets
happiness_2015 = pd.read_csv('data/World_Happiness_2015.csv')
happiness_2016 = pd.read_csv('data/World_Happiness_2016.csv')
happiness_2017 = pd.read_csv('data/World_Happiness_2017.csv')

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

# Add Region column to 2017 dataset if missing
if 'Region' not in happiness_2017.columns:
    # Create a mapping from 2015 dataset
    region_map = dict(zip(happiness_2015['Country'], happiness_2015['Region']))
    
    # Add Region column to 2017 dataset
    happiness_2017['Region'] = happiness_2017['Country'].map(region_map).fillna('Unknown')

# Combine datasets
combined_data = pd.concat([
    happiness_2015[['Country', 'Happiness_Score', 'Region', 'Year']],
    happiness_2016[['Country', 'Happiness_Score', 'Region', 'Year']],
    happiness_2017[['Country', 'Happiness_Score', 'Region', 'Year']]
], ignore_index=True)

# Aggregate data by region and year
region_happiness = combined_data.groupby(['Region', 'Year'])['Happiness_Score'].agg([
    ('Mean', 'mean'), 
    ('Median', 'median'), 
    ('Std', 'std'),
    ('Count', 'count')
]).reset_index()

# Print aggregated data
print("Regional Happiness Statistics:")
print(region_happiness)

# Visualization
plt.figure(figsize=(20, 15))

# 1. Bar Plot of Mean Happiness Scores by Region and Year
ax1 = plt.subplot(2, 2, 1)
bar_plot = sns.barplot(x='Region', y='Mean', hue='Year', data=region_happiness)
plt.title('Mean Happiness Score by Region and Year', fontsize=12)
plt.xlabel('Region', fontsize=10)
plt.ylabel('Mean Happiness Score', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add value labels on top of bars
for container in bar_plot.containers:
    bar_plot.bar_label(container, fmt='%.2f', padding=3, rotation=0, fontsize=8)

# 2. Box Plot of Happiness Scores by Region
ax2 = plt.subplot(2, 2, 2)
box_plot = sns.boxplot(x='Region', y='Happiness_Score', data=combined_data)
plt.title('Distribution of Happiness Scores by Region', fontsize=12)
plt.xlabel('Region', fontsize=10)
plt.ylabel('Happiness Score', fontsize=10)
plt.xticks(rotation=45, ha='right')

# Correct median calculation
medians = combined_data.groupby('Region')['Happiness_Score'].median()
    
# Add median values on box plots
for i, (region, median) in enumerate(medians.items()):
    box_plot.text(i, median, f'{median:.2f}', 
                  horizontalalignment='center', 
                  verticalalignment='bottom', 
                  fontsize=8,
                  color='red',  # Make the text more visible
                  fontweight='bold')

# Detailed median calculation debugging
print("\nDetailed Median Calculation:")
for region in combined_data['Region'].unique():
    region_data = combined_data[combined_data['Region'] == region]
    print(f"\n{region}:")
    print("Yearly Medians:")
    yearly_medians = region_data.groupby('Year')['Happiness_Score'].median()
    print(yearly_medians)
    print("Overall Median:", region_data['Happiness_Score'].median())

# 3. Line Plot of Mean Happiness Scores by Region
ax3 = plt.subplot(2, 2, 3)
for region in combined_data['Region'].unique():
    region_data = region_happiness[region_happiness['Region'] == region]
    line = plt.plot(region_data['Year'], region_data['Mean'], marker='o', label=region)
    
    # Add value labels at the end of each line
    last_value = region_data['Mean'].iloc[-1]
    plt.annotate(f'{last_value:.2f}', 
                xy=(2017, last_value), 
                xytext=(5, 0), 
                textcoords='offset points', 
                fontsize=8,
                va='center')

plt.title('Mean Happiness Score Trends by Region', fontsize=12)
plt.xlabel('Year', fontsize=10)
plt.ylabel('Mean Happiness Score', fontsize=10)
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

# 4. Violin Plot of Happiness Scores by Region
ax4 = plt.subplot(2, 2, 4)
violin_plot = sns.violinplot(x='Region', y='Happiness_Score', data=combined_data)
plt.title('Violin Plot of Happiness Scores by Region', fontsize=12)
plt.xlabel('Region', fontsize=10)
plt.ylabel('Happiness Score', fontsize=10)
plt.xticks(rotation=45, ha='right')

# Add median values on violin plots
medians = combined_data.groupby('Region')['Happiness_Score'].median()
for i, median in enumerate(medians):
    violin_plot.text(i, median, f'{median:.2f}', horizontalalignment='center', verticalalignment='bottom', fontsize=8)

# Adjust layout and save
plt.tight_layout()
plt.suptitle('World Happiness Trends by Region (2015-2017)', fontsize=16, y=1.02)

# Cross-checking function
def cross_check_values(combined_data, region_happiness):
    print("\n--- CROSS-CHECKING GRAPH VALUES ---")
    
    # 1. Bar Plot (Mean Happiness by Region and Year)
    print("\n1. Bar Plot (Mean Happiness Scores):")
    for _, row in region_happiness.iterrows():
        print(f"{row['Region']} ({row['Year']}): Mean = {row['Mean']:.4f}, Median = {row['Median']:.4f}")
    
    # 2. Box Plot (Median Happiness Scores)
    print("\n2. Box Plot (Median Happiness Scores):")
    medians = combined_data.groupby('Region')['Happiness_Score'].median()
    for region, median in medians.items():
        print(f"{region}: {median:.4f}")
    
    # 3. Line Plot (Mean Happiness Trends)
    print("\n3. Line Plot (Mean Happiness Trends):")
    yearly_means = combined_data.groupby(['Region', 'Year'])['Happiness_Score'].mean().reset_index()
    for region in combined_data['Region'].unique():
        region_data = yearly_means[yearly_means['Region'] == region]
        print(f"\n{region}:")
        for _, row in region_data.iterrows():
            print(f"Year {row['Year']}: {row['Happiness_Score']:.4f}")
    
    # 4. Violin Plot (Distribution)
    print("\n4. Violin Plot (Distribution Statistics):")
    distribution_stats = combined_data.groupby('Region')['Happiness_Score'].agg(['median', 'mean', 'std'])
    print(distribution_stats)

# Add this function call before plt.show()
cross_check_values(combined_data, region_happiness)

# Business-friendly tables generation
def generate_business_tables(combined_data, region_happiness):
    import pandas as pd
    
    # 1. Regional Happiness Overview
    overview_table = combined_data.groupby('Region')['Happiness_Score'].agg([
        ('Avg Happiness', 'mean'),
        ('Median Happiness', 'median'),
        ('Happiness Variability', 'std'),
        ('Number of Countries', 'count')
    ]).round(2).reset_index()
    overview_table.to_csv('data/regional_happiness_overview.csv', index=False)
    print("\n1. Regional Happiness Overview:")
    print(overview_table.to_string(index=False))
    
    # 2. Yearly Trend Analysis
    yearly_trends = combined_data.groupby(['Region', 'Year'])['Happiness_Score'].agg([
        ('Avg Happiness', 'mean'),
        ('Change from Previous Year', lambda x: x.mean() - x.mean())
    ]).round(2).reset_index()
    
    # Calculate year-over-year change
    yearly_trends_with_change = []
    for region in combined_data['Region'].unique():
        region_data = yearly_trends[yearly_trends['Region'] == region].sort_values('Year')
        if len(region_data) > 1:
            for i in range(1, len(region_data)):
                region_data.loc[region_data.index[i], 'Change from Previous Year'] = (
                    region_data.iloc[i]['Avg Happiness'] - region_data.iloc[i-1]['Avg Happiness']
                )
        yearly_trends_with_change.append(region_data)
    
    yearly_trends_df = pd.concat(yearly_trends_with_change).round(2)
    yearly_trends_df.to_csv('data/regional_happiness_yearly_trends.csv', index=False)
    print("\n2. Yearly Happiness Trends:")
    print(yearly_trends_df.to_string(index=False))
    
    # 3. Top and Bottom Performers
    performance_table = combined_data.groupby('Region')['Happiness_Score'].agg([
        ('Best Year Happiness', 'max'),
        ('Worst Year Happiness', 'min'),
        ('Performance Range', lambda x: x.max() - x.min())
    ]).round(2).reset_index()
    performance_table.to_csv('data/regional_happiness_performance.csv', index=False)
    print("\n3. Regional Performance Summary:")
    print(performance_table.to_string(index=False))

# Call the function before plt.show()
generate_business_tables(combined_data, region_happiness)

def print_formatted_tables(combined_data, region_happiness):
    import pandas as pd
    import textwrap
    
    # Open a file to write the tables
    with open('data/happiness_tables.txt', 'w') as f:
        # 1. Regional Happiness Overview
        overview_header = "\n🌍 GLOBAL HAPPINESS REPORT: REGIONAL OVERVIEW 🌍"
        overview_separator = "=" * 80
        f.write(overview_header + "\n")
        f.write(overview_separator + "\n")
        
        overview_table = combined_data.groupby('Region')['Happiness_Score'].agg([
            ('Avg Happiness', 'mean'),
            ('Median Happiness', 'median'),
            ('Happiness Variability', 'std'),
            ('Number of Countries', 'count')
        ]).round(2).reset_index()
        
        # Custom formatting for presentation
        header = f"{'Region':<30} {'Avg Happiness':>15} {'Median':>10} {'Variability':>15} {'Countries':>10}\n"
        separator = "-" * 80 + "\n"
        f.write(header)
        f.write(separator)
        
        for _, row in overview_table.iterrows():
            line = f"{row['Region']:<30} {row['Avg Happiness']:>15.2f} {row['Median Happiness']:>10.2f} {row['Happiness Variability']:>15.2f} {row['Number of Countries']:>10}\n"
            f.write(line)
        
        # 2. Yearly Trends Analysis
        trends_header = "\n📊 HAPPINESS TRENDS BY REGION (2015-2017) 📊"
        trends_separator = "=" * 80
        f.write(trends_header + "\n")
        f.write(trends_separator + "\n")
        
        yearly_trends = combined_data.groupby(['Region', 'Year'])['Happiness_Score'].agg([
            ('Avg Happiness', 'mean')
        ]).round(2).reset_index()
        
        # Pivot the data for easy reading
        trends_pivot = yearly_trends.pivot(index='Region', columns='Year', values='Avg Happiness')
        trends_pivot['Change 2015-2017'] = trends_pivot[2017] - trends_pivot[2015]
        
        trends_header_line = f"{'Region':<30} {'2015':>10} {'2016':>10} {'2017':>10} {'Change':>10}\n"
        trends_separator_line = "-" * 80 + "\n"
        f.write(trends_header_line)
        f.write(trends_separator_line)
        
        for region, row in trends_pivot.iterrows():
            line = f"{region:<30} {row[2015]:>10.2f} {row[2016]:>10.2f} {row[2017]:>10.2f} {row['Change 2015-2017']:>10.2f}\n"
            f.write(line)
        
        # 3. Performance Summary
        performance_header = "\n🏆 REGIONAL HAPPINESS PERFORMANCE SUMMARY 🏆"
        performance_separator = "=" * 80
        f.write(performance_header + "\n")
        f.write(performance_separator + "\n")
        
        performance_table = combined_data.groupby('Region')['Happiness_Score'].agg([
            ('Best Score', 'max'),
            ('Worst Score', 'min'),
            ('Performance Range', lambda x: x.max() - x.min())
        ]).round(2).reset_index()
        
        performance_header_line = f"{'Region':<30} {'Best Score':>15} {'Worst Score':>15} {'Performance Range':>20}\n"
        performance_separator_line = "-" * 80 + "\n"
        f.write(performance_header_line)
        f.write(performance_separator_line)
        
        for _, row in performance_table.iterrows():
            line = f"{row['Region']:<30} {row['Best Score']:>15.2f} {row['Worst Score']:>15.2f} {row['Performance Range']:>20.2f}\n"
            f.write(line)
    
    # Also print to console
    with open('data/happiness_tables.txt', 'r') as f:
        print(f.read())

# Call the function before plt.show()
print_formatted_tables(combined_data, region_happiness)

plt.savefig('data/happiness_by_region.png', dpi=300, bbox_inches='tight')
plt.show()

# Save aggregated data to CSV
region_happiness.to_csv('data/regional_happiness_stats.csv', index=False)
print("\nRegional happiness statistics saved to 'data/regional_happiness_stats.csv'")
