#imports
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def ElecPowerCapa():
    
    #only keep date from 20170101 to 20210101 for Beauvechain
    Beauvechain = pd.read_csv("Beauvechain.csv", sep=",")
    Beauvechain=Beauvechain.loc[Beauvechain["    DATE"] >= 20170101].loc[Beauvechain["    DATE"] <= 20210101]

    #only keep date from 20170101 to 20210101 for Elsenborn
    Elsenborn = pd.read_csv("Elsenborn.csv", sep=",")
    Elsenborn=Elsenborn.loc[Elsenborn["    DATE"] >= 20170101].loc[Elsenborn["    DATE"] <= 20210101]
    
    #put all the non trusted value (!= 0) in ErrorsElsenborn and ErrorsBeauvechain
    ErrorsElsenborn=Elsenborn.loc[Elsenborn[" Q_FG"] != 0] 
    ErrorsBeauvechain=Beauvechain.loc[Beauvechain[" Q_FG"] != 0]

    #Only keep the trusted value
    Elsenborn=Elsenborn[~Elsenborn["    DATE"].isin(ErrorsBeauvechain["    DATE"])]
    Beauvechain=Beauvechain[~Beauvechain["    DATE"].isin(ErrorsElsenborn["    DATE"])]

    #if the wind speed is higher than 90km/h then set the value in the table to 0
    #and if the wind speed is negative, then delete the line from the file
    Elsenborn=Elsenborn.loc[Elsenborn["   FG"] >=0]
    Elsenborn.loc[Elsenborn["   FG"] > 90, "   FG"] = 0 
    Beauvechain=Beauvechain.loc[Beauvechain["   FG"] >=0]
    Beauvechain.loc[Beauvechain["   FG"] > 90, "   FG"] = 0

    #constant variables
    PI = math.pi
    RHO = 1.2
    S = (32**2)*PI
    
    #variables
    ResBeauvechain=[]
    ResElsenborn=[]

    # for each day speed in Elsenborn, append the electric power in the final result
    for i in Elsenborn["   FG"]:
        wSpeed = (i/3.6)**3
        Pk=8*0.5*RHO*S*wSpeed
        Pe = Pk*0.42 #because of the betz limit
        Pe = Pe/(10**6) #convert  in MW
        ResElsenborn.append(Pe) 

    for i in Beauvechain["   FG"]:
        wSpeed = (i/3.6)**3
        Pk=8*0.5*RHO*S*wSpeed
        Pe = Pk*0.42 #because of the betz limit
        Pe = Pe/(10**6) #convert  in MW
        ResBeauvechain.append(Pe) 

    #adds the value from beauvechain and elsenborn one by one
    #power measured in W
    FinalRes = (ResElsenborn, ResBeauvechain)
    return FinalRes