from imports import *

from Q1 import df

Hour = df["Hour"]
Hourdummies = pd.get_dummies(Hour, prefix="H", drop_first=True)

Weekday = df["Weekday"]
Weekdaydummies = pd.get_dummies(Weekday, prefix="W", drop_first=True)

Array = df.drop(["Hour", "Weekday"], axis=1)
Array.insert(0, "Constant", np.ones(len(Array)), True)

Array = Array.join(Hourdummies)
Array = Array.join(Weekdaydummies)

print(Array)
