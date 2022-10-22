import imp
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

#takes gamma parameters
alphaBeauvechain = stats.gamma.fit(WindBeauvechain)[0]
betaBeauvechain = stats.gamma.fit(WindBeauvechain)[2]
paramGammaB = stats.gamma.fit(WindBeauvechain)

#takes invert gauss parameters
muBeauvechain = stats.invgauss.fit(WindBeauvechain)[0]
lambdBeauvechain = stats.invgauss.fit(WindBeauvechain)[2]
paramInvGaussB = stats.invgauss.fit(WindBeauvechain)

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