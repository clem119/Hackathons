import time
import math
import pandas as pd

def ElecPowerCapa():

    Beauvechain = pd.read_csv("Beauvechain.csv", sep=",")
    Beauvechain=Beauvechain.loc[Beauvechain["    DATE"] >= 20170101].loc[Beauvechain["    DATE"] <= 20210101]

    Elsenborn = pd.read_csv("Elsenborn.csv", sep=",")
    Elsenborn=Elsenborn.loc[Elsenborn["    DATE"] >= 20170101].loc[Elsenborn["    DATE"] <= 20210101]
    
    ErrorsElsenborn=Elsenborn.loc[Elsenborn[" Q_FG"] != 0]
    ErrorsBeauvechain=Beauvechain.loc[Beauvechain[" Q_FG"] != 0]

    Elsenborn=Elsenborn[~Elsenborn["    DATE"].isin(ErrorsBeauvechain["    DATE"])]
    Beauvechain=Beauvechain[~Beauvechain["    DATE"].isin(ErrorsElsenborn["    DATE"])]

    Elsenborn=Elsenborn.loc[Elsenborn["   FG"] >=0]
    Beauvechain=Beauvechain.loc[Beauvechain["   FG"] >=0]


    print(Elsenborn)

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

 

    Pe = 0.42*Pk
    return Pe

##########################

ElecPowerCapa()
