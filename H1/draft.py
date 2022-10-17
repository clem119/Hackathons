import Q1
import time
import math
from typing import List
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#only keep date from 20170101 to 20210101 for Beauvechain
Beauvechain = pd.read_csv("H1/Beauvechain.csv", sep=",")
Beauvechain=Beauvechain.loc[Beauvechain["    DATE"] >= 20170101].loc[Beauvechain["    DATE"] <= 20210101]#.loc[Beauvechain["   FG"] <= 90]

#only keep date from 20170101 to 20210101 for Elsenborn
Elsenborn = pd.read_csv("H1/Elsenborn.csv", sep=",")
Elsenborn=Elsenborn.loc[Elsenborn["    DATE"] >= 20170101].loc[Elsenborn["    DATE"] <= 20210101]#.loc[Elsenborn["   FG"] <= 90]

WindBeauvechain = np.array(Beauvechain["   FG"])
WindElsenborn = np.array(Elsenborn["   FG"])


Results=np.concatenate((WindElsenborn, WindBeauvechain))

N=0
for i in Results:
    if(i<=0 or i>90): N+=1

print(N)

# max=np.max(Results)
# bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
# nb=100
# for i in range(nb): bins.append(i*max/nb) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

# plt.hist(Results, bins=bins, edgecolor='black')
# plt.xlabel("Electric power capacity (MW)")
# plt.ylabel("Nb") 
# plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021")
# plt.show()