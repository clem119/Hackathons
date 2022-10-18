from Q1 import ElecPowerCapa
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

fig = plt.figure(figsize=(20,20))

#only keep date from 20170101 to 20210101 for Beauvechain
Beauvechain = pd.read_csv("H1/Beauvechain.csv", sep=",")

#only keep date from 20170101 to 20210101 for Elsenborn
Elsenborn = pd.read_csv("H1/Elsenborn.csv", sep=",")

#remove negative wind speeds
Elsenborn=Elsenborn.loc[Elsenborn["   FG"] >= 0]
Beauvechain=Beauvechain.loc[Beauvechain["   FG"] >= 0]


#put all the non trusted value (!= 0) in ErrorsElsenborn and ErrorsBeauvechain
ErrorsElsenborn=Elsenborn.loc[Elsenborn[" Q_FG"] != 0]
ErrorsBeauvechain=Beauvechain.loc[Beauvechain[" Q_FG"] != 0]

#only keep the wind speed values
WindBeauvechain = np.array(Beauvechain["   FG"])
WindElsenborn = np.array(Elsenborn["   FG"])

#concatenates both of the arrays
Results=np.concatenate((WindElsenborn, WindBeauvechain))

# plot param
gamma = stats.gamma
a, loc, scale = 3, 0, 2
size = len(Results)

x = np.linspace(0, Results.max(), len(Results))
# fit
param = gamma.fit(Results, floc=0)
pdf_fitted = gamma.pdf(x, *param)
plt.plot(x, pdf_fitted, color='r')

plt.hist(Results, bins=30)
# plt.hist(Results, bins=100, edgecolor='black')

# plt.xlabel("Wind speed (km/h)")
# plt.ylabel("Nb of occurrence") 
# plt.title("Wind speeds in Beavechain and Elsenborn")
# fig.legend(labels=['Data'])

plt.show()