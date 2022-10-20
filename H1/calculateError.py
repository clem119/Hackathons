import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from Q4 import WindElsenborn


#takes gamma parameters
shapeGammaElsenborn = stats.gamma.fit(WindElsenborn)[0]
locationGammaElsenborn = stats.gamma.fit(WindElsenborn)[1]
scaleGammaElsenborn = stats.gamma.fit(WindElsenborn)[2]
print("ShapeGammaElsenborn: {} \nLocationGammaElsenborn: {} \nScaleGammaElsenborn: {}\n".format(shapeGammaElsenborn, locationGammaElsenborn, scaleGammaElsenborn))


#takes invert gauss parameters
shapeInvGaussElsenborn = stats.invgauss.fit(WindElsenborn)[0]
locationInvGaussElsenborn = stats.invgauss.fit(WindElsenborn)[1]
scaleInvGaussElsenborn = stats.invgauss.fit(WindElsenborn)[2]

x = np.linspace (0, 150, 150)

gammaPdf = stats.gamma.pdf(x, shapeGammaElsenborn, scale=scaleGammaElsenborn)
invGaussPdf = stats.invgauss.pdf(x, shapeInvGaussElsenborn, scale=scaleInvGaussElsenborn)

plt.plot(x, gammaPdf)
plt.plot(x, invGaussPdf)

plt.show()