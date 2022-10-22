
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q4 import WindBeauvechain

#Graph
GammaStyle = dict(color='red', linewidth=4)
InvGaussStyle = dict(color='purple', linewidth=4)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindBeauvechain, bins=100, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA') # Plot histogram of nums1

span = int(max(WindBeauvechain))


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

print(fitted_muB , fitted_scaleInvGaussB)
#MLE curves

sns.distplot(
    WindBeauvechain,
    hist=None,
    kde=False, 
    fit=stats.gamma, 
    fit_kws=dict(color='sienna', linewidth=4, label='Beauvechain gamma fit')
)

sns.distplot(
    WindBeauvechain,
    hist=None,
    kde=False, 
    fit=stats.invgauss, 
    fit_kws=dict(color='maroon', linewidth=4, label='Beauvechain inv gauss fit')
)

plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds in Beauvechain(normed graph)")
plt.legend()
plt.show()