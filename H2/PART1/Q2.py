from imports import *

df = pd.read_csv("Data_heating_cooling.csv")
Y = df["Cooling_Load"]

Orientation = df["Orientation"]
OrientationDummies = pd.get_dummies(Orientation, prefix="O", drop_first=True)

GAD = df["Glazing_Area_Distribution"]
GADDUmmies = pd.get_dummies(GAD, prefix="GAD", drop_first=True)
print(GADDUmmies)
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


#part 1
#computing the linear regression
mod = sm.OLS(Y,X)
f1 = mod.fit()

#part 2

#getting the coefs, p-values and intercept
coefs = f1.summary2().tables[1]['Coef.']
p_values = f1.pvalues
print(p_values)

#print answers
print("=============================================")
print('F-Statistic: ',f1.fvalue)
print('R2: ',f1.rsquared)
print("=============================================\n")

print("=============================================")
print(f"p-values:\n\n{p_values[1:]}")
print("=============================================\n")

# #according to the course method
# x = X.to_numpy()
# y = Y.to_numpy()

# xtx = np.matmul(x.transpose(), x)
# xty = np.matmul(x.transpose(), y)
# xtxinv = np.linalg.inv(xtx)
# betaHat = np.matmul(xtxinv, xty)
# print(fii.summary2())
# print("\nvalues obtained by matrices operations:")
# for i in betaHat: print(i)