import math 
from scipy import stats
from Q4 import getDistributionParameters, WindBeauvechain, WindElsenborn

#extract fitted gamma parameters for Beauvechain
fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv = getDistributionParameters(WindBeauvechain)[0]
#extract fitted gamma parameters for Elsenborn
fitted_alphaElsen, fitted_gammaLocElsen, fitted_scaleGammaElsen = getDistributionParameters(WindElsenborn)[0]

#Gamma values for Wind of Beauvechain in KM/H
windMedianBeauv = stats.gamma.median(fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv)
windStdBeauv = stats.gamma.std(fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv)
windPercentilBeauv = stats.gamma.ppf([0.05, 0.95],fitted_alphaBeauv, fitted_gammaLocBeauv, fitted_scaleGammaBeauv) #put in an array the value for 5% and 95%

#Gamma values for Wind of Elsenborn in KM/H
windMedianElsen = stats.gamma.median(fitted_alphaElsen, fitted_gammaLocElsen, fitted_scaleGammaElsen)
windStdElsen = stats.gamma.std(fitted_alphaElsen, fitted_gammaLocElsen, fitted_scaleGammaElsen)
windPercentilElsen = stats.gamma.ppf([0.05, 0.95],fitted_alphaElsen, fitted_gammaLocElsen, fitted_scaleGammaElsen)

#constants
PI = math.pi
RHO = 1.2
S = (32**2)*PI

#take a wind speed in km/h and convert in MW
def windToPower(windSpeed):
    windSpeed = (windSpeed/3.6)**3
    Pk=8*0.5*RHO*S*windSpeed
    Pe = Pk*0.42 #because of the betz limit
    Pe = Pe/(10**6) #convert  in MW
    return Pe

#get power values for Beauvechain
powerMedianBeauv = windToPower(windMedianBeauv)
powerStdBeauv = windToPower(windStdBeauv)
powerSmallPercentilBeauv = windToPower(windPercentilBeauv[0])
powerBigPercentilBeauv = windToPower(windPercentilBeauv[1])

#get power values for Beauvechain
powerMedianElsen = windToPower(windMedianElsen)
powerStdElsen = windToPower(windStdElsen)
powerSmallPercentilElsen = windToPower(windPercentilElsen[0])
powerBigPercentilElsen = windToPower(windPercentilElsen[1])

print("Value gamma distribution for Beauvechain: ")
print("Expected and median powers for each farm (MW): {}".format(powerMedianBeauv))
print("Standard deviation of powers for each farm (MW): {}".format(powerStdBeauv))
print("5% and 95% percentiles of powers for each farm (MW): {} and {}".format(powerSmallPercentilBeauv, powerBigPercentilBeauv))

print("==========================================================================")

print("Value gamma distribution for Elsenborn: ")
print("Expected and median powers for each farm (MW): {}".format(powerMedianElsen))
print("Standard deviation of powers for each farm (MW): {}".format(powerStdElsen))
print("5% and 95% percentiles of powers for each farm (MW): {} and {}".format(powerSmallPercentilElsen, powerBigPercentilElsen))






