import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Replace Calories with Average
average_calories = df["Calories"].mean()
df["Calories"].fillna(average_calories, inplace = True)

# Remove rows with Duration > 120
for row in df.index:
  if df.loc[row, "Duration"] > 120:
    df.drop(row, inplace = True)

# Drop Date column
df.drop("Date", axis = 1, inplace = True)

# Drop duplicate rows
df.drop_duplicates(inplace = True)

# Create the plot
df.plot()

# Save plot as PNG
plt.savefig('plot.png')

# Print to Terminal
print(df.to_string())
