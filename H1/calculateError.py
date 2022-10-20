
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q1 import ElecPowerCapa

electroCapa = ElecPowerCapa()[0]
etendue = round(max(ElecPowerCapa()[0]))

#takes gamma parameters
shapeGammaElsenborn,locationGammaElsenborn,scaleGammaElsenborn  = stats.gamma.fit(electroCapa)


#takes invert gauss parameters
shapeInvGaussElsenborn, locationInvGaussElsenborn, scaleInvGaussElsenborn = stats.invgauss.fit(electroCapa)

x = np.linspace (0, etendue, etendue) #creat an array with of percentil

gammaPdf = stats.gamma.pdf(x, shapeGammaElsenborn, loc=locationGammaElsenborn, scale=scaleGammaElsenborn) #store all the value of the gamma pdf for each percitil
invGaussPdf = stats.invgauss.pdf(x, shapeInvGaussElsenborn, loc=locationInvGaussElsenborn, scale=scaleInvGaussElsenborn) #store all the value of the inverte gauss pdf for each percentil

#creates an array that has the amount of value for each value of MW rounded
def makeArray(etendue):
    a = np.empty(etendue)
    for i in range(etendue-1):
        a[round(electroCapa[i])] += 1

    return a

totalErrorGamma = 0
totalErrorInvGauss = 0
#computes the error by taking the difference between the curve and the real value (rounded)
for i in range(etendue):
    totalErrorGamma += (gammaPdf[i] - makeArray(etendue)[i])**2
    totalErrorInvGauss += (invGaussPdf[i] - makeArray(etendue)[i])**2

print("total error gamma: ", totalErrorGamma)
print("total error inverte Gauss: ",totalErrorInvGauss)


plt.plot(x, gammaPdf)
plt.plot(x, invGaussPdf)

plt.show()



############################################################""

# R = ElecPowerCapa()

# def ComputeError(array):

#     span=round(max(array))

#     #takes gamma parameters
#     shapeG, locationG, scaleG  = stats.gamma.fit(electroCapa)


#     #takes invert gauss parameters
#     shapeI, locationI, scaleI = stats.invgauss.fit(electroCapa)

#     x = np.linspace (0, span, span) #creates an array with of percentil

#     gammaPdf = stats.gamma.pdf(x, shapeG, loc=locationG, scale=scaleG) #store all the value of the gamma pdf for each percitil
#     invGaussPdf = stats.invgauss.pdf(x, shapeI, loc=locationI, scale=scaleI) #store all the value of the inverte gauss pdf for each percentil

#     #creates an array that has the amount of value for each value of MW rounded
#     def makeArray(span):
#         a = np.empty(span)
#         for i in range(span-1):
#             a[round(array[i])] += 1
#         return a

#     totalErrorGamma = 0
#     totalErrorInvGauss = 0

#     #computes the error by taking the difference between the curve and the real value (rounded)
#     for i in range(span):
#         totalErrorGamma += (gammaPdf[i] - makeArray(span)[i])**2
#         totalErrorInvGauss += (invGaussPdf[i] - makeArray(span)[i])**2

#     print("total error gamma: ", totalErrorGamma)
#     print("total error inverte Gauss: ",totalErrorInvGauss)


#     plt.plot(x, gammaPdf)
#     plt.plot(x, invGaussPdf)

#     plt.show()

# ComputeError(R[0])
# ComputeError(R[1])