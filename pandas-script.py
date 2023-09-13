import pandas as pd

# dataset url
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/fifa/fifa_countries_audience.csv"

# create pandas dataframe from url
df = pd.read_csv(url)

# get the top 5 countries with the greatest mean population share
mean_population_share = df.groupby('country')['population_share'].mean().sort_values(ascending=False)
print('MEAN POPULATION SHARE TOP 5:')
print(mean_population_share.head())

# get the top 5 countries with the greatest tv audience share
tv_audience = df.groupby('country')['tv_audience_share'].mean().sort_values(ascending=False)
print('TV AUDIENCE TOP 5:')
print(tv_audience.head())

# get the top 5 countries with the greatest gdp_weighted share
gdp_weighted = df.groupby('country')['gdp_weighted_share'].mean().sort_values(ascending=False)
print('GDP WEIGHTED TOP 5:')
print(gdp_weighted.head())

# get the number of countries per each confederation
confederation_counts = df.groupby('confederation').size()
print('NUMBER OF COUNTRIES IN EACH CONFEDERATION:')
print(confederation_counts)
