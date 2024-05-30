import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the URL
url = "https://raw.githubusercontent.com/TjabbeN/BAproef/main/data/data_glansmeting.csv"
df = pd.read_csv(url)

# Drop the 'meting' column
df = df.drop(columns=['meting'])

# Calculate the average per zone
average_per_zone = df.groupby('zone').mean()

# Define the custom colors for each column
colors = {
    '20': '#d6b863',  
    '60': '#CF4C48',  
    '85': '#242B5F',  
    'DOI': '#CFCFCF',  
    'Haze': '#a0a0a0',  
    'Rspec': '#767676'  
}

# Reorder colors to match the order of columns in average_per_zone
ordered_colors = [colors[col] for col in average_per_zone.columns]

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))
average_per_zone.plot(kind='bar', ax=ax,color=ordered_colors, width = 0.805, zorder = 3)
ax.set_title('Gemiddelde Glans Metingen per Mock-up')
ax.set_xlabel('Mock-up')
#ax.set_yscale('log')
ax.set_ylabel('Gemiddelde Waarde per Meting')
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder = 2, color = "#C5C5C4")
plt.xticks(rotation=0)
plt.legend(title='Metingen', loc='upper left')
plt.tight_layout()

for value in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]:
    ax.axvline(x=value, color='#f6f6f6', linestyle='-', linewidth=40, zorder = 1)

# Display the plot
plt.show()
