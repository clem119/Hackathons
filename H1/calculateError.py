import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from Q4 import WindBeauvechain, WindElsenborn

def ComputeError(array):

    span=int(max(array))
    x = np.linspace(0, span, span+1)

    #takes gamma parameters
    shapeG, locationG, scaleG  = stats.gamma.fit(array)

    #takes invert gauss parameters
    shapeI, locationI, scaleI = stats.invgauss.fit(array)

    gammaPdf = stats.gamma.pdf(x, shapeG, loc=locationG, scale=scaleG) #store all the value of the gamma pdf for each percitil
    invGaussPdf = stats.invgauss.pdf(x, shapeI, loc=locationI, scale=scaleI) #store all the value of the inverte gauss pdf for each percentil
    #creates an array that has the amount of value for each value of MW rounded
    
    def makeArray(span):
        a = np.zeros(span+1)
        for i in array:
            a[i] += 1
        return a

    totalErrorGamma = 0
    totalErrorInvGauss = 0

    #computes the error by taking the difference between the curve and the real value (rounded)
    L = makeArray(span)
    for i in range(span):
        totalErrorGamma += (gammaPdf[i] - L[i])**2
        totalErrorInvGauss += (invGaussPdf[i] - L[i])**2

    print("total error gamma: ", totalErrorGamma)
    print("total error inverte Gauss: ",totalErrorInvGauss)


    plt.plot(x, gammaPdf)
    plt.plot(x, invGaussPdf)

    plt.show()

ComputeError(WindBeauvechain) # compute error for Elsenborn
ComputeError(WindElsenborn) # compute error for Beauvechain (doesn't work)