import imp
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

# Compute the value of the two moments
n = len(WindBeauvechain)
M1 = np.sum(WindBeauvechain)/n
M2 = 0
for i in WindBeauvechain:
    M2 += i**2
M2 = M2/n

# Compute gamma estimators from M1 and M2 
alphabeauvechin = M1**2 / (M2 - M1**2)
betabeauvechin = M2 / M1 - 1

# Compute inverse gaussian estimators from M1 and M2 
mubeauvechin = M2 - M1**2
deltabeauvechin = M1**3 / (M2 - M1**2)

x = np.linspace(0, 100, 100)
y = stats.gamma.pdf(x, a = alpha, scale = beta)

plt.plot(x,y)
plt.show()

