import time
import math
from typing import List
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def ElecPowerCapa():
    
    #only keep date from 20170101 to 20210101 for beauvechain
    Beauvechain = pd.read_csv("H1/Beauvechain.csv", sep=",")
    Beauvechain=Beauvechain.loc[Beauvechain["    DATE"] >= 20170101].loc[Beauvechain["    DATE"] <= 20210101]

    #only keep date from 20170101 to 20210101 for Elsenborn
    Elsenborn = pd.read_csv("H1/Elsenborn.csv", sep=",")
    Elsenborn=Elsenborn.loc[Elsenborn["    DATE"] >= 20170101].loc[Elsenborn["    DATE"] <= 20210101]
    
    #put all the non trusted value (!= 0) in ErrorsElsenborn and ErrorsBeauvechain
    ErrorsElsenborn=Elsenborn.loc[Elsenborn[" Q_FG"] != 0] 
    ErrorsBeauvechain=Beauvechain.loc[Beauvechain[" Q_FG"] != 0]

    #Only keep the trust value
    Elsenborn=Elsenborn[~Elsenborn["    DATE"].isin(ErrorsBeauvechain["    DATE"])]
    Beauvechain=Beauvechain[~Beauvechain["    DATE"].isin(ErrorsElsenborn["    DATE"])]

    #if the with is higher than 90km/h set the value in the table to 0
    Elsenborn=Elsenborn.loc[Elsenborn["   FG"] >=0]
    Elsenborn.loc[Elsenborn["   FG"] > 90, "   FG"] = 0 
    Beauvechain=Beauvechain.loc[Beauvechain["   FG"] >=0]
    Beauvechain.loc[Beauvechain["   FG"] > 90, "   FG"] = 0

    #constantes imposées dans l'énoncé
    PI = math.pi
    RHO = 1.2
    SPEEDLIMIT = 90/3.6 # en m/s
    Pk = 0
    beauvechain = None
    elsenborn = None
    nDays=0
    ItB=0 #itérateur pour beauvechain
    ItE=0 #itérateur pour elsenborn
    res=[]

    for i in Elsenborn["   FG"]:
        Pk=8*0.5*RHO*((32**2)*PI)*(i/3.6)**3
        res.append(Pk*0.42)

    for i in Beauvechain["   FG"]:
        Pk+=8*0.5*RHO*((32**2)*PI)*(i/3.6)**3
        res.append(Pk*0.42)

    return np.array(res)/(10**6)

##########################
res = ElecPowerCapa()
for i in res: print(i)

max=np.max(res)
bins = [] # bins est l'argument qui permet de répartir les données en un certain nombre de barres verticales
for i in range(50): bins.append(i*max/50) # ici, l'argument bins est une liste qui comprend 50 intervales croissant linéairement entre 0 et la puissance max

plt.hist(res, bins=bins, edgecolor='black')
plt.xlabel("Electric power capacity (MW)")
plt.ylabel("Nombre d'occurrences") 
plt.title("Electric power capacity (MW) from the 1/1/2017 to the 1/1/2021")
plt.show()
