import pandas as pd

df = pd.read_csv('epl.csv')
df.plot(kind="scatter", x="timestamp", y="attendance")
