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

#Graph
fig = plt.figure(figsize=(15,10))
plt.hist(WindBeauvechain, bins=100, color='green', edgecolor='black')
plt.hist(WindElsenborn, bins=100, color='blue', edgecolor='black')

fig.legend(labels=['Beauvechain','Elsenborn'])
plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds compared in Beauvechain and Elsenborn")

plt.show()