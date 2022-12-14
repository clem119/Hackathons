import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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

def getDistributionParameters(windFarmWinds):

    #Gamma distribution
    #takes gamma parameters
    alpha, gammaLoc, scaleGamma = stats.gamma.fit(windFarmWinds)

    #Invert Gauss distribution
    #takes invert gauss parameters
    mu, invgaussLoc, scaleInvGauss = stats.invgauss.fit(windFarmWinds)

    gammaParameters = [alpha, gammaLoc, scaleGamma]
    invertGaussParameters = [mu, invgaussLoc, scaleInvGauss]

    return (gammaParameters, invertGaussParameters)

def windFarmBestDistribution(windFarmWinds):

    gammaParameters = getDistributionParameters(windFarmWinds)[0]
    invertGaussParameters = getDistributionParameters(windFarmWinds)[1]

    span = int(max(windFarmWinds))
    x = np.linspace(0, span, span)

    fig, ax = plt.subplots()
    ax.hist(windFarmWinds, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA') # Plot histogram of nums1
    

    #Gamma distribution
    #takes gamma parameters

    gammaPdf = stats.gamma.pdf(x, gammaParameters[0], gammaParameters[1], gammaParameters[2])

    #Invert Gauss distribution
    
    invGaussPdf = stats.invgauss.pdf(x, invertGaussParameters[0], invertGaussParameters[1], invertGaussParameters[2])


    #create plot of Gamma distribution
    plt.plot(x, gammaPdf)
    plt.plot(x, invGaussPdf)

    #display plot
    plt.show()


# windFarmBestDistribution(WindBeauvechain)
# windFarmBestDistribution(WindElsenborn)
