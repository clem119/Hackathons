from Q1 import ElecPowerCapa
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

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