from imports import *

from Q1 import df

X = []
Mean = 0
Counter = 0
index = 0
# Average electric consumption per day (y axis) versus weekday (x axis)
def AverageDay():
    for i in df["Load"]:
        Counter+=1
        if(Counter != 23):
            Mean += i
        else: 
            Mean = Mean / 23
            X[index] = Mean
            Mean = 0
            index+=1
    return

AverageDay

print(X)

plt.xlabel("Weekday")
plt.ylabel("Electric Consumption")
plt.show()