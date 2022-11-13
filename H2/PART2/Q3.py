from imports import *

from Q1 import df2

Hour = df2["Hour"]
Hourdummies = pd.get_dummies(Hour, prefix="H", drop_first=True)

Weekday = df2["Weekday"]
Weekdaydummies = pd.get_dummies(Weekday, prefix="W", drop_first=True)
print(Hourdummies)
Array = df2.drop(["Hour", "Weekday"], axis=1)
Array.insert(0, "Constant", np.ones(len(Array)), True)

Array = Array.join(Hourdummies)
Array = Array.join(Weekdaydummies)

# Array is now the transformed dataset ! 
# We remove H0 and W1 because they are superfluous.
# We do this conversion because it will then be easier to do the linear regression.

print(Array)

