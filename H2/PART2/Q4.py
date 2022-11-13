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
def predictData(data):
    Y = data["Load"]

    X = data.drop(["Date", "Hour", "Weekday", "Load"], axis=1)
    Hourdummies = pd.get_dummies(data["Hour"], prefix="H", drop_first=True)
    Weekdaydummies = pd.get_dummies(data["Weekday"], prefix="W", drop_first=True)

    X = X.join(Hourdummies)
    X = X.join(Weekdaydummies)

    mod = sm.OLS(Y, X)
    f2 = mod.fit()

    Res = f2.predict(X) #predict next value based on past value (lm1, lm2,...)
    return Res

trainingPredictedValue = predictData(training_set)

print("predicted values for the training set: \n", trainingPredictedValue)

TrainingSetError = mae(training_set["Load"], trainingPredictedValue)

print("Mean absolute error for the training set ", TrainingSetError)
