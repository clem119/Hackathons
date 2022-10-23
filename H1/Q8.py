import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q4 import WindBeauvechain
from Q6_Beauvechain import alphaMM, betaMM

#get the gamma distribution parameters
alpha, loc, scale = getDistributionParameters(WindBeauvechain)[0]

#takes the highest wind
span = int(max(WindBeauvechain))
x = np.linspace(0, span, span)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindBeauvechain, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA')

# Compute the value of the two moments
M1 = np.mean(WindBeauvechain)
M2 = 0
for i in WindBeauvechain:
    M2 += i**2
M2 = M2/len(WindBeauvechain)

# Compute gamma estimators from M1 and M2 
alphaMM = M1**2 / (M2 - M1**2)
betaMM = sqrt((M2 - M1**2)/alphaMM)

fig,(ax1, ax2) = plt.subplots(2)

span = int(max(WindBeauvechain))
x = np.linspace(0, span, span)

gamma_pdf = stats.gamma.pdf(x , a = alphaMM, scale = betaMM)

#compute M pdf 
M_PDF = 30*((np.cumsum(gamma_pdf))**29) * gamma_pdf
M_CFD = (np.cumsum(M_PDF))



ax1.plot(x, M_PDF)
ax1.set_title("Xmax PDF")
ax2.plot(x, M_CFD)
ax2.set_title("Xmax CFD")
plt.xlabel("Wind speed (km/h)") 
plt.legend()
plt.show()