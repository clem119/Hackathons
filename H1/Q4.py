import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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

def getDistributionParameters(windFarmWinds):

    #Gamma distribution
    #takes gamma parameters
    fitted_alphaB, fitted_gammaLocB, fitted_scaleGammaB = stats.gamma.fit(windFarmWinds)

    #Invert Gauss distribution
    #takes invert gauss parameters
    fitted_muB, fitted_invgaussLocB, fitted_scaleInvGaussB = stats.invgauss.fit(windFarmWinds)

    gammaParameters = [fitted_alphaB, fitted_gammaLocB, fitted_scaleGammaB]
    invertGaussParameters = [fitted_muB, fitted_invgaussLocB, fitted_scaleInvGaussB]

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
