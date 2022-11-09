from imports import *

df = pd.read_csv("Data_heating_cooling.csv", sep=",")

keys = "Relative_Compactness,Surface_Area,Wall_Area,Roof_Area,Overall_Height,Orientation,Glazing_Area,Glazing_Area_Distribution,Heating_Load,Cooling_Load".split(",")

for i in keys:
    array = np.array(df[i])
    print("=============================================\n")
    print(f"Useful statistics for {i}:")
    print(f"mean: {array.mean()}")
    print(f"standard deviation: {array.std()}")
    #print(f"heatmap correlations: {array.corrcoef()}")
    print("=============================================\n")

sns.heatmap(df.corr())
plt.show()

