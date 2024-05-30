import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the URL
url = "https://raw.githubusercontent.com/TjabbeN/BAproef/main/data/data_glansmeting.csv"
df = pd.read_csv(url)

# Drop the 'meting' column
df = df.drop(columns=['meting'])

# Calculate the average per zone
average_per_zone = df.groupby('zone').mean()

print(average_per_zone)