from Q1 import ElecPowerCapa
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
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

#Graph

GammaStyle = dict(color='red', linewidth=4)
InvGaussStyle = dict(color='purple', linewidth=4)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindBeauvechain, bins=100, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA') # Plot histogram of nums1
ax.hist(WindElsenborn, bins=100, density=True, color='wheat', edgecolor='slategrey', label='Elsenborn DATA') # Plot histogram of nums2

#MLE curves
sns.distplot(
    WindElsenborn,
    hist=None,
    kde=False, 
    fit=stats.gamma, 
    fit_kws=dict(color='cornflowerblue', linewidth=4, label='Elsenborn gamma fit')
)

sns.distplot(
    WindBeauvechain,
    hist=None,
    kde=False, 
    fit=stats.gamma, 
    fit_kws=dict(color='sienna', linewidth=4, label='Beauvechain gamma fit')
)

sns.distplot(
    WindElsenborn,
    hist=None,
    kde=False, 
    fit=stats.invgauss, 
    fit_kws=dict(color='royalblue', linewidth=4, label='Elsenborn inv gauss fit')
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
plt.title("Wind speeds compared in Beauvechain and Elsenborn (normed graph)")
plt.legend()
plt.show()