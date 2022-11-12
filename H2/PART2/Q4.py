from imports import *
from Q1 import df2

#dates
time1 = pd.Timestamp('20150102')
time2 = pd.Timestamp('20180112')
time3 = pd.Timestamp('20181202')
time4 = pd.Timestamp('20181231')


training_set = df2.loc[df2["Date"] <= time2]
test = df2.loc[df2["Date"] >= time3].loc[df2["Date"] <= time4]

#print(training_set)
for i in df2["Date"]: print(i)

#print(test)

