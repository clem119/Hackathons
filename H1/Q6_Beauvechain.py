from math import *
from turtle import st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q4 import WindBeauvechain


#graph
GammaStyle = dict(color='red', linewidth=4)
InvGaussStyle = dict(color='purple', linewidth=4)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindBeauvechain, bins=100, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA')

span = int(max(WindBeauvechain))
x = np.linspace(0, span, span)

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

y_gamma = stats.gamma.pdf(x, a = alphabeauvechin, scale = betabeauvechin)
y_inv_gauss = stats.invgauss.pdf(x, mu = mubeauvechin, scale = deltabeauvechin)


plt.plot(x,y_gamma)
plt.plot(x,y_inv_gauss)
plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds in Beauvechain(normed graph)")
plt.legend()
plt.show()

