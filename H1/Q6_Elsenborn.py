from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from Q4 import WindElsenborn, getDistributionParameters

#get the gamma distribution parameters with MLE
alphaMLE, locMLE, scaleMLE = getDistributionParameters(WindElsenborn)[1]

#takes the highest wind
span = int(max(WindElsenborn))
x = np.linspace(0, span, span)

fig,ax = plt.subplots() # Instantiate figure and axes object
ax.hist(WindElsenborn, bins=span, density=True, color='palevioletred', edgecolor='slategrey', label='Beauvechain DATA')

# Compute the value of the two moments
M1 = np.mean(WindElsenborn)
M2 = 0
for i in WindElsenborn:
    M2 += i**2
M2 = M2/len(WindElsenborn)

# Compute gamma estimators from M1 and M2 
alphaMM = M1**2 / (M2 - M1**2)
betaMM = sqrt((M2 - M1**2)/alphaMM)

pdfGammaMLE = stats.invgauss.pdf(x, a = alphaMM, scale = betaMM)
pdfGammaMM = stats.invgauss.pdf(x, alphaMLE, locMLE, scaleMLE)

print("alpha MM:", alphaMM)
print("beta MM:", betaMM)
print("alpha MLE:", alphaMLE)
print("beta MLE:", scaleMLE)

plt.plot(x,pdfGammaMLE, label="Gamma fit MLE")
plt.plot(x,pdfGammaMM, label="gamma fit MM")
plt.xlabel("Wind speed (km/h)")
plt.ylabel("Nb") 
plt.title("Wind speeds in Beauvechain(normed graph)")
plt.legend()
plt.show()

