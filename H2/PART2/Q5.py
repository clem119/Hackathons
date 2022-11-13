from imports import *
from Q4 import test

Y = test["Load"]

X = test.drop(["Date", "Hour", "Weekday", "Load"], axis=1)

Hour = test["Hour"]
Hourdummies = pd.get_dummies(Hour, prefix="H", drop_first=True)

Weekday = test["Weekday"]
Weekdaydummies = pd.get_dummies(Weekday, prefix="W", drop_first=True)

X = X.join(Hourdummies)
X = X.join(Weekdaydummies)

mod = sm.OLS(Y, X)
f2 = mod.fit()


coefs = f2.summary2().tables[1]['Coef.']
print(coefs)

