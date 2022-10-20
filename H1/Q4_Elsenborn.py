import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q4 import WindElsenborn

#Graph

GammaStyle = dict(color='red', linewidth=4)
InvGaussStyle = dict(color='purple', linewidth=4)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindElsenborn, bins=100, density=True, color='skyblue', edgecolor='slategrey', label='Elsenborn DATA') # Plot histogram of nums2

#MLE curves
sns.distplot(
    WindElsenborn,
    hist=None,
    kde=False, 
    fit=stats.gamma, 
    fit_kws=dict(color='cornflowerblue', linewidth=4, label='Elsenborn gamma fit')
)

sns.distplot(
    WindElsenborn,
    hist=None,
    kde=False, 
    fit=stats.invgauss, 
    fit_kws=dict(color='royalblue', linewidth=4, label='Elsenborn inv gauss fit')
)


plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds in Elsenborn (normed graph)")
plt.legend()
plt.show()