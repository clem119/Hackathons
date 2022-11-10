from imports import *

df1 = pd.read_csv("H2/Data_heating_cooling.csv", sep=",")

keys = "Relative_Compactness,Surface_Area,Wall_Area,Roof_Area,Overall_Height,Orientation,Glazing_Area,Glazing_Area_Distribution,Heating_Load,Cooling_Load".split(",")
statnames = "mean,std,min,25%,50%,75%,max".split(",")

statistics = df1.describe()
print(statistics)

#print answers
for i in keys:
    print("=============================================\n")
    print(f"{i}\n\n{statistics[i]}")
    print("=============================================\n")


#plot
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(df1.corr())
plt.title("Heatmap of correlations")
plt.show()

