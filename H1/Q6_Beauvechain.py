from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from Q4 import WindBeauvechain, getDistributionParameters

#get the gamma distribution parameters
alpha, loc, scale = getDistributionParameters(WindBeauvechain)[0]

#takes the highest wind
span = int(max(WindBeauvechain))
x = np.linspace(0, span, span)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindBeauvechain, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA')

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

pdfGammaMLE = stats.gamma.pdf(x, a = alphaMM, scale = betaMM)
pdfGammaMM = stats.gamma.pdf(x, alpha, loc, scale)

print("alpha MM:", alphaMM)
print("beta MM:", betaMM)
print("alpha MLE:", alpha)
print("beta MLE:", scale)

plt.plot(x,pdfGammaMLE, label="Gamma fit MLE")
plt.plot(x,pdfGammaMM, label="gamma fit MM")
plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds in Beauvechain(normed graph)")
plt.legend()
plt.show()

