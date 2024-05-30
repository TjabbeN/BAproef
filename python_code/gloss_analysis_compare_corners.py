import pandas as pd
import matplotlib.pyplot as plt
from set_axis_color import set_axis_color

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

# Function to plot data for a specific corner
def plot_corner(corner_suffix):
    # Filter the data for the specific corner
    filtered_zones = average_per_zone[average_per_zone.index.str.endswith(corner_suffix)]
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 9), gridspec_kw={'width_ratios': [7, 1]}, sharey=True)
    
    # Plotting all measurements for the filtered zones
    filtered_zones.plot(kind='bar', ax=ax1, color=[colors[col] for col in filtered_zones.columns], width=0.9, legend=True, zorder = 3)
    ax1.set_title(f'Gemiddelde Glans Metingen per kwadrant ({corner_suffix.upper()})', color = "#221F20")
    ax1.set_xlabel('Mock-up', color = "#221F20")
    ax1.set_ylabel('Gemiddelde Waarde per Meting', color = "#221F20")
    ax1.set_yscale('log')
    ax1.tick_params(axis='x', rotation=0, color = "#221F20")
    ax1.grid(axis='y', linestyle='--', alpha=0.7, color = "#C5C5C4", zorder = 1)
    ax1.legend(title='Metingen', loc='upper left')
    set_axis_color(ax1, "#221F20")

    # Add light grey vertical lines behind values 2, 4, and 6 in the left subplot
    for value in [1.5, 3.5, 5.5]:
        ax1.axvline(x=value - 0.5, color='#f6f6f6', linestyle='-', linewidth=105, zorder = 1)

    # Plotting "bc" data on the right subplot
    bc_data = average_per_zone.loc['bc']
    bc_data.plot(kind='bar', ax=ax2, color=[colors[col] for col in filtered_zones.columns], width=0.9, legend=False, zorder = 3)
    ax2.set_title('Referentie kabinet', color = "#221F20")
    ax2.set_ylabel('Gemiddelde Waarde per Meting', color = "#221F20")
    ax2.tick_params(axis='x', rotation=45, color = "#221F20")
    ax2.grid(axis='y', linestyle='--', alpha=0.7, color = "#C5C5C4", zorder = 1)
    
    # Adjust layout
    plt.tight_layout()
    set_axis_color(ax2, "#221F20")

    # Display the plot
    plt.show()

# Plot the data for corners "lb", "lo", "rb", "ro"
for corner in ['lb', 'lo', 'rb', 'ro']:
    plot_corner(corner)