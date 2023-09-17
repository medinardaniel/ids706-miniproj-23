import polars as pl
import matplotlib.pyplot as plt

# dataset url
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/fifa/fifa_countries_audience.csv"
# output
out_file = 'output.md'

# create pandas dataframe from url
df = pl.read_csv(url)

# generate descriptive statistics
desc = df.describe()

# get the mean of tv_audience_share per confederation
mean_tv_viewers = (
    df.group_by('confederation')
    .agg(pl.col('tv_audience_share').mean().alias('mean_tv_audience_share'))
)

# plot mean_tv_viewers in a bar chart
mean_tv_viewers.to_pandas().plot.bar(x='confederation', y='mean_tv_audience_share')
plt.title('Confederations by mean TV audience share')
plt.xlabel('Confederation')
plt.ylabel('Mean TV audience share')
plt.savefig('top_10.png')

# write desc to markdown file
desc_pd = desc.to_pandas()
desc_str = desc_pd.to_string()
with open(out_file, 'w') as f:
    f.write(desc_str)
