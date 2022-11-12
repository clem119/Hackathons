from imports import *

from Q1 import df2

####################
## Sub-Question 1 ## Average electric consumption per day (y axis) versus weekday (x axis)
####################

print(df2)

week = []
for i in range(1,8):
    week.append(
        np.mean(np.array(df2.loc[df2["Weekday"] == i, "Load"]))
    )

#print(WeekDays)
bins1 = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
x1 = [i for i in range(1,8)]

####################
## Sub-Question 2 ## Average electric consumption per hour(y axis) versus hour (x axis)
####################

hours = []
for i in range(24):
    hours.append(
        np.mean(np.array(df2.loc[df2["Hour"] == i, "Load"]))
    )

bins2 = [f"H{i}" for i in range(24)]
x2 = [i for i in range(24)]


#plot
fig1, ax1 = plt.subplots(figsize=(15, 10))
plt.bar(x1, week, color="silver")
plt.plot(x1, week, marker = 'o', linewidth=3, color="slateblue")
plt.xlabel("Weekday")
plt.ylabel("Electric Consumption")
plt.title("Average electric consumption per day")
plt.xticks(x1, bins1)

fig2, ax2 = plt.subplots(figsize=(15, 10))
plt.bar(x2, hours, color="silver")
plt.plot(x2, hours, marker='o', linewidth=3, color="slateblue")
plt.xlabel("Hours")
plt.ylabel("Electric Consumption")
plt.title("Average electric consumption per hour")
plt.xticks(x2, bins2)
plt.show()