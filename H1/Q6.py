from math import *
import re
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from Q4 import WindBeauvechain, WindElsenborn
from Q5 import fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv, fitted_alphaElsen, fitted_gammaLocElsen, fitted_scaleGammaElsen

def twoMoments(windfarm):
    n = len(windfarm)
    M1 = np.sum(windfarm)/n
    M2 = 0
    for i in windfarm:
        M2 += i**2
    M2 = M2/n
    return (M1, M2)

def estimators(windfarm):
    span = int(max(windfarm))
    x = np.linspace(0, span, span)

    M1 = twoMoments(windfarm)[0]
    M2 = twoMoments(windfarm)[1]

    # Compute gamma estimators from M1 and M2 
    alpha = M1**2 / (M2 - M1**2)
    scale = sqrt((M2 - M1**2)/alpha)
    print(alpha, scale)
    pdfGammaMM = stats.gamma.pdf(x, a = alpha, scale = scale)
    pdfGammaMLE = stats.gamma.pdf(x, fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv)

    return (pdfGammaMLE, pdfGammaMM)

def plotgraph(windfarm):
    span = int(max(windfarm))
    x = np.linspace(0, span, span)
    fig,ax = plt.subplots() # Instantiate figure and axes object
    ax.hist(windfarm, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA')
    plt.plot(x,estimators(windfarm)[0], label="Gamma fit MLE", color="greenyellow")
    plt.plot(x,estimators(windfarm)[1], label="gamma fit MM", color="forestgreen")
    plt.xlabel("Wind speed (km/h)")
    plt.ylabel("Nb") 
    plt.title("Wind speeds(normed graph)")
    plt.legend()
    plt.show()

plotgraph(WindBeauvechain)
plotgraph(WindElsenborn)