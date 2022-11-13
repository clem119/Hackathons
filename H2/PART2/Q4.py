from imports import *
from Q1 import df2


#dates
time1 = pd.Timestamp('20150102')
time2 = pd.Timestamp('20181201')
time3 = pd.Timestamp('20181202')
time4 = pd.Timestamp('20181231')

training_set = df2.loc[df2["Date"] <= time2]
test = df2.loc[df2["Date"] >= time3].loc[df2["Date"] <= time4]

#print(training_set)
#for i in df2["Date"]: print(i)

#print(test)

Y = training_set["Load"]

X = training_set.drop(["Date", "Hour", "Weekday", "Load"], axis=1)

Hour = training_set["Hour"]
Hourdummies = pd.get_dummies(Hour, prefix="H", drop_first=True)

Weekday = training_set["Weekday"]
Weekdaydummies = pd.get_dummies(Weekday, prefix="W", drop_first=True)

X = X.join(Hourdummies)
X = X.join(Weekdaydummies)

mod = sm.OLS(Y, X)
f2 = mod.fit()


coefs = f2.summary2().tables[1]['Coef.']
print(coefs)
