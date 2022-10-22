import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
from Q4 import WindBeauvechain


span = int(max(WindBeauvechain))
fig,ax = plt.subplots()
ax.hist(WindBeauvechain, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA') # Plot histogram of nums1



#used get value of the pdf for the highest value of wind registered
x = np.linspace(0, span, span)

#Gamma distribution
#takes gamma parameters
fitted_alphaB, fitted_gammaLocB, fitted_scaleGammaB = stats.gamma.fit(WindBeauvechain)
gammaPdf = stats.gamma.pdf(x, fitted_alphaB, fitted_gammaLocB, fitted_scaleGammaB)

#Invert Gauss distribution
#takes invert gauss parameters
fitted_muB, fitted_invgaussLocB, fitted_scaleInvGaussB = stats.invgauss.fit(WindBeauvechain)
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