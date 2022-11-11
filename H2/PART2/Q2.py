from imports import *

from Q1 import df2

####################
## Sub-Question 1 ## Average electric consumption per day (y axis) versus weekday (x axis)
####################

Monday = np.mean(np.array(df2.loc[df2["Weekday"] == 1, "Load"]))
Tuesday = np.mean(np.array(df2.loc[df2["Weekday"] == 2, "Load"]))
Wednesday = np.mean(np.array(df2.loc[df2["Weekday"] == 3, "Load"]))
Thursday = np.mean(np.array(df2.loc[df2["Weekday"] == 4, "Load"]))
Friday = np.mean(np.array(df2.loc[df2["Weekday"] == 5, "Load"]))
Saturday = np.mean(np.array(df2.loc[df2["Weekday"] == 6, "Load"]))
Sunday = np.mean(np.array(df2.loc[df2["Weekday"] == 7, "Load"]))

WeekDays = np.array([Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday])
#print(WeekDays)
a_bins = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
x = [1, 2, 3, 4, 5, 6, 7]

#plt.hist(WeekDays, bins=7, color="mediumseagreen", edgecolor="slategrey")
plt.plot(x, WeekDays, alpha = 0.8, marker = 'o')
plt.xlabel("Weekday")
plt.ylabel("Electric Consumption")
plt.title("Average electric consumption per day")
plt.xticks(x, a_bins)
plt.show()

####################
## Sub-Question 2 ## Average electric consumption per hour(y axis) versus hour (x axis)
####################

H0 = np.mean(np.array(df2.loc[df2["Hour"] == 0, "Load"]))
H1 = np.mean(np.array(df2.loc[df2["Hour"] == 1, "Load"]))
H2 = np.mean(np.array(df2.loc[df2["Hour"] == 2, "Load"]))
H3 = np.mean(np.array(df2.loc[df2["Hour"] == 3, "Load"]))
H4 = np.mean(np.array(df2.loc[df2["Hour"] == 4, "Load"]))
H5 = np.mean(np.array(df2.loc[df2["Hour"] == 5, "Load"]))
H6 = np.mean(np.array(df2.loc[df2["Hour"] == 6, "Load"]))
H7 = np.mean(np.array(df2.loc[df2["Hour"] == 7, "Load"]))
H8 = np.mean(np.array(df2.loc[df2["Hour"] == 8, "Load"]))
H9 = np.mean(np.array(df2.loc[df2["Hour"] == 9, "Load"]))
H10 = np.mean(np.array(df2.loc[df2["Hour"] == 10, "Load"]))
H11 = np.mean(np.array(df2.loc[df2["Hour"] == 11, "Load"]))
H12 = np.mean(np.array(df2.loc[df2["Hour"] == 12, "Load"]))
H13 = np.mean(np.array(df2.loc[df2["Hour"] == 13, "Load"]))
H14 = np.mean(np.array(df2.loc[df2["Hour"] == 14, "Load"]))
H15 = np.mean(np.array(df2.loc[df2["Hour"] == 15, "Load"]))
H16 = np.mean(np.array(df2.loc[df2["Hour"] == 16, "Load"]))
H17 = np.mean(np.array(df2.loc[df2["Hour"] == 17, "Load"]))
H18 = np.mean(np.array(df2.loc[df2["Hour"] == 18, "Load"]))
H19 = np.mean(np.array(df2.loc[df2["Hour"] == 19, "Load"]))
H20 = np.mean(np.array(df2.loc[df2["Hour"] == 20, "Load"]))
H21 = np.mean(np.array(df2.loc[df2["Hour"] == 21, "Load"]))
H22 = np.mean(np.array(df2.loc[df2["Hour"] == 22, "Load"]))
H23 = np.mean(np.array(df2.loc[df2["Hour"] == 23, "Load"]))

Avrg_per_hour = np.array([H0, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15, H16, H17, H18, H19, H20, H21, H22, H23])
new_a_bins = ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H17", "H18", "H19", "H20", "H21", "H22", "H23"]
new_x = [i for i in range(24)]

plt.plot(new_x, Avrg_per_hour, alpha=0.8, marker='o')
plt.xlabel("Hours")
plt.ylabel("Electric Consumption")
plt.title("Average electric consumption per hour")
plt.xticks(new_x, new_a_bins)
plt.show()



#X = []
#Mean = 0
#Counter = 0
#index = 0
# Average electric consumption per day (y axis) versus weekday (x axis)
#def AverageDay():
#    for i in df2["Load"]:
#        Counter+=1
#        if(Counter != 23):
#            Mean += i
#        else: 
#            Mean = Mean / 23
#            X[index] = Mean
#            Mean = 0
#            index+=1
#    return

#AverageDay
