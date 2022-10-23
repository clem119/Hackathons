from math import *
from turtle import st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats as sc
import random as rn
from Q4 import WindBeauvechain
from Q4 import WindElsenborn

#only keep 500 wind speeds
winds_b = WindBeauvechain[0:500]
winds_e = WindElsenborn[0:500]

#number of bootstrappings
M = 1000

#arrays that will contain the gamma parameters for each resample
alphab =[]
betab = []

#take the wind speed sample, shuffle it and then estimate the parameters with an MLE
for m in np.arange(0,M):
    datm = rn.choices(population=winds_b,k=len(winds_b))
    params = sc.gamma.fit(data=datm,scale=1)
    alphab.append(params[0])
    betab.append(params[2])


alphab = np.sort(alphab)
betab = np.sort(betab)

#taking the lower and upper bounds of the 5% confidence interval
alphab_begin = alphab[25]
alphab_end = alphab[974]

betab_begin = betab[25]
betab_end = betab[974]

print("Beauvechain :")
print("Aplha 5% confidence interval: [",alphab_begin,":",alphab_end,"]")
print("Beta 5% confidence interval: [",betab_begin,":",betab_end,"] \n")

#do the same thing all over again for Elsenborn
alphae =[]
betae = []
for m in np.arange(0,M):
    datm = rn.choices(population=winds_e,k=len(winds_e))
    params = sc.gamma.fit(data=datm,scale=1)
    alphae.append(params[0])
    betae.append(params[2])

alphae = np.sort(alphae)
betae = np.sort(betae)

alphae_begin = alphae[25]
alphae_end = alphae[974]

betae_begin = betae[25]
betae_end = betae[974]

print("Elsenborn :")
print("Aplha 5% confidence interval: [",alphae_begin,":",alphae_end,"]")
print("Beta 5% confidence interval: [",betae_begin,":",betae_end,"] \n")