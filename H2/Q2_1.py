from imports import *

df = pd.read_csv("Data_heating_cooling.csv")
Y = df["Cooling_Load"]

Orientation = df["Orientation"]
OrientationDummies = pd.get_dummies(Orientation, prefix="O", drop_first=True)
print(OrientationDummies)

GAD = df["Glazing_Area_Distribution"]
GADDUmmies = pd.get_dummies(GAD, prefix="GAD", drop_first=True)

#We drop the "Surface_Area" because it is a linear combination of the "Wall_Area" and "Roof_Area" columns
#We drop the "Orientation" column because we changed it in dummy variables
#We drop the "Glazing_Area_Distribution" column because we changed it in dummy variables

#the O_3, O_4, O_5 columns are the dummy variables for the "Orientation" column
#note that O_2 = 1 when O_3 = O_4 = O_5 = 0

#the GAD_1, GAD_2, GAD_3, GAD_4, GAD_5 columns are the dummy variables for the "Glazing_Area_Distribution" column
#note that GAD_0 = 1 when GAD_1 = GAD_2 = GAD_3 = GAD_4 = GAD_5 = 0
X = df.drop(["Surface_Area", "Orientation", "Glazing_Area_Distribution", "Heating_Load", "Cooling_Load"], axis=1)
X.insert(0, "Intercept", np.ones(len(X)), True)
X = X.join(OrientationDummies)
X= X.join(GADDUmmies)

