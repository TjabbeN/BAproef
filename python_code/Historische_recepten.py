import pandas as pd
import matplotlib.pyplot as plt
from set_axis_color import set_axis_color

url = "https://raw.githubusercontent.com/TjabbeN/BAproef/main/data/data_hist_recepten.csv"

df = pd.read_csv(url)

# Count the occurrences of each category
category_counts = df['techniek'].value_counts()

# Plot the frequency of each category
plt.figure(figsize=(14,8))
category_counts.plot(kind='bar', zorder = 2, color = "#CF4C48")
plt.grid(axis = "y", color = "#C5C5C4", zorder = 1)
plt.title('Vermelde polijsttechnieken en -materialen in historische bronnen (1548-1794)', color = "#221F20")
plt.xlabel('Materiaal/techniek', color = "#221F20")
plt.ylabel('Frequentie', color = "#221F20")
plt.xticks(rotation=45, ha='right', color = "#221F20")
plt.tight_layout()

set_axis_color(color = "#221F20")

plt.show()