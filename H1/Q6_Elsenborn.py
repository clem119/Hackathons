from math import *
from turtle import st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q4 import WindElsenborn


#graph
GammaStyle = dict(color='red', linewidth=4)
InvGaussStyle = dict(color='purple', linewidth=4)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindElsenborn, bins=100, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA')

span = int(max(WindElsenborn))
x = np.linspace(0, span, span)

# Compute the value of the two moments
n = len(WindElsenborn)
print(n)
M1 = np.sum(WindElsenborn)/n
M2 = 0
for i in WindElsenborn:
    M2 += i**2
M2 = M2/n

# Compute gamma estimators from M1 and M2 
alphaElsenborn = M1**2 / (M2 - M1**2)
betaElsenborn = sqrt((M2 - M1**2)/alphaElsenborn)

# Compute inverse gaussian estimators from M1 and M2 
muElsenborn = M1
deltaElsenborn = M1**3 / (M2 - M1**2)

print(muElsenborn, deltaElsenborn)

y_gamma = stats.gamma.pdf(x, a = alphaElsenborn, scale = betaElsenborn)
y_inv_gauss = stats.invgauss.pdf(x, mu = muElsenborn, scale = deltaElsenborn)


plt.plot(x,y_gamma)
plt.plot(x,y_inv_gauss)
plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds in Elsenborn(normed graph)")
plt.legend()
plt.show()