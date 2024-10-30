import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("countries-table.csv")
df = df.dropna()
print(df)

plt.pie(df['worldPercentage'], labels=df['country'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('World Percentage by Country')
plt.show()