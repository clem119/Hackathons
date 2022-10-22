import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q4 import WindElsenborn
#Graph

#only keep date from 20170101 to 20210101 for Beauvechain
Elsenborn = pd.read_csv("Elsenborn.csv", sep=",")

#put all the non trusted value (!= 0) in ErrorsElsenborn and ErrorsBeauvechain
ErrorsElsenborn=Elsenborn.loc[Elsenborn[" Q_FG"] != 0]

#only keep the wind speed values
fig, ax = plt.subplots(1, 1)
WindElsenborn = np.array(Elsenborn["   FG"])
gamma=stats.gamma

X = WindElsenborn
step = 0.1
minVal = 0
maxVal = int(max(X)/step) + 1
x = [i*step for i in range(minVal, maxVal)]

# Histogram
numberOfBins = int(len(x)/10)

# Theta vectors
theta_vectors = {}
        
## GAMMA
# Gamma fitting using scipy
fit_alpha, fit_loc, fit_beta=gamma.fit(X)
gamma_fitted_Y = gamma.pdf(x=x, a=fit_alpha, loc=fit_loc, scale=fit_beta)
ax.plot(x, gamma_fitted_Y, 'b-', lw=2, alpha=0.8, label='Gamma fitted distribution')
theta_vectors['gammaDistribution'] = [fit_alpha, fit_loc, fit_beta]
plt.show()



# fig,ax = plt.subplots() # Instantiate figure and axes object
# ax.hist(WindElsenborn, bins=100, density=True, color='skyblue', edgecolor='slategrey', label='Elsenborn DATA') # Plot histogram of nums2

# #MLE curves
# sns.distplot(
#     WindElsenborn,
#     hist=None,
#     kde=False, 
#     fit=stats.gamma, 
#     fit_kws=dict(color='cornflowerblue', linewidth=4, label='Elsenborn gamma fit')
# )

# sns.distplot(
#     WindElsenborn,
#     hist=None,
#     kde=False, 
#     fit=stats.invgauss, 
#     fit_kws=dict(color='royalblue', linewidth=4, label='Elsenborn inv gauss fit')
# )

# #takes gamma parameters
# alphaElsenborn = stats.gamma.fit(WindElsenborn)[0]
# betaElsenborn = stats.gamma.fit(WindElsenborn)[2]

# #takes invert gauss parameters
# muElsenborn = stats.invgauss.fit(WindElsenborn)[0]
# lambdElsenborn = stats.invgauss.fit(WindElsenborn)[2]


# plt.xlabel("Wind speed (km/h)")
# plt.ylabel("Nb") 
# plt.title("Wind speeds in Elsenborn (normed graph)")
# plt.legend()
# plt.show()