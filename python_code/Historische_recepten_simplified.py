import pandas as pd
import matplotlib.pyplot as plt
from set_axis_color import set_axis_color

url = "https://raw.githubusercontent.com/TjabbeN/BAproef/main/data/data_hist_recepten.csv"

df = pd.read_csv(url)

# Function to simplify categories
def simplify_category(category):
    # Split category by '(' and take the first part
    simplified_category = category.split('(')[0].strip()
    return simplified_category

# Apply the function to the 'techniek' column
df['simplified_techniek'] = df['techniek'].apply(simplify_category)

# Count the occurrences of each simplified category
category_counts = df['simplified_techniek'].value_counts()

# Group categories with less than or equal to 2 elements into 'Others'
threshold = 2
other_categories = category_counts[category_counts <= threshold].index
df['simplified_techniek'] = df['simplified_techniek'].replace(other_categories, 'Overige technieken')

# Count the occurrences of each simplified category after grouping
simplified_category_counts = df['simplified_techniek'].value_counts()

# Plot the frequency of the 'Others' category
plt.figure(figsize=(14,8))
simplified_category_counts.plot(kind='bar', zorder = 2, color = "#CF4C48")
plt.grid(axis = "y", zorder = 1, color = "#C5C5C4")
plt.title('Vermelde polijsttechnieken en -materialen per hoofdcategorie in historische bronnen (1548-1794)', color = "#221F20")
plt.xlabel('Categorie', color = "#221F20")
plt.ylabel('Frequentie', color = "#221F20")
plt.xticks(rotation=45, ha='right', color = "#221F20")
plt.tight_layout()

set_axis_color(color = "#221F20")

plt.show()