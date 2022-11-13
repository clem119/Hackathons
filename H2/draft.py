import pandas as pd
from PART2.Q1 import df2

df2 = df2.loc[df2["Hour"] == 13]
print(df2)

d1 = pd.Timestamp(2013, 4, 4)
d2 = pd.Timestamp(2012, 4, 4)
print(d1 > d2)