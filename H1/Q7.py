from math import *
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as sc
import random as rn
from Q4 import WindBeauvechain, WindElsenborn

def Q7(array, place, distribution):

    #only keep 500 wind speeds
    winds = array[:500]

    #number of bootstrappings
    M = 1000

    #arrays that will contain the gamma parameters for each resample
    alpha = []
    beta = []

    #take the wind speed sample, shuffle it and then estimate the parameters with an MLE
    for m in np.arange(0,M):
        datm = rn.choices(population=winds,k=len(winds))
        params = sc.gamma.fit(data=datm,scale=1)
        alpha.append(params[0])
        beta.append(params[2])


    alpha = np.sort(alpha)
    beta = np.sort(beta)

    #taking the lower and upper bounds of the 5% confidence interval
    alpha_begin = alpha[25]
    alpha_end = alpha[974]

    beta_begin = beta[25]
    beta_end = beta[974]

    print(f"{place} :")
    print("Aplha 5% confidence interval: [",alpha_begin,":",alpha_end,"]")
    print("Beta 5% confidence interval: [",beta_begin,":",beta_end,"] \n")

Q7(WindBeauvechain, "Beauvechain")
Q7(WindElsenborn, "Elsenborn")