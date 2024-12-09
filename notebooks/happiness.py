# Import pandas
import pandas as pd

# Read and parse World_Happiness_2015.csv
happiness2015 = pd.read_csv('../data/World_Happiness_2015.csv')
# Add year column for 2015
happiness2015['Year'] = 2015

# Read and parse World_Happiness_2016.csv
happiness2016 = pd.read_csv('../data/World_Happiness_2016.csv')
# Add year column for 2016
happiness2016['Year'] = 2016

# Read and parse World_Happiness_2017.csv
happiness2017 = pd.read_csv('../data/World_Happiness_2017.csv')
# Add year column for 2017
happiness2017['Year'] = 2017

# You can view the data like this:
print("2015 Data:")
print(happiness2015.head())
print("\n2016 Data:")
print(happiness2016.head())
print("\n2017 Data:")
print(happiness2017.head())


###
#Select only the columns we want from each dataframe
happiness2015_subset = happiness2015[['Country', 'Happiness Score', 'Year']].head(3)
happiness2016_subset = happiness2016[['Country', 'Happiness Score', 'Year']].head(3)

# Concatenate the two dataframes vertically and reset the index
happiness_combined_1516 = pd.concat([happiness2015_subset, happiness2016_subset], axis=0).reset_index(drop=True)

# Display the result
print("Combined 2015-2016 Data (First 3 rows from each year) with consecutive index:")
print(happiness_combined_1516)

# Create three_2015 and three_2016 subsets with three columns
three_2015 = happiness2015[['Country', 'Happiness Score', 'Year']]
three_2016 = happiness2016[['Country', 'Happiness Score', 'Year']]

# Print unique countries in each dataset
print("Countries in 2015 dataset:")
print(set(three_2015['Country']))
print("\nCountries in 2016 dataset:")
print(set(three_2016['Country']))

# Check for exact matches
matching_countries = set(three_2015['Country']) & set(three_2016['Country'])
print("\nCountries present in both years:")
print(matching_countries)

# Merge the two dataframes on the Country column
merged = pd.merge(three_2015, three_2016, on='Country')
print("\nMerged Dataset:")
print(merged)