from math import gamma
from scipy import stats
from Q4 import getDistributionParameters, WindBeauvechain, WindElsenborn
#extract fitted gamma parameters for Beauvechain
fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv = getDistributionParameters(WindBeauvechain)[0]
#extract fitted gamma parameters for Elsenborn
fitted_alphaElsen, fitted_gammaLocElsen, fitted_scaleGammaElsen = getDistributionParameters(WindElsenborn)[0]

#Gamma values for Wind of Beauvechain in KM/H
