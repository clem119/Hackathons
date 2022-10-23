from math import *
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from Q4 import WindBeauvechain
from Q5 import fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv



span = int(max(WindBeauvechain))
x = np.linspace(0, span, span)
#graph
GammaStyle = dict(color='red', linewidth=4)
InvGaussStyle = dict(color='purple', linewidth=4)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindBeauvechain, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA')

# Compute the value of the two moments
n = len(WindBeauvechain)
print(n)
M1 = np.sum(WindBeauvechain)/n
M2 = 0
for i in WindBeauvechain:
    M2 += i**2
M2 = M2/n

# Compute gamma estimators from M1 and M2 
alphabeauvechin = M1**2 / (M2 - M1**2)
betabeauvechin = sqrt((M2 - M1**2)/alphabeauvechin)

# Compute inverse gaussian estimators from M1 and M2 
mubeauvechin = M1
deltabeauvechin = M1**3 / (M2 - M1**2)

print(mubeauvechin, deltabeauvechin)

pdfGammaMLE = stats.gamma.pdf(x, a = alphabeauvechin, scale = betabeauvechin)
pdfGammaMM = stats.gamma.pdf(x, fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv)

print("alpha MM:", alphabeauvechin)
print("beta MM:", betabeauvechin)
print("alpha MLE:", fitted_alphaBeauv)
print("beta MLE:", fitted_scaleGammaBeauv)

plt.plot(x,pdfGammaMLE)
plt.plot(x,pdfGammaMM)
plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds in Beauvechain(normed graph)")
plt.legend()
plt.show()

