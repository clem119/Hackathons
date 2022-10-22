
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q1 import ElecPowerCapa

R = ElecPowerCapa()

def ComputeError(array):

    span=round(max(array)+1)

    #takes gamma parameters
    shapeG, locationG, scaleG  = stats.gamma.fit(array)


    #takes invert gauss parameters
    shapeI, locationI, scaleI = stats.invgauss.fit(array)

    x = np.linspace (0, 110, 110) #creates an array with of percentil
    print(x)
    gammaPdf = stats.gamma.pdf(x, shapeG, loc=locationG, scale=scaleG) #store all the value of the gamma pdf for each percitil
    invGaussPdf = stats.invgauss.pdf(x, shapeI, loc=locationI, scale=scaleI) #store all the value of the inverte gauss pdf for each percentil
    #creates an array that has the amount of value for each value of MW rounded
    def makeArray(span):
        a = np.empty(span)
        for i in range(span-1):
            a[round(array[i])] += 1
        return a

    totalErrorGamma = 0
    totalErrorInvGauss = 0

    #computes the error by taking the difference between the curve and the real value (rounded)
    for i in range(span):
        totalErrorGamma += (gammaPdf[i] - makeArray(span)[i])**2
        totalErrorInvGauss += (invGaussPdf[i] - makeArray(span)[i])**2

    print("total error gamma: ", totalErrorGamma)
    print("total error inverte Gauss: ",totalErrorInvGauss)


    plt.plot(x, gammaPdf)
    plt.plot(x, invGaussPdf)

    plt.show()

ComputeError(R[0]) # compute error for Elsenborn
ComputeError(R[1]) # compute error for Beauvechain (doesn't work)