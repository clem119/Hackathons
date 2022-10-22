from Q1 import ElecPowerCapa
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

#only keep date from 20170101 to 20210101 for Beauvechain
Beauvechain = pd.read_csv("Beauvechain.csv", sep=",")

#only keep date from 20170101 to 20210101 for Elsenborn
Elsenborn = pd.read_csv("Elsenborn.csv", sep=",")

#remove negative wind speeds
Elsenborn=Elsenborn.loc[Elsenborn["   FG"] >= 0]
Beauvechain=Beauvechain.loc[Beauvechain["   FG"] >= 0]


#put all the non trusted value (!= 0) in ErrorsElsenborn and ErrorsBeauvechain
ErrorsElsenborn=Elsenborn.loc[Elsenborn[" Q_FG"] != 0]
ErrorsBeauvechain=Beauvechain.loc[Beauvechain[" Q_FG"] != 0]

#only keep the wind speed values
WindBeauvechain = np.array(Beauvechain["   FG"])
WindElsenborn = np.array(Elsenborn["   FG"])

def windFarmBestDistribution(windFarmWinds):
    span = int(max(windFarmWinds))
    fig, ax = plt.subplots()
    ax.hist(windFarmWinds, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA') # Plot histogram of nums1



    #used get value of the pdf for the highest value of wind registered
    x = np.linspace(0, span, span)

    #Gamma distribution
    #takes gamma parameters
    fitted_alphaB, fitted_gammaLocB, fitted_scaleGammaB = stats.gamma.fit(windFarmWinds)
    gammaPdf = stats.gamma.pdf(x, fitted_alphaB, fitted_gammaLocB, fitted_scaleGammaB)

    #Invert Gauss distribution
    #takes invert gauss parameters
    fitted_muB, fitted_invgaussLocB, fitted_scaleInvGaussB = stats.invgauss.fit(windFarmWinds)
    invGaussPdf = stats.invgauss.pdf(x, fitted_muB, fitted_invgaussLocB, fitted_scaleInvGaussB)

    #print(WindBeauvechain)
    #print("invert gaussian value: ",invGaussPdf)
    #print("gamma values: ", gammaPdf)
    #define x-axis values


    #statGamma, p_valueGamma = ttest_ind(WindBeauvechain, gammaPdf)
    #print("stat:", statGamma)
    #print("pvalue:", p_valueGamma)

    #create plot of Gamma distribution
    plt.plot(x, gammaPdf)
    plt.plot(x, invGaussPdf)

    #display plot
    plt.show()

windFarmBestDistribution(WindBeauvechain)
windFarmBestDistribution(WindElsenborn)
