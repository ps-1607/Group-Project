import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("singapore_avg_september.csv", parse_dates=['DATE'])
print("Original Data")
print(df.keys())

print(type(df['TAVG'][1]))
df['TAVG'] = df['TAVG'].astype(float)

plt.plot(df['DATE'], df['TAVG'])
plt.show()