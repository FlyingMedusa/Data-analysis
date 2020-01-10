import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_read = pd.read_csv('multiTimeline.csv', header=1)
print("\nFirst 5: \n", df_read.head())
print("\nLast 5: \n", df_read.tail())

# Row values for index 100
row100 = df_read.iloc[100]
print("\n", row100)

df_read.rename(columns={
    "crossfit: (Cały świat)": "crossfit",
    "python: (Cały świat)": "python",
    "tofu: (Cały świat)": "tofu",
    "Miesiąc": "date"
}, inplace=True)

print("\n", df_read[df_read['date'] == '2019-01'])
print("\n", df_read[(df_read['date'] > '2019-09')])
print("\n", df_read[(df_read['date'] > '2018-01') & (df_read['date'] < '2018-05')])
print("\n", df_read[(df_read['python'] > 90) | (df_read['python'] < 30)])

df_copy = df_read.copy()
df_copy.loc[df_copy['date'] == '2019-12', 'python'] = 100
print("\n", df_copy.tail())

df_read['crossfit'] = df_read['crossfit'].str.replace('<', '')
df_read.info()
df_read['date'] = df_read['date'].astype('datetime64')
df_read['crossfit'] = df_read['crossfit'].astype('int64')
df_read.info()

print("\n", df_read[df_read['crossfit'] > df_read['python']])
print(df_read[['crossfit', 'python', 'tofu']].max())
print(df_read[['crossfit', 'python', 'tofu']].min())
df_read['year'] = df_read['date'].dt.year
print(df_read)
