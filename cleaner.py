import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Replace Calories with Average
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

# Remove rows with Duration > 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# Drop duplicate rows
df.drop_duplicates(inplace = True)

df.plot()
# Save plot as PNG
plt.savefig('plot.png')

# Print to Terminal
print(df.to_string())
