from math import *
import re
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from Q4 import WindBeauvechain, WindElsenborn, getDistributionParameters

def Q6(array, place):

    #get the gamma distribution parameters with MLE
    alpha, loc, scale = getDistributionParameters(array)[0]

    #takes the highest wind
    span = int(max(array))
    x = np.linspace(0, span, span)

    fig,ax = plt.subplots() # Instantiate figure and axes object
    ax.hist(array, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label=f'{place} DATA')

    # Compute the value of the two moments
    M1 = np.mean(array)
    M2 = 0
    for i in array:
        M2 += i**2
    M2 = M2/len(array)

    # Compute gamma estimators from M1 and M2 
    alphaMM = M1**2 / (M2 - M1**2)
    betaMM = sqrt((M2 - M1**2)/alphaMM)

    pdfGammaMLE = stats.gamma.pdf(x, a = alphaMM, scale = betaMM)
    pdfGammaMM = stats.gamma.pdf(x, alpha, loc, scale)

    print("=====================================================================")
    print(f"Comparing estimators for both methods (MM and MLE) for {place}:")
    print(f"alpha (Method of moments): {alphaMM}")
    print(f"beta (Method of moments): {betaMM}")
    print(f"alpha (MLE): {alpha}")
    print(f"alpha (MLE): {scale}")
    print("=====================================================================\n")

    plt.plot(x,pdfGammaMLE, label="Gamma fit MLE")
    plt.plot(x,pdfGammaMM, label="gamma fit MM")
    plt.xlabel("Wind speed (km/h)")
    plt.ylabel("Nb") 
    plt.title(f"Wind speeds in {place}(normed graph)")
    plt.legend()
    plt.show()

Q6(WindBeauvechain, "Beauvechain")
Q6(WindElsenborn, "Elsenborn")

